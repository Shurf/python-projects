# coding=utf-8

from collections import namedtuple

#default_book_name = "____current_book"
default_book_name = "Тест".decode('utf-8')
#default_book_name = "I. Космогенезис (космическая эволюция)".decode('utf-8')
Part = namedtuple("parts", "name first_page last_page")
Chapter = namedtuple("Chapter", "name parts")

page_selector = "ЛД 'ТД ЕПБ' том 1 (.+).pdf"
#book_number = '1431'
book_number = '1230'
#book_number = '1220'

file_name_prefix = "ЛД 'ТД ЕПБ' том 3 ".decode('utf-8')
file_name_postfix = ".pdf".decode('utf-8')


#files_path = 'c:\\5\\Архив\\'
files_path = '/users/schrecknetuser/1/doctrine3'

structure = [
             Chapter("Глава 1. Великое знание",
                     [Part("Часть 1.", 1, 3),
                      Part("Часть 2.", 4, 6),
                      Part("Часть 3.", 7, 200)]),

             Chapter("Глава 2. Скрытый смысл",
             [Part("Часть 1", 4, 6)])

             ]
