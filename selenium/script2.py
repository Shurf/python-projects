# coding=utf-8
__author__ = 'schrecknetuser'

from selenium import webdriver
from input_data import *
import os
import re

# hardcoded values
library_name = 'Библиотека'.decode('utf-8')
edit_content_name = 'Редактировать содержимое'.decode('utf-8')
edit_name = 'Редактировать'.decode('utf-8')
page_name_class = 'pageName'.decode('utf-8')
object_action_class = 'objectAction'.decode('utf-8')
objects_name = 'Объекты '.decode('utf-8')
book_number0_id = 'book_number0'.decode('utf-8')
change_name = 'Изменить'.decode('utf-8')
select_name = 'Выбрать'.decode('utf-8')
book_chapters = 'Книга. Главы'.decode('utf-8')
book_parts = 'Книга. Части'.decode('utf-8')
book_pages = 'Книга. Страницы'.decode('utf-8')
chapter_parts = 'Глава. Части'.decode('utf-8')
chapter_pages = 'Глава. Страницы'.decode('utf-8')
part_pages = 'Часть. Страницы'.decode('utf-8')
chapter_name = 'Глава'.decode('utf-8')
part_name = 'Часть'.decode('utf-8')
page_name = 'Страница'.decode('utf-8')
add_name = 'Добавить'.decode('utf-8')
add_file_name = 'Добавить файл'.decode('utf-8')
chapter_number_colon = 'Глава. Номер :'.decode('utf-8')
part_number_colon = 'Часть. Номер :'.decode('utf-8')
page_number_colon = 'Страница. Номер :'.decode('utf-8')
book_name_input_name = 'book_name'.decode('utf-8')
chapter_name_input_name = 'chapter_name'.decode('utf-8')
part_name_input_name = 'part_name'.decode('utf-8')
dynamic_databrowser_browse_books = 'dynamic_databrowser3400'.decode('utf-8')
dynamic_databrowser_browse_chapters = 'dynamic_databrowser3600'.decode('utf-8')
dynamic_databrowser_browse_parts = 'dynamic_databrowser3800'.decode('utf-8')
close_name = 'Закрыть'.decode('utf-8')
clone_suffix = '_clone'.decode('utf-8')
pdf_file = 'Файл PDF'.decode('utf-8')
files_name = 'Файлы'.decode('utf-8')
input_files_name = 'files[]'.decode('utf-8')
input_files_type = 'file'.decode('utf-8')
file_container_id = 'file_container'.decode('utf-8')
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
book_number = '1341'


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
        self.files_path = files_path.decode('utf-8')
        pass

    def get_file_path(self, file_num):
        for file_name in os.listdir(self.files_path):
            if not os.path.isfile(os.path.join(self.files_path, file_name)):
                continue
            match = re.search(page_selector.decode('utf-8'), file_name)
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
        pass

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

    def add_page(self, page_num):

        pdf_file_name = file_manager = FileManager(files_path).get_file_path(page_num)
        if pdf_file_name is None:
            return

        # find and click "add page" button
        element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % part_pages)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        # find and click "add page"
        element = self.driver.find_element_by_xpath('//td[h1[text()[normalize-space()] = "%s"]]' % page_name)
        element = element.find_element_by_xpath('span[text()[normalize-space()] = "%s"]' % add_name)
        element.click()

        #find main form for page
        form = self.driver.find_element_by_xpath('//form[div/b[contains(text(), "%s")]]' % page_number_colon)

        #input page number
        element = form.find_element_by_id(page_number_id)
        element.send_keys(page_num)

        #find and click the button that links created part to current book
        element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % book_pages)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        #link book to this page
        self.link_book_to_current_page()

        #find and click the button that links created page to current chapter
        element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % chapter_pages)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        self.link_chapter_to_current_page()

        #find and click the button that links created part to current chapter
        element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % part_pages)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        self.link_part_to_current_page()

        #find and click "pdf file"
        element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % pdf_file)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        #find and click "add file"
        element = self.driver.find_element_by_xpath('//td[h3[text()[normalize-space()] = "%s"]]' % files_name)
        element = element.find_element_by_xpath('span[text()[normalize-space()] = "%s"]' % add_file_name)
        element.click()

        #show plain uploader that we can work with
        self.driver.execute_script(
            "util.hideElements('uploadContainerFS', 'uploadContainerURI'); 	util.showElement('uploadContainerFSOld')")

        #put file name to the hidden input field
        element = self.driver.find_element_by_xpath('//input[@type="%s" and @name="%s"]' % (input_files_type, input_files_name))
        element.send_keys(pdf_file_name)
        element.submit()

        # find_element_by_xpath returns first element, find_elements_by_xpath returns a collection
        # we only need first, so it's ok
        element = self.driver.find_element_by_xpath('//ul[@id="%s"]/li/span' % file_container_id)
        element.click()

    def add_part(self, part, part_num):
        # find and click "add part" button
        element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % chapter_parts)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        #find and click "add button"
        element = self.driver.find_element_by_xpath('//td[h1[text()[normalize-space()] = "%s"]]' % part_name)
        element = element.find_element_by_xpath('span[text()[normalize-space()] = "%s"]' % add_name)
        element.click()

        #find main form for part
        form = self.driver.find_element_by_xpath('//form[div/b[contains(text(), "%s")]]' % part_number_colon)

        #input part number
        element = form.find_element_by_id(part_number_id)
        element.send_keys(part_num)

        #input default page name to make search easier - later this default name is replaced
        element = form.find_element_by_id(part_name_id)
        element.send_keys(default_part_name)

        #find and click the button that links created part to current book
        element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % book_parts)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        #link book to this part
        self.link_book_to_current_part()

        #find and click the button that links created part to current chapter
        element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % chapter_parts)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        self.link_chapter_to_current_part()

        #we have to submit the form and then reopen it because otherwise we won't be able to select it
        form.submit()
        self.find_current_part()
        self.edit_found_part()

        for page_num in range(part.first_page, part.last_page):
            self.add_page(page_num)
            break

            #force apply changes
            #self.driver.execute_script("popupController.reloadLastPopup(false)")
            #
            ##find main form once again
            #form = self.driver.find_element_by_xpath('//form[div/b[contains(text(), "%s")]]' % part_number_colon)
            #
            ##change name to normal
            #element = form.find_element_by_id(part_name_id)
            #element.clear()
            #element.send_keys(part.name.decode('utf-8'))
            #form.submit()
            #
            #self.close_parts_window()

    def add_chapter(self, chapter):
        element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % book_chapters)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        element = self.driver.find_element_by_xpath('//td[h1[text()[normalize-space()] = "%s"]]' % chapter_name)
        element = element.find_element_by_xpath('span[text()[normalize-space()] = "%s"]' % add_name)
        element.click()

        form = self.driver.find_element_by_xpath('//form[div/b[contains(text(), "%s")]]' % chapter_number_colon)
        element = form.find_element_by_id(chapter_number_id)
        element.send_keys(self.get_first_chapter_page_num(chapter))

        element = form.find_element_by_id(chapter_name_id)
        element.send_keys(default_chapter_name)

        element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % book_chapters)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        self.link_book_to_current_chapter()
        # we have to submit the form and then reopen it because otherwise we won't be able to select it
        form.submit()
        self.find_current_chapter()
        self.edit_found_chapter()

        part_num = 1
        for part in chapter.parts:
            self.add_part(part, part_num)
            part_num += 1
            break

            #force apply changes
            #self.driver.execute_script("popupController.reloadLastPopup(false)")
            #
            ##find form again
            #form = self.driver.find_element_by_xpath('//form[div/b[contains(text(), "%s")]]' % chapter_number_colon)
            #
            ##set normal chapter name
            #element = form.find_element_by_id(chapter_name_id)
            #element.clear()
            #element.send_keys(chapter.name.decode('utf-8'))
            #form.submit()


    def edit_book(self, book_number):
        element = self.driver.find_element_by_xpath(
            '//td[@id="%s" and contains(text(), "%s")]' % (book_number0_id, book_number))
        element = element.find_element_by_xpath('../td/span[text()[normalize-space()]="%s"]' % change_name)
        element.click()

        for chapter in structure:
            self.add_chapter(chapter)

            break


def __main__():
    driver = webdriver.Firefox()

    LoginManager(driver).login()

    library_worker = LibraryWorker(driver)

    library_worker.open_library()
    library_worker.edit_book(book_number)


if __name__ == '__main__':
    __main__()
