# coding=utf-8

from collections import namedtuple

#default_book_name = "____current_book"
default_book_name = "Тест"
#default_book_name = "I. Космогенезис (космическая эволюция)"
Part = namedtuple("Part", "name pages")
Chapter = namedtuple("Chapter", "name parts pages")
Book = namedtuple("Book", "name chapters parts pages")

page_selector = "ЛД 'ТД ЕПБ' том 1 (.+)"
pdf_extension = '.pdf'
html_extension = '.html'
#book_number = '1431'
#book_number = '1230'
#book_number = '1220'

file_name_prefix = "ЛД 'ТД ЕПБ' том 3 "
file_name_postfix = ".pdf"


#files_path = 'c:\\5\\Архив\\'
files_path = '/users/schrecknetuser/1'

book_structure = Book("Название книги",
                      [Chapter('Глава 1',
                               [Part('Раздел 1',
                                     '2'),
                                Part('Раздел 2',
                                     '5')],
                               '4, 6-7'),
                       Chapter('Внезапная вторая глава',
                               [Part('Раздел 1',
                                     '8')],
                               '9')],
                      [Part('Раздел 1',
                            '10')],
                      '1, 3')

