# coding=utf-8
from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
import os
import re
import time
import shutil
import subprocess

# hardcoded values
library_name = 'Библиотека'
edit_content_name = 'Редактировать содержимое'
edit_name = 'Редактировать'
page_name_class = 'pageName'
objects_name = 'Объекты '
book_number0_id = 'book_number0'
book_name1_id = 'book_name1'
change_name = 'Изменить'
book_chapters = 'Книга. Главы'
book_parts = 'Книга. Части'
book_pages = 'Книга. Страницы'
chapter_parts = 'Глава. Части'
chapter_pages = 'Глава. Страницы'
part_pages = 'Часть. Страницы'
book_name_input_name = 'book_name'
chapter_name_td_id = 'chapter_name1'

page_number_in_list_id = 'page_number'
page_name_in_list_id = 'page_name'
chapter_name_in_list_id = 'chapter_name'
part_name_in_list_id = 'part_name'

page_prefix = 'Страница '

# config
password = '7DaJVD8a'
book_config_file_name = 'config.yaml'


class LoginManager:
    def __init__(self, driver):
        self.driver = driver
        pass

    def login(self):
        self.driver.get('http://secretdoctrine.ru/my/s3/login/')
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_name('enter').click()


class ContentElement:
    def __init__(self, name, element_type, page):
        self.name = name
        self.element_type = element_type
        self.page = page


# noinspection PyBroadException
class LibraryWorker:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 3
        self.book_name = ''
        self.contents_elements = []
        self.min_page = 10000
        self.max_page = -10000
        pass

    def find_element_by_xpath_wrapper(self, parent, xpath):
        try:
            return parent.find_element_by_xpath(xpath)
        except:
            time.sleep(self.timeout)
            return parent.find_element_by_xpath(xpath)

    def find_elements_by_xpath_wrapper(self, parent, xpath):
        try:
            return parent.find_elements_by_xpath(xpath)
        except:
            time.sleep(self.timeout)
            return parent.find_elements_by_xpath(xpath)

    def find_element_by_id_wrapper(self, parent, element_id):
        try:
            return parent.find_element_by_id(element_id)
        except:
            time.sleep(self.timeout)
            return parent.find_element_by_id(element_id)

    def find_elements_by_id_wrapper(self, parent, element_id):
        try:
            return parent.find_elements_by_id(element_id)
        except:
            time.sleep(self.timeout)
            return parent.find_elements_by_id(element_id)

    def find_element_by_css_selector_wrapper(self, parent, css_selector):
        try:
            return parent.find_element_by_css_selector(css_selector)
        except:
            time.sleep(self.timeout)
            return parent.find_element_by_css_selector(css_selector)

    def find_elements_by_css_selector_wrapper(self, parent, css_selector):
        try:
            return parent.find_elements_by_css_selector(css_selector)
        except:
            time.sleep(self.timeout)
            return parent.find_elements_by_css_selector(css_selector)

    def open_library(self):
        self.driver.find_element_by_xpath(
            '//span[text()="%s" and @class="%s"]' % (library_name, page_name_class)).click()
        self.driver.find_element_by_xpath('//span[text()="%s"]' % edit_content_name).click()

        element = self.driver.find_element_by_xpath('//div[span[text()="%s"]]' % objects_name)
        element = element.find_element_by_xpath('li/span[text()="%s"]' % edit_name)
        element.click()

    def fill_part_pages(self):
        element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % part_pages)
        min_part_page = self.get_pages_array_from_current_browser_pages(element)
        self.driver.execute_script('popupController.closeLastPopup()')

        return min_part_page

    def fill_parts(self, root):
        min_page_of_parts = 10000
        # it's quite possible to have no parts
        try:
            parts = self.find_elements_by_xpath_wrapper(root, 'table/tbody/tr')
        except NoSuchElementException:
            return min_page_of_parts

        for part in parts:
            element = self.find_element_by_css_selector_wrapper(part, 'td[id*="%s"]' % part_name_in_list_id)
            part_name = element.text
            element = self.find_element_by_xpath_wrapper(part, 'td/span[text()[normalize-space()]="%s"]' % change_name)
            element.click()
            min_part_page = self.fill_part_pages()
            if min_part_page < min_page_of_parts:
                min_page_of_parts = min_part_page
            self.contents_elements.append(ContentElement(part_name, 'part', min_part_page))
        return min_page_of_parts

    def process_chapter(self):

        element = self.find_element_by_xpath_wrapper(self.driver, '//div[b[contains(text(), "%s")]]' % chapter_parts)
        min_parts_page = self.fill_parts(element)
        element = self.find_element_by_xpath_wrapper(self.driver, '//div[b[contains(text(), "%s")]]' % chapter_pages)
        min_page = self.get_pages_array_from_current_browser_pages(element)

        self.driver.execute_script('popupController.closeLastPopup()')

        return min(min_parts_page, min_page)

    def get_pages_array_from_current_browser_pages(self, root):

        # element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % book_pages)
        local_min_page = 10000
        pages = self.find_elements_by_xpath_wrapper(root, 'table/tbody/tr')
        for page in pages:
            element = self.find_element_by_css_selector_wrapper(page, 'td[id*="%s"]' % page_number_in_list_id)
            page_num = int(element.text)
            if page_num < self.min_page:
                self.min_page = page_num
            if page_num < local_min_page:
                local_min_page = page_num
            if page_num > self.max_page:
                self.max_page = page_num

            element = self.find_element_by_css_selector_wrapper(page, 'td[id*="%s"]' % page_name_in_list_id)
            if not re.match(page_prefix + ' (\d+)', element.text):
                self.contents_elements.append(ContentElement(element.text, 'page', page_num))
        return local_min_page

    def edit_book(self, book_number, book_name):

        element = self.find_element_by_xpath_wrapper(self.driver, '//form/div/input[@name="%s"]' %
                                                     book_name_input_name)
        element.send_keys(book_name)
        element.submit()

        element = self.driver.find_element_by_xpath(
            '//td[@id="%s" and contains(text(), "%s")]' % (book_number0_id, book_number))
        name_element = element.find_element_by_xpath('../td[@id="%s"]' % book_name1_id)
        self.book_name = name_element.text
        element = element.find_element_by_xpath('../td/span[text()[normalize-space()]="%s"]' % change_name)
        element.click()

        element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % book_chapters)
        chapters = element.find_elements_by_xpath('table/tbody/tr')

        for chapter in chapters:
            element = self.find_element_by_id_wrapper(chapter, chapter_name_td_id)
            chapter_name = element.text
            element = chapter.find_element_by_xpath('td/span[text()[normalize-space()]="%s"]' % change_name)
            element.click()
            chapter_page = self.process_chapter()
            self.contents_elements.append(ContentElement(chapter_name, 'chapter', chapter_page))

        element = self.find_element_by_xpath_wrapper(self.driver, '//div[b[contains(text(), "%s")]]' % book_parts)
        self.fill_parts(element)

        element = self.find_element_by_xpath_wrapper(self.driver, '//div[b[contains(text(), "%s")]]' % book_pages)
        self.get_pages_array_from_current_browser_pages(element)

