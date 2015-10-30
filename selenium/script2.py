# coding=utf-8
__author__ = 'schrecknetuser'

import os
import re
from enum import Enum
import time

from selenium import webdriver
from selenium.common.exceptions import *
from bs4 import UnicodeDammit
import pyperclip
from selenium.webdriver.common.keys import Keys

import input_data


# hardcoded values
library_name = 'Библиотека'
edit_content_name = 'Редактировать содержимое'
edit_name = 'Редактировать'
page_name_class = 'pageName'
page_name_id = 'page_name'
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
page_number = 'Страница. Номер'
edit_html_source_name = 'Редактировать HTML-исходник'
textarea_htmlsource_id = 'htmlSource'
html_editor_frame_id = 'mce_'
# save_changes = 'Сохранить изменения'


chapter_number_id = 'chapter_number'
part_number_id = 'part_number'
page_number_id = 'page_number'
chapter_name_id = 'chapter_name'
part_name_id = 'part_name'
page_number_in_list_id = 'page_number'

default_chapter_name = '____current_chapter'
default_part_name = '____current_part'
page_prefix = 'Страница '

# config
password = '7DaJVD8a'
book_config_file_name = 'config.yaml'

# book config
book_number = '1341'


class PageType(Enum):
    book_page = 1
    chapter_page = 2
    part_page = 3

class PartType(Enum):
    book_part = 1
    chapter_part = 2

