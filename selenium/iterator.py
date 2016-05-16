# coding=utf-8
from selenium.common.exceptions import NoSuchElementException

__author__ = 'schrecknetuser'

from selenium import webdriver
import os
import re
import time
import iterator_config

# hardcoded values
library_name = 'Библиотека'
edit_content_name = 'Редактировать содержимое'
edit_name = 'Редактировать'
page_name_class = 'pageName'
object_action_class = 'objectAction'
objects_name = 'Объекты '
book_number0_id = 'book_number0'
change_name = 'Изменить'
select_name = 'Выбрать'
book_chapters = 'Книга. Главы'
book_parts = 'Книга. Части'
book_pages = 'Книга. Страницы'
chapter_parts = 'Глава. Части'
chapter_pages = 'Глава. Страницы'
part_pages = 'Часть. Страницы'
chapter_name = 'Глава'
part_name = 'Часть'
page_name = 'Страница'
add_name = 'Добавить'
add_file_name = 'Добавить файл'
chapter_number_colon = 'Глава. Номер :'
part_number_colon = 'Часть. Номер :'
page_number_colon = 'Страница. Номер :'
book_name_input_name = 'book_name'
chapter_name_input_name = 'chapter_name'
part_name_input_name = 'part_name'
dynamic_databrowser_browse_books = 'dynamic_databrowser3400'
dynamic_databrowser_browse_chapters = 'dynamic_databrowser3600'
dynamic_databrowser_browse_parts = 'dynamic_databrowser3800'
close_name = 'Закрыть'
clone_suffix = '_clone'
pdf_file = 'Файл PDF'
files_name = 'Файлы'
input_files_name = 'files[]'
input_files_type = 'file'
file_container_id = 'file_container'
choose_name = 'выбрать'
chapter_name_td_id = 'chapter_name1'
# save_changes = 'Сохранить изменения'


chapter_number_id = 'chapter_number'
part_number_id = 'part_number'
page_number_id = 'page_number'
chapter_name_id = 'chapter_name'
part_name_id = 'part_name'

page_number_in_list_id = 'page_number'
page_name_in_list_id = 'page_name'
chapter_name_in_list_id = 'chapter_name'
part_name_in_list_id = 'part_name'

default_chapter_name = '____current_chapter'
default_part_name = '____current_part'
page_prefix = 'Страница '

# config
password = '7DaJVD8a'
book_config_file_name = 'config.yaml'

# book config
# book_number = '1341'

yml = True
if yml:
    output_file_name = 'output.yml'
else:
    output_file_name = 'output.py'




class LoginManager:
    def __init__(self, driver):
        self.driver = driver
        pass

    def login(self):
        self.driver.get('http://secretdoctrine.ru/my/s3/login/')
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_name('enter').click()