class PdfConverter:
    def __init__(self, pdf_files_path, additional_options):
        self.pdf_files_path = pdf_files_path
        self.converter_name = 'pdf2htmlex'
        self.additional_options = additional_options
        self.tmp_file_name = 'tmp.tmp'

    def convert(self):
        # command_line = os.path.join(self.pdf_converter_path, self.converter_name) + ' '
        #command_line += self.dest_dir_specifier + self.pdf_files_path + ' '
        for file_name in os.listdir(self.pdf_files_path):
            full_path = os.path.join(self.pdf_files_path, file_name)
            if not os.path.isfile(full_path):
                continue
            match = re.search('(.+)\.pdf', file_name)
            if not match:
                continue

            args = [self.converter_name]
            for option in self.additional_options:
                args.append(option)
            args.append('--dest-dir=' + self.pdf_files_path)
            args.append(full_path)

            print("Converting %s" % full_path)
            subprocess.call(args)

def grab_content(book_number, book_name, input_folder, output_folder, yml_name='config.yml'):

    new_folder = os.path.join(output_folder, os.path.basename(os.path.normpath(input_folder)))
    if os.path.exists(new_folder):
        shutil.rmtree(new_folder)
    os.makedirs(new_folder)

    i = 1

    for file in sorted(os.listdir(input_folder), key=lambda x: x.lower()):
        if file[0] == '.':
            continue
        shutil.copyfile(os.path.join(input_folder, file), os.path.join(new_folder, str(i).zfill(4) + '.pdf'))
        i += 1

    driver = webdriver.Firefox()

    LoginManager(driver).login()

    library_worker = LibraryWorker(driver)

    library_worker.open_library()
    library_worker.edit_book(book_number, book_name)
    driver.close()
    with open(os.path.join(new_folder, yml_name), 'w', encoding='utf-8') as f:
        f.write('pdf_regex: \'^(\d+).pdf$\'\n')
        f.write('html_regex: \'^(.+).html$\'\n')
        f.write('book:\n')
        f.write('  picture_path: \n')
        f.write('  book_file: \n')
        f.write('  name_prefix: \n')
        f.write('  tree_prefix: \n')
        f.write('  name: \'%s\'\n' % library_worker.book_name)
        f.write('  name_comment: \n')
        f.write('  page_count: \'%d\'\n' % (library_worker.max_page - library_worker.min_page + 1))
        f.write('  first_page: \'%d\'\n' % library_worker.min_page)
        f.write('  synopsis: \n')
        f.write('  contents: \n')

        for contents_element in sorted(library_worker.contents_elements, key=lambda x: x.page):
            f.write('  ' * 2 + '- \n')
            f.write('  ' * 3 + 'name: \'' + contents_element.name + '\'\n')
            f.write('  ' * 3 + 'page: ' + '\'' + str(contents_element.page) + '\'\n')
            f.write('  ' * 3 + 'type: \'' + contents_element.element_type + '\'\n')
    PdfConverter(new_folder,
                 ['--fallback=1', '--zoom=1.5',
                 '--data-dir=/usr/local/opt/pdf2htmlex/share/pdf2htmlEX/',
                 '--stretch-narrow-glyph=1',
                 '--process-outline=0']).convert()


