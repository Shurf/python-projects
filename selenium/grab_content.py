# coding=utf-8
__author__ = 'schrecknetuser'

from selenium import webdriver
import input_data_grab
import os
import re
import time

import pyperclip
from selenium.webdriver.common.keys import Keys

# hardcoded values

edit_html_source_name = 'Редактировать HTML-исходник'
textarea_htmlsource_id = 'htmlSource'
html_editor_frame_id = 'mce_'

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
# save_changes = 'Сохранить изменения'


chapter_number_id = 'chapter_number'
part_number_id = 'part_number'
page_number_id = 'page_number'
chapter_name_id = 'chapter_name'
part_name_id = 'part_name'

default_chapter_name = '____current_chapter'
default_part_name = '____current_part'

# config
password = '7DaJVD8a'
book_config_file_name = 'config.yaml'

# book config
#book_number = '1341'


class LoginManager:
    def __init__(self, driver):
        self.driver = driver
        pass

    def login(self):
        self.driver.get('http://secretdoctrine.ru/my/s3/login/')
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_name('enter').click()


class FileManager:
    def __init__(self, files_path):
        self.files_path = files_path
        pass

    def get_file_path(self, file_num):
        for file_name in os.listdir(self.files_path):
            if not os.path.isfile(os.path.join(self.files_path, file_name)):
                continue
            match = re.search(page_selector, file_name)
            if not match:
                continue
            if len(match.groups()) < 1:
                continue
            try:
                match_file_num = int(match.group(1))
                if match_file_num == file_num:
                    return os.path.join(self.files_path, file_name)
            except:
                continue
        return None