class LibraryWorker:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 3
        self.output_string = ''
        self.pages_dictionary = {}
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

    def find_element_by_id_wrapper(self, parent, id):
        try:
            return parent.find_element_by_id(id)
        except:
            time.sleep(self.timeout)
            return parent.find_element_by_id(id)

    def find_elements_by_id_wrapper(self, parent, id):
        try:
            return parent.find_elements_by_id(id)
        except:
            time.sleep(self.timeout)
            return parent.find_elements_by_id(id)

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

    def fill_part_pages(self, indent_count):
        element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % part_pages)
        pages_array = self.get_pages_array_from_current_browser_pages(element)
        if len(pages_array) == 0:
            if yml:
                self.output_string += '\t'*(indent_count + 1) + 'pages: \'\''
            else:
                self.output_string += '\t\'\''
        else:
            if yml:
                self.output_string += '\t'*(indent_count + 1) + 'pages: '
                self.output_string += '\'' + str(min(pages_array)).replace('-', '~') + \
                                      '-' + \
                                      str(max(pages_array)).replace('-', '~') + '\'\n'
            else:
                self.output_string += '\t' * indent_count + '\'' + \
                                      str(min(pages_array)).replace('-', '~') + \
                                      '-' + \
                                      str(max(pages_array)).replace('-', '~') + '\''
        self.driver.execute_script('popupController.closeLastPopup()')

    def fill_parts(self, root, indent_count):
        # it's quite possible to have no parts
        try:
            parts = self.find_elements_by_xpath_wrapper(root, 'table/tbody/tr')
        except NoSuchElementException:
            return

        for part in parts:
            if yml:
                self.output_string += '\t' * indent_count + '- \n'
            else:
                self.output_string += '\t' * indent_count + 'Part(\''
            element = self.find_element_by_css_selector_wrapper(part, 'td[id*="%s"]' % part_name_in_list_id)
            if yml:
                self.output_string += '\t' * (indent_count + 1) + 'name: \'' + element.text + '\'\n'
            else:
                self.output_string += element.text + '\',\n'
            element = self.find_element_by_xpath_wrapper(part, 'td/span[text()[normalize-space()]="%s"]' % change_name)
            element.click()
            self.fill_part_pages(indent_count)
            if not yml:
                self.output_string += '),\n'

    def process_chapter(self):

        if not yml:
            self.output_string += '\t\t[\n'

        element = self.find_element_by_xpath_wrapper(self.driver, '//div[b[contains(text(), "%s")]]' % chapter_parts)

        if yml:
            self.output_string += '\t\t\tparts:\n'
            self.fill_parts(element, 4)
        else:
            self.fill_parts(element, 2)

        if not yml:
            self.output_string += '\t\t],\n'

        element = self.find_element_by_xpath_wrapper(self.driver, '//div[b[contains(text(), "%s")]]' % chapter_pages)
        pages_array = self.get_pages_array_from_current_browser_pages(element)
        if yml:
            self.output_string += '\t\t\tpages: \'' + \
                                  str(min(pages_array)).replace('-', '~') + \
                                  '-' + \
                                  str(max(pages_array)).replace('-', '~') + \
                                  '\''
        else:
            self.output_string += '\t\t\'' + \
                                  str(min(pages_array)).replace('-', '~') + \
                                  '-' + \
                                  str(max(pages_array)).replace('-', '~') + \
                                  '\''
        self.output_string += '\n'
        self.driver.execute_script('popupController.closeLastPopup()')

    def get_pages_array_from_current_browser_pages(self, root):
        pages_array = []

        # element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % book_pages)
        pages = self.find_elements_by_xpath_wrapper(root, 'table/tbody/tr')
        for page in pages:
            element = self.find_element_by_css_selector_wrapper(page, 'td[id*="%s"]' % page_number_in_list_id)
            page_num = int(element.text) + iterator_config.shift
            pages_array.append(page_num)

            element = self.find_element_by_css_selector_wrapper(page, 'td[id*="%s"]' % page_name_in_list_id)
            if not element.text == page_prefix + str(page_num - iterator_config.shift):
                self.pages_dictionary[page_num] = element.text.replace(str(page_num - iterator_config.shift),
                                                                       str(page_num))

        return pages_array

    def edit_book(self, book_number):

        element = self.find_element_by_xpath_wrapper(self.driver, '//form/div/input[@name="%s"]' %
                                                     book_name_input_name)
        element.send_keys(iterator_config.book_name)
        element.submit()


        element = self.driver.find_element_by_xpath(
            '//td[@id="%s" and contains(text(), "%s")]' % (book_number0_id, book_number))
        element = element.find_element_by_xpath('../td/span[text()[normalize-space()]="%s"]' % change_name)
        element.click()

        if yml:
            self.output_string = 'book:\n\tname: \'\'\n'
        else:
            self.output_string = 'Book(\'__name__\',\n\t[\n'


        element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % book_chapters)
        chapters = element.find_elements_by_xpath('table/tbody/tr')
        if yml:
            self.output_string += '\tchapters:\n'
        for chapter in chapters:
            if yml:
                self.output_string += '\t\t- \n'
                self.output_string += '\t\t\tname: '
            else:
                self.output_string += '\tChapter('

            element = self.find_element_by_id_wrapper(chapter, chapter_name_td_id)
            if yml:
                self.output_string += '\'%s\'\n' % element.text
            else:
                self.output_string += '\'%s\',\n' % element.text

            element = chapter.find_element_by_xpath('td/span[text()[normalize-space()]="%s"]' % change_name)
            element.click()
            self.process_chapter()
            if not yml:
                self.output_string += '\t),\n'

        if yml:
            self.output_string += '\n'
        else:
            self.output_string += '\t],\n'

        element = self.find_element_by_xpath_wrapper(self.driver, '//div[b[contains(text(), "%s")]]' % book_parts)
        if yml:
            self.output_string += '\tparts:\n'
            self.fill_parts(element, 2)
            self.output_string += '\n'
        else:
            self.output_string += '\t[\n'
            self.fill_parts(element, 1)
            self.output_string += '\t],\n'

        element = self.find_element_by_xpath_wrapper(self.driver, '//div[b[contains(text(), "%s")]]' % book_pages)
        pages_array = self.get_pages_array_from_current_browser_pages(element)
        if yml:
            self.output_string += '\tpages: '
            self.output_string += '\'' + \
                                  str(min(pages_array)).replace('-', '~') + \
                                  '-' + \
                                  str(max(pages_array)).replace('-', '~') + '\''
            self.output_string += '\n'
        else:
            self.output_string += '\t\'' + \
                                  str(min(pages_array)).replace('-', '~') + \
                                  '-' + \
                                  str(max(pages_array)).replace('-', '~') + '\''
            self.output_string += ')'


def __main__():
    driver = webdriver.Firefox()

    LoginManager(driver).login()

    library_worker = LibraryWorker(driver)

    library_worker.open_library()
    library_worker.edit_book(iterator_config.book_number)

    if yml:
        library_worker.output_string = library_worker.output_string.replace('\t', '  ')
    else:
        library_worker.output_string = library_worker.output_string.replace('\t', '    ')

    with open(output_file_name, 'w') as f:
        if not yml:
            f.write('from collections import namedtuple\n\n')
            f.write('Part = namedtuple("Part", "name pages")\n')
            f.write('Chapter = namedtuple("Chapter", "name parts pages")\n')
            f.write('Book = namedtuple("Book", "name chapters parts pages")\n\n')

        if yml:
            f.write('shift_modifier: \'%d\'\n\n' % -iterator_config.shift)
        else:
            f.write('shift_modifier=%d\n\n' % -iterator_config.shift)

        if yml:
            f.write(library_worker.output_string)
            f.write('\n')
        else:
            f.write('book_structure = ')
            f.write(library_worker.output_string)
            f.write('\n')

        if yml:
            f.write('pages_dictionary:\n')
            for key in sorted(library_worker.pages_dictionary.keys()):
                f.write('  - \n')
                f.write('    page: \'%s\'\n' % str(key))
                f.write('    name: \'%s\'\n' % library_worker.pages_dictionary[key])
        else:
            f.write('pages_dictionary = {\n')
            for key in sorted(library_worker.pages_dictionary.keys()):
                f.write('    ' + str(key) + ': \'' + library_worker.pages_dictionary[key] + '\',\n')
            f.write('}')


if __name__ == '__main__':
    __main__()