def __main__():

    grab_content(
        '4102',
        'Чаша Христа',
        '/Users/schrecknetuser/Downloads/Документы/1. Мысль/2. Чаша Христа',
        '/Users/schrecknetuser/pdf-ocr/documents/Мысль')

    grab_content(
        '4103',
        'Канченджанга',
        '/Users/schrecknetuser/Downloads/Документы/1. Мысль/3. Канченджанга',
        '/Users/schrecknetuser/pdf-ocr/documents/Мысль')

    grab_content(
        '4104',
        'Весть Шамбалы',
        '/Users/schrecknetuser/Downloads/Документы/1. Мысль/4. весть шамбалы',
        '/Users/schrecknetuser/pdf-ocr/documents/Мысль')

    grab_content(
        '4105',
        'Молния. Зов неба',
        '/Users/schrecknetuser/Downloads/Документы/1. Мысль/5. Молния. Зов неба.',
        '/Users/schrecknetuser/pdf-ocr/documents/Мысль')

    grab_content(
        '4106',
        'Распятое человечество',
        '/Users/schrecknetuser/Downloads/Документы/1. Мысль/6. распятое человечество',
        '/Users/schrecknetuser/pdf-ocr/documents/Мысль')

    grab_content(
        '4107',
        'Пиета',
        '/Users/schrecknetuser/Downloads/Документы/1. Мысль/7. Пиета',
        '/Users/schrecknetuser/pdf-ocr/documents/Мысль')

    grab_content(
        '4108',
        'Завет учителя',
        '/Users/schrecknetuser/Downloads/Документы/1. Мысль/8. Завет учителя',
        '/Users/schrecknetuser/pdf-ocr/documents/Мысль')

    grab_content(
        '4109',
        'Мысль',
        '/Users/schrecknetuser/Downloads/Документы/1. Мысль/9. Мысль',
        '/Users/schrecknetuser/pdf-ocr/documents/Мысль')

    grab_content(
        '4110',
        'Красные кони',
        '/Users/schrecknetuser/Downloads/Документы/1. Мысль/10. Красные кони',
        '/Users/schrecknetuser/pdf-ocr/documents/Мысль')




    grab_content(
        '4201',
        'На вершинах',
        '/Users/schrecknetuser/Downloads/Документы/2. Армагеддон/1. на вершинах',
        '/Users/schrecknetuser/pdf-ocr/documents/Армагеддон')

    grab_content(
        '4202',
        'Вестник',
        '/Users/schrecknetuser/Downloads/Документы/2. Армагеддон/2. вестник',
        '/Users/schrecknetuser/pdf-ocr/documents/Армагеддон')

    grab_content(
        '4203',
        'Победа',
        '/Users/schrecknetuser/Downloads/Документы/2. Армагеддон/3. победа',
        '/Users/schrecknetuser/pdf-ocr/documents/Армагеддон')

    grab_content(
        '4204',
        'Бэда-проповедник',
        '/Users/schrecknetuser/Downloads/Документы/2. Армагеддон/4. Бэда проповедник',
        '/Users/schrecknetuser/pdf-ocr/documents/Армагеддон')

    grab_content(
        '4205',
        'Сошествие во Ад',
        '/Users/schrecknetuser/Downloads/Документы/2. Армагеддон/5. сошествие во ад',
        '/Users/schrecknetuser/pdf-ocr/documents/Армагеддон')

    grab_content(
        '4206',
        'Мы сами строим свои тюрьмы',
        '/Users/schrecknetuser/Downloads/Документы/2. Армагеддон/6. мы сами строим',
        '/Users/schrecknetuser/pdf-ocr/documents/Армагеддон')

    grab_content(
        '4207',
        'Ты не должен видеть этого пламени',
        '/Users/schrecknetuser/Downloads/Документы/2. Армагеддон/7. ты не должен',
        '/Users/schrecknetuser/pdf-ocr/documents/Армагеддон')

    grab_content(
        '4208',
        'Я двигаюсь среди этих теней',
        '/Users/schrecknetuser/Downloads/Документы/2. Армагеддон/8. я двигаюсь',
        '/Users/schrecknetuser/pdf-ocr/documents/Армагеддон')

    grab_content(
        '4209',
        'Ангел последний',
        '/Users/schrecknetuser/Downloads/Документы/2. Армагеддон/9. Ангел последний',
        '/Users/schrecknetuser/pdf-ocr/documents/Армагеддон')

    grab_content(
        '4210',
        'Молчание',
        '/Users/schrecknetuser/Downloads/Документы/2. Армагеддон/10. молчание',
        '/Users/schrecknetuser/pdf-ocr/documents/Армагеддон')


    grab_content(
        '4301',
        'Чантанг',
        '/Users/schrecknetuser/Downloads/Документы/3. Сознание красоты спасет/1. Чантанг',
        '/Users/schrecknetuser/pdf-ocr/documents/Сознание красоты спасет')

    grab_content(
        '4302',
        'Чинтамани',
        '/Users/schrecknetuser/Downloads/Документы/3. Сознание красоты спасет/2. Чинтамани',
        '/Users/schrecknetuser/pdf-ocr/documents/Сознание красоты спасет')

    grab_content(
        '4303',
        'Жемчуг исканий',
        '/Users/schrecknetuser/Downloads/Документы/3. Сознание красоты спасет/3. Жемчуг исканий',
        '/Users/schrecknetuser/pdf-ocr/documents/Сознание красоты спасет')

    grab_content(
        '4304',
        'Священная флейта',
        '/Users/schrecknetuser/Downloads/Документы/3. Сознание красоты спасет/4. Священная флейта',
        '/Users/schrecknetuser/pdf-ocr/documents/Сознание красоты спасет')

    grab_content(
        '4305',
        'Знаки Христа',
        '/Users/schrecknetuser/Downloads/Документы/3. Сознание красоты спасет/5. Знаки Христа',
        '/Users/schrecknetuser/pdf-ocr/documents/Сознание красоты спасет')

    grab_content(
        '4306',
        'Путь на Кайлас',
        '/Users/schrecknetuser/Downloads/Документы/3. Сознание красоты спасет/6. Путь на Кайлас',
        '/Users/schrecknetuser/pdf-ocr/documents/Сознание красоты спасет')

    grab_content(
        '4307',
        'Добрый самаритянин',
        '/Users/schrecknetuser/Downloads/Документы/3. Сознание красоты спасет/7. Добрый самаритянин',
        '/Users/schrecknetuser/pdf-ocr/documents/Сознание красоты спасет')

    grab_content(
        '4308',
        'Гуру Камба-ла',
        '/Users/schrecknetuser/Downloads/Документы/3. Сознание красоты спасет/8. Гуру Камба-ла',
        '/Users/schrecknetuser/pdf-ocr/documents/Сознание красоты спасет')

    grab_content(
        '4309',
        'И мы приближаемся',
        '/Users/schrecknetuser/Downloads/Документы/3. Сознание красоты спасет/9. И мы приближаемся',
        '/Users/schrecknetuser/pdf-ocr/documents/Сознание красоты спасет')

    grab_content(
        '4310',
        'Заклинатель огня',
        '/Users/schrecknetuser/Downloads/Документы/3. Сознание красоты спасет/10. Заклинатель огня',
        '/Users/schrecknetuser/pdf-ocr/documents/Сознание красоты спасет')



if __name__ == '__main__':
    __main__()