class LibraryWorker:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 3
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

    def get_first_chapter_page_num(self, chapter):
        return chapter.parts[0].first_page

    def link_book_to_current_component(self):
        element = self.driver.find_element_by_xpath('//div[@id="%s"]//form/div/input[@name="%s"]' %
                                                    (dynamic_databrowser_browse_books, book_name_input_name))
        element.send_keys(default_book_name)
        element.submit()

        # find it again because page has been reloaded
        input = self.driver.find_element_by_xpath('//div[@id="%s"]//form/div/input[@name="%s"]' %
                                                  (dynamic_databrowser_browse_books, book_name_input_name))
        element = input.find_element_by_xpath('../../../table/tbody/tr/td/span[text()[normalize-space()]="%s"]' %
                                              select_name)
        element.click()

        element = input.find_element_by_xpath('../../../input[@value = "%s"]' % close_name)
        element.click()

    def make_chapter_div_id(self, is_clone):
        div_id = dynamic_databrowser_browse_chapters
        if is_clone:
            div_id += clone_suffix
        return div_id

    def find_current_chapter(self, is_clone=False):
        element = self.driver.find_element_by_xpath('//div[@id="%s"]//form/div/input[@name="%s"]' %
                                                    (self.make_chapter_div_id(is_clone), chapter_name_input_name))
        element.send_keys(default_chapter_name)
        element.submit()

    def edit_found_chapter(self, is_clone=False):
        element = self.driver.find_element_by_xpath('//div[@id="%s"]//form/div/input[@name="%s"]' %
                                                    (self.make_chapter_div_id(is_clone), chapter_name_input_name))
        element = element.find_element_by_xpath('../../../table/tbody/tr/td/span[text()[normalize-space()]="%s"]' %
                                                change_name)
        element.click()

    def select_found_chapter(self, is_clone=False):
        element = self.driver.find_element_by_xpath('//div[@id="%s"]//form/div/input[@name="%s"]' %
                                                    (self.make_chapter_div_id(is_clone), chapter_name_input_name))
        element = element.find_element_by_xpath('../../../table/tbody/tr/td/span[text()[normalize-space()]="%s"]' %
                                                select_name)
        element.click()

    def close_chapters_window(self, is_clone=False):
        element = self.driver.find_element_by_xpath('//div[@id="%s"]//form/div/input[@name="%s"]' %
                                                    (self.make_chapter_div_id(is_clone), chapter_name_input_name))
        element = element.find_element_by_xpath('../../../input[@value = "%s"]' % close_name)
        element.click()

    def make_part_div_id(self, is_clone):
        div_id = dynamic_databrowser_browse_parts
        if is_clone:
            div_id += clone_suffix
        return div_id

    def find_current_part(self, is_clone=False):
        element = self.driver.find_element_by_xpath('//div[@id="%s"]//form/div/input[@name="%s"]' %
                                                    (self.make_part_div_id(is_clone), part_name_input_name))
        element.send_keys(default_part_name)
        element.submit()

    def edit_found_part(self, is_clone=False):
        input = self.driver.find_element_by_xpath('//div[@id="%s"]//form/div/input[@name="%s"]' %
                                                  (self.make_part_div_id(is_clone), part_name_input_name))
        element = input.find_element_by_xpath('../../../table/tbody/tr/td/span[text()[normalize-space()]="%s"]' %
                                              change_name)
        element.click()

    def select_found_part(self, is_clone=False):
        input = self.driver.find_element_by_xpath('//div[@id="%s"]//form/div/input[@name="%s"]' %
                                                  (self.make_part_div_id(is_clone), part_name_input_name))
        element = input.find_element_by_xpath('../../../table/tbody/tr/td/span[text()[normalize-space()]="%s"]' %
                                              select_name)
        element.click()

    def close_parts_window(self, is_clone=False):
        input = self.driver.find_element_by_xpath('//div[@id="%s"]//form/div/input[@name="%s"]' %
                                                  (self.make_part_div_id(is_clone), part_name_input_name))
        element = input.find_element_by_xpath('../../../input[@value = "%s"]' % close_name)
        element.click()

    def link_chapter_to_current_component(self, is_clone=False):
        self.find_current_chapter(is_clone)

        # find it again because page has been reloaded
        self.select_found_chapter(is_clone)

        self.close_chapters_window(is_clone)

    def link_part_to_current_component(self, is_clone=False):
        self.find_current_part(is_clone)

        # find it again because page has been reloaded
        self.select_found_part(is_clone)

        self.close_parts_window(is_clone)

    def link_book_to_current_chapter(self):
        self.link_book_to_current_component()

    def link_chapter_to_current_part(self):
        self.link_chapter_to_current_component()

    def link_book_to_current_part(self):
        self.link_book_to_current_component()

    def link_book_to_current_page(self):
        self.link_book_to_current_component()

    def link_part_to_current_page(self):
        self.link_part_to_current_component(True)

    def link_chapter_to_current_page(self):
        self.link_chapter_to_current_component(True)


    def process_page(self):

        #find main form for page
        form = self.driver.find_element_by_xpath('//form[div/b[contains(text(), "%s")]]' % page_number_colon)

        #input page number
        element = form.find_element_by_id(page_number_id)

        page_num = int(element.get_attribute('value'))

        element = self.find_element_by_xpath_wrapper(form,
                                                     'div/span/table/tbody/tr/td/table/tbody/tr/td/a[@title="%s"]' % edit_html_source_name)
        element.click()

        self.driver.switch_to_frame(
            self.find_element_by_css_selector_wrapper(self.driver, 'iframe[id*="%s"]' % html_editor_frame_id))

        html_file_name = os.path.join(
            input_data_grab.book_path,
            input_data_grab.html_prefix + str(page_num).zfill(4) + input_data_grab.html_postfix)
        with open(html_file_name, 'w') as file:
            # element = self.driver.find_element_by_xpath('//form/textarea')
            element = self.find_element_by_xpath_wrapper(self.driver,
                                                         '//form/textarea[@name="%s"]' % textarea_htmlsource_id)

            if os.name == 'posix':
                element.send_keys(Keys.COMMAND, 'a')
                element.send_keys(Keys.COMMAND, 'c')
            else:
                element.send_keys(Keys.CONTROL, 'a')
                element.send_keys(Keys.CONTROL, 'c')
            file.write('<html><body>\n' + pyperclip.paste() + '\n</body></html>')

            #self.driver.execute_script('tinyMCEPopup.close();')
            #print('!')
            element = self.find_element_by_xpath_wrapper(self.driver,
                                                         '//form/div/div/input[@name="%s"]' % "cancel")
            element.click()

        self.driver.switch_to_default_content()

        self.driver.execute_script('popupController.closeLastPopup();')

    def process_part(self):
        element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % part_pages)
        pages = element.find_elements_by_xpath('table/tbody/tr')
        for page in pages:
            element = page.find_element_by_xpath('td/span[text()[normalize-space()]="%s"]' % change_name)
            element.click()
            self.process_page()

        self.driver.execute_script('popupController.closeLastPopup()')

    def process_chapter(self):

        element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % chapter_parts)
        parts = element.find_elements_by_xpath('table/tbody/tr')
        for part in parts:
            element = part.find_element_by_xpath('td/span[text()[normalize-space()]="%s"]' % change_name)
            element.click()
            self.process_part()

        element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % chapter_pages)
        pages = element.find_elements_by_xpath('table/tbody/tr')
        for page in pages:
            element = page.find_element_by_xpath('td/span[text()[normalize-space()]="%s"]' % change_name)
            element.click()
            self.process_page()

        self.driver.execute_script('popupController.closeLastPopup()')


    def find_element_by_xpath_wrapper(self, parent, xpath):
        try:
            return parent.find_element_by_xpath(xpath)
        except:
            time.sleep(self.timeout)
            return parent.find_element_by_xpath(xpath)

    def edit_book(self, book_number):
        element = self.find_element_by_xpath_wrapper(self.driver, '//form/div/input[@name="%s"]' %
                                                     book_name_input_name)
        element.send_keys(input_data_grab.book_name)
        element.submit()

        element = self.find_element_by_xpath_wrapper(self.driver,
                                                     '//td[@id="%s" and contains(text(), "%s")]' % (
                                                         book_number0_id, book_number))
        element = self.find_element_by_xpath_wrapper(element,
                                                     '../td/span[text()[normalize-space()]="%s"]' % change_name)
        element.click()

        element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % book_chapters)
        chapters = element.find_elements_by_xpath('table/tbody/tr')
        for chapter in chapters:
            element = chapter.find_element_by_xpath('td/span[text()[normalize-space()]="%s"]' % change_name)
            element.click()
            self.process_chapter()

        element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % book_pages)
        pages = element.find_elements_by_xpath('table/tbody/tr')
        for page in pages:
            element = page.find_element_by_xpath('td/span[text()[normalize-space()]="%s"]' % change_name)
            element.click()
            self.process_page()


def __main__():
    driver = webdriver.Firefox()

    LoginManager(driver).login()

    library_worker = LibraryWorker(driver)

    library_worker.open_library()
    library_worker.edit_book(input_data_grab.book_number)


if __name__ == '__main__':
    __main__()