class StructureWorker:
    def make_pages_array(self, pages_string):

        result = []
        trimmed_string = pages_string.strip()
        if not trimmed_string:
            return result

        blocks = trimmed_string.split(',')
        for block in blocks:
            trimmed_block = block.strip()
            split_block = trimmed_block.split('-')
            if len(split_block) < 2:
                result.append(int(trimmed_block))
            else:
                for i in range(int(split_block[0]), int(split_block[1]) + 1):
                    result.append(i)

        return result

    def find_min_part_page(self, part):
        array = self.make_pages_array(part.pages)
        return min(array)

    def find_min_chapter_page(self, chapter):
        array = self.make_pages_array(chapter.pages)

        for part in chapter.parts:
            array += self.make_pages_array(part.pages)

        return min(array)


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

    def get_file_path(self, file_num, extension):
        for file_name in os.listdir(self.files_path):
            if not os.path.isfile(os.path.join(self.files_path, file_name)):
                continue
            match = re.search(input_data.page_selector + extension, file_name)
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
        return 1  # chapter.parts[0].first_page

    def link_book_to_current_component(self):
        element = self.driver.find_element_by_xpath('//div[@id="%s"]//form/div/input[@name="%s"]' %
                                                    (dynamic_databrowser_browse_books, book_name_input_name))
        element.send_keys(input_data.default_book_name)
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
        self.link_part_to_current_component()

    def link_chapter_to_current_page(self):
        self.link_chapter_to_current_component()

    def add_part(self, part, part_num):
        # find and click "add part" button
        element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % chapter_parts)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        # find and click "add button"
        element = self.driver.find_element_by_xpath('//td[h1[text()[normalize-space()] = "%s"]]' % part_name)
        element = element.find_element_by_xpath('span[text()[normalize-space()] = "%s"]' % add_name)
        element.click()

        # find main form for part
        form = self.driver.find_element_by_xpath('//form[div/b[contains(text(), "%s")]]' % part_number_colon)

        # input part number
        element = form.find_element_by_id(part_number_id)
        element.send_keys(part_num)

        # input default page name to make search easier - later this default name is replaced
        element = form.find_element_by_id(part_name_id)
        element.send_keys(default_part_name)

        # find and click the button that links created part to current book
        element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % book_parts)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        # link book to this part
        self.link_book_to_current_part()

        # find and click the button that links created part to current chapter
        element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % chapter_parts)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        self.link_chapter_to_current_part()

        # we have to submit the form and then reopen it because otherwise we won't be able to select it
        form.submit()
        self.find_current_part()
        self.edit_found_part()

        for page_num in range(part.first_page, part.last_page):
            self.add_page(page_num)
            break

            # force apply changes
            # self.driver.execute_script("popupController.reloadLastPopup(false)")
            #
            # #find main form once again
            # form = self.driver.find_element_by_xpath('//form[div/b[contains(text(), "%s")]]' % part_number_colon)
            #
            # #change name to normal
            # element = form.find_element_by_id(part_name_id)
            # element.clear()
            # element.send_keys(part.name)
            # form.submit()
            #
            # self.close_parts_window()

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

            # force apply changes
            # self.driver.execute_script("popupController.reloadLastPopup(false)")
            #
            # #find form again
            # form = self.driver.find_element_by_xpath('//form[div/b[contains(text(), "%s")]]' % chapter_number_colon)
            #
            # #set normal chapter name
            # element = form.find_element_by_id(chapter_name_id)
            # element.clear()
            # element.send_keys(chapter.name)
            # form.submit()


            # ###################################

    def create_part(self, part_number, part_type):

        # finding "add part button"
        if part_type == PartType.chapter_part:
            element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % chapter_parts)
            element = element.find_element_by_xpath('span[button]')
            element.click()
        elif part_type == PartType.book_part:
            element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % book_parts)
            element = element.find_element_by_xpath('span[button]')
            element.click()
        else:
            raise ValueError('Unknown page type for part %d' % part_number)

        # finding "add" button in the part list screen
        element = self.driver.find_element_by_xpath('//td[h1[text()[normalize-space()] = "%s"]]' % part_name)
        element = element.find_element_by_xpath('span[text()[normalize-space()] = "%s"]' % add_name)
        element.click()

        # finding main form for part
        form = self.driver.find_element_by_xpath('//form[div/b[contains(text(), "%s")]]' % part_number_colon)
        element = form.find_element_by_id(part_number_id)
        element.send_keys(part_number)

        # input part name
        element = form.find_element_by_id(part_name_id)
        element.send_keys(default_part_name)

        if part_type == PartType.chapter_part:
            # linking part to chapter
            element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % chapter_parts)
            element = element.find_element_by_xpath('span[button]')
            element.click()

            self.link_chapter_to_current_part()

        elif part_type == PartType.book_part:
            # linking part to chapter
            element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % book_parts)
            element = element.find_element_by_xpath('span[button]')
            element.click()

            self.link_book_to_current_part()
        else:
            raise ValueError('Unknown page type for part %d' % part_number)

        # we have to submit the form and then reopen it because otherwise we won't be able to select it
        form.submit()

        self.close_parts_window()

        # force update chapter page to display newly created part
        self.driver.execute_script("popupController.reloadLastPopup(false)")

    def add_page(self, page_num, page_type):

        file_manager = FileManager(input_data.files_path)

        pdf_file_name = file_manager.get_file_path(page_num, input_data.pdf_extension)
        if pdf_file_name is None:
            return

        html_file_name = file_manager.get_file_path(page_num, input_data.html_extension)
        if html_file_name is None:
            return

        if page_type == PageType.book_page:
            h1_text = book_pages
        elif page_type == PageType.chapter_page:
            h1_text = chapter_pages
        elif page_type == PageType.part_page:
            h1_text = part_pages
        else:
            raise ValueError('Unknown page type for page %d' % page_num)

        # find and click "add page" button
        element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % h1_text)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        # find and click "add page"
        element = self.driver.find_element_by_xpath('//td[h1[text()[normalize-space()] = "%s"]]' % page_name)
        element = element.find_element_by_xpath('span[text()[normalize-space()] = "%s"]' % add_name)
        element.click()

        # find main form for page
        form = self.driver.find_element_by_xpath('//form[div/b[contains(text(), "%s")]]' % page_number_colon)

        # input page number
        element = form.find_element_by_id(page_number_id)
        element.send_keys(page_num)

        element = form.find_element_by_id(page_name_id)
        element.send_keys(page_prefix + str(page_num))

        if page_type == PageType.book_page:
            # find and click the button that links created part to current book
            element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % book_pages)
            element = element.find_element_by_xpath('span[button]')
            element.click()

            # link book to this page
            self.link_book_to_current_page()
        elif page_type == PageType.chapter_page:
            # find and click the button that links created page to current chapter
            element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % chapter_pages)
            element = element.find_element_by_xpath('span[button]')
            element.click()

            self.link_chapter_to_current_page()
        elif page_type == PageType.part_page:
            # find and click the button that links created part to current part
            element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % part_pages)
            element = element.find_element_by_xpath('span[button]')
            element.click()

            self.link_part_to_current_page()
        else:
            raise ValueError('Unknown page type for page %d' % page_num)

        # find and click "pdf file"
        element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % pdf_file)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        # find and click "add file"
        try:
            element = self.driver.find_element_by_xpath('//td[h3[text()[normalize-space()] = "%s"]]' % files_name)
        except:
            time.sleep(5)
            element = self.driver.find_element_by_xpath('//td[h3[text()[normalize-space()] = "%s"]]' % files_name)
        element = element.find_element_by_xpath('span[text()[normalize-space()] = "%s"]' % add_file_name)
        element.click()

        # show plain uploader that we can work with
        self.driver.execute_script(
            "util.hideElements('uploadContainerFS', 'uploadContainerURI'); 	util.showElement('uploadContainerFSOld')")

        # put file name to the hidden input field
        element = self.driver.find_element_by_xpath(
            '//input[@type="%s" and @name="%s"]' % (input_files_type, input_files_name))
        element.send_keys(pdf_file_name)
        element.submit()

        # find_element_by_xpath returns first element, find_elements_by_xpath returns a collection
        # we only need first, so it's ok
        element = self.driver.find_element_by_xpath('//ul[@id="%s"]/li/span' % file_container_id)
        element.click()

        # now we must add a html source
        element = form.find_element_by_xpath(
            'div/span/table/tbody/tr/td/table/tbody/tr/td/a[@title="%s"]' % edit_html_source_name)
        element.click()

        self.driver.switch_to_frame(self.driver.find_element_by_css_selector('iframe[id*="%s"]' % html_editor_frame_id))

        with open(html_file_name, 'rb') as file:
            html_content = UnicodeDammit(file.read(), is_html=True).unicode_markup
            # element = self.driver.find_element_by_xpath('//form/textarea')
            element = self.driver.find_element_by_xpath('//form/textarea[@name="%s"]' % textarea_htmlsource_id)
            pyperclip.copy(html_content)
            if os.name == 'posix':
                element.send_keys(Keys.COMMAND, 'v')
            else:
                element.send_keys(Keys.CONTROL, 'v')
            # element.send_keys(html_content)
            # self.driver.execute_script('document.getElementById("%s").value = "%s"' % (textarea_htmlsource_id, html.escape(html_content)))
            # self.driver.execute_script('arguments[0].setAttribute("value", "%s")' % html_content, element)
            element.submit()

        self.driver.switch_to_default_content()
        form.submit()

        self.driver.execute_script('popupController.closeLastPopup();')

    def find_pages_table_div(self, text_to_find):
        pages_table_div = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % text_to_find)
        return pages_table_div

    def process_part(self, part):

        pages_array = StructureWorker().make_pages_array(part.pages)

        for page_num in pages_array:
            pages_table_div = self.find_pages_table_div(part_pages)
            try:
                # if a page exists then we've already completed it
                found = False
                elements = pages_table_div.find_elements_by_css_selector('td[id*="%s"]' % page_number_in_list_id)
                for element in elements:
                    if element.text.strip() == str(page_num):
                        found = True
                        break
                if found:
                    continue
            except NoSuchElementException:
                pass

            self.add_page(page_num, PageType.part_page)

            # uncomment for production
            # force update part page to display newly created page
            self.driver.execute_script("popupController.reloadLastPopup(false)")

        # finding main form for part
        form = self.driver.find_element_by_xpath('//form[div/b[contains(text(), "%s")]]' % part_number_colon)
        element = form.find_element_by_id(part_name_id)
        element.clear()
        element.send_keys(part.name)
        form.submit()

    def process_chapter(self, chapter):
        # finding table with already loaded chapters

        for part in chapter.parts:
            parts_table_div = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % chapter_parts)
            try:
                # if such a chapter already exists, it should be completed
                found = False
                # if such a part already exists, it should be completed
                existing_parts = parts_table_div.find_elements_by_xpath(
                    'table/tbody/tr/td[contains(text(), "%s")]' % part.name)
                for existing_part in existing_parts:
                    if existing_part.text.strip() == part.name:
                        found = True
                        break
                if found:
                    continue
            except NoSuchElementException:
                pass

            # we try to find a part with default name: if it is found, we probably crashed while filling it
            try:
                element = parts_table_div.find_element_by_xpath(
                    'table/tbody/tr/td[contains(text(), "%s")]' % default_part_name)
            except NoSuchElementException:
                self.create_part(StructureWorker().find_min_part_page(part), PartType.chapter_part)
                # after updating we should find the div again
                parts_table_div = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % chapter_parts)
                element = parts_table_div.find_element_by_xpath(
                    'table/tbody/tr/td[contains(text(), "%s")]' % default_part_name)

            change_button = element.find_element_by_xpath('../td/span[text()[normalize-space()]="%s"]' % change_name)
            change_button.click()

            self.process_part(part)
            # force update part page to display newly created part
            self.driver.execute_script("popupController.reloadLastPopup(false)")

        pages_array = StructureWorker().make_pages_array(chapter.pages)

        for page_num in pages_array:
            pages_table_div = self.find_pages_table_div(chapter_pages)
            try:
                # if a page exists then we've already completed it
                found = False
                elements = pages_table_div.find_elements_by_css_selector('td[id*="%s"]' % page_number_in_list_id)
                for element in elements:
                    if element.text.strip() == str(page_num):
                        found = True
                        break
                if found:
                    continue
            except NoSuchElementException:
                pass

            self.add_page(page_num, PageType.chapter_page)

            # uncomment for production
            # force update part page to display newly created page
            self.driver.execute_script("popupController.reloadLastPopup(false)")

        # uncomment for production
        # find main form for part
        form = self.driver.find_element_by_xpath('//form[div/b[contains(text(), "%s")]]' % chapter_number_colon)
        element = form.find_element_by_id(chapter_name_id)
        element.clear()
        element.send_keys(chapter.name)
        form.submit()

    def create_chapter(self, chapter):
        element = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % book_chapters)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        element = self.driver.find_element_by_xpath('//td[h1[text()[normalize-space()] = "%s"]]' % chapter_name)
        element = element.find_element_by_xpath('span[text()[normalize-space()] = "%s"]' % add_name)
        element.click()

        form = self.driver.find_element_by_xpath('//form[div/b[contains(text(), "%s")]]' % chapter_number_colon)
        element = form.find_element_by_id(chapter_number_id)
        element.send_keys(StructureWorker().find_min_chapter_page(chapter))

        element = form.find_element_by_id(chapter_name_id)
        element.send_keys(default_chapter_name)

        element = form.find_element_by_xpath('div[b[contains(text(), "%s")]]' % book_chapters)
        element = element.find_element_by_xpath('span[button]')
        element.click()

        self.link_book_to_current_chapter()
        # we have to submit the form and then reopen it because otherwise we won't be able to select it
        form.submit()

        self.close_chapters_window()

        # force update
        self.driver.execute_script("popupController.reloadLastPopup(false)")

    def edit_book(self, book_number):
        element = self.driver.find_element_by_xpath(
            '//td[@id="%s" and contains(text(), "%s")]' % (book_number0_id, book_number))
        element = element.find_element_by_xpath('../td/span[text()[normalize-space()]="%s"]' % change_name)
        element.click()

        for chapter in input_data.book_structure.chapters:
            # finding table with already loaded chapters
            chapters_table_div = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % book_chapters)
            try:
                # if such a chapter already exists, it should be completed
                found = False
                existing_chapters = chapters_table_div.find_elements_by_xpath(
                    'table/tbody/tr/td[contains(text(), "%s")]' % chapter.name)
                for existing_chapter in existing_chapters:
                    if existing_chapter.text.strip() == chapter.name:
                        found = True
                        break
                if found:
                    continue
            except NoSuchElementException:
                pass

            # we try to find a chapter with default name: if it is found, we probably crashed while filling it
            try:
                element = chapters_table_div.find_element_by_xpath(
                    'table/tbody/tr/td[contains(text(), "%s")]' % default_chapter_name)
            except NoSuchElementException:
                self.create_chapter(chapter)
                # after updating we should find the div again
                chapters_table_div = self.driver.find_element_by_xpath(
                    '//div[b[contains(text(), "%s")]]' % book_chapters)
                element = chapters_table_div.find_element_by_xpath(
                    'table/tbody/tr/td[contains(text(), "%s")]' % default_chapter_name)
                # we should now create a chapter with default name
            change_button = element.find_element_by_xpath('../td/span[text()[normalize-space()]="%s"]' % change_name)
            change_button.click()
            self.process_chapter(chapter)

            # force update
            self.driver.execute_script("popupController.reloadLastPopup(false)")

        for part in input_data.book_structure.parts:
            # finding table with already loaded chapters
            parts_table_div = self.driver.find_element_by_xpath('//div[b[contains(text(), "%s")]]' % book_parts)
            try:
                found = False
                # if such a part already exists, it should be completed
                existing_parts = parts_table_div.find_elements_by_xpath(
                    'table/tbody/tr/td[contains(text(), "%s")]' % part.name)
                for existing_part in existing_parts:
                    if existing_part.text.strip() == part.name:
                        found = True
                        break
                if found:
                    continue
            except NoSuchElementException:
                pass

            # we try to find a part with default name: if it is found, we probably crashed while filling it
            try:
                element = parts_table_div.find_element_by_xpath(
                    'table/tbody/tr/td[contains(text(), "%s")]' % default_part_name)
            except NoSuchElementException:
                self.create_part(StructureWorker().find_min_part_page(part), PartType.book_part)
                # after updating we should find the div again
                parts_table_div = self.driver.find_element_by_xpath(
                    '//div[b[contains(text(), "%s")]]' % book_parts)
                element = parts_table_div.find_element_by_xpath(
                    'table/tbody/tr/td[contains(text(), "%s")]' % default_part_name)
                # we should now create a chapter with default name
            change_button = element.find_element_by_xpath('../td/span[text()[normalize-space()]="%s"]' % change_name)
            change_button.click()
            self.process_part(part)

            # force update
            self.driver.execute_script("popupController.reloadLastPopup(false)")

        pages_array = StructureWorker().make_pages_array(input_data.book_structure.pages)

        for page_num in pages_array:
            pages_table_div = self.find_pages_table_div(book_pages)
            try:
                # if a page exists then we've already completed it
                found = False
                elements = pages_table_div.find_elements_by_css_selector('td[id*="%s"]' % page_number_in_list_id)
                for element in elements:
                    if element.text.strip() == str(page_num):
                        found = True
                        break
                if found:
                    continue
            except NoSuchElementException:
                pages_table_div.find_element_by_css_selector('table/tbody/tr/td[id*="%s"]' % page_number_in_list_id)
                pass

            self.add_page(page_num, PageType.book_page)

            # uncomment for production
            # force update part page to display newly created page
            self.driver.execute_script("popupController.reloadLastPopup(false)")


def __main__():
    driver = webdriver.Firefox()

    LoginManager(driver).login()

    library_worker = LibraryWorker(driver)

    library_worker.open_library()
    library_worker.edit_book(book_number)


if __name__ == '__main__':
    __main__()
