# coding=utf-8

from collections import namedtuple

default_book_name = "____current_book"
#default_book_name = "Тест"
#default_book_name = "I. Космогенезис (космическая эволюция)"
Part = namedtuple("Part", "name pages num")
Part.__new__.__defaults__ = (None, None, None)
Chapter = namedtuple("Chapter", "name parts pages")
Book = namedtuple("Book", "name chapters parts pages")

#page_selector = "ЛД 'ТД ЕПБ' том 1 (.+)"
page_selector = 'letters - (.+)'
pdf_extension = '.pdf'
html_extension = '.html'
#book_number = '1431'
#book_number = '1230'
#book_number = '1220'
book_number = '9005'

#file_name_prefix = "ЛД 'ТД ЕПБ' том 3 "
#file_name_postfix = ".pdf"


#files_path = 'c:\\5\\Архив\\'
files_path = '/users/schrecknetuser/pdf-ocr/letters/letters.pdf'

shift_modifier=0

book_structure = Book('__name__',
    [
    Chapter('Том I',
        [
        Part('I. От Е.П.Б. к Г.С.0',
            '13-19'),
        Part('II. К Г.С.О. от «Луксорского Братства»',
            '20-23'),
        Part('III. «Важное примечание»',
            '24-26'),
        Part('IV. «Куча хороших новостей»',
            '27-30'),
        Part('V. «Что важно знать спиритуалистам»',
            '31-39'),
        Part('VI. Из альбома, 27 мая 1875 год',
            '40-42'),
        Part('VII. Из альбома, Е.П.Б. и масонское братство',
            '43-54'),
        Part('VIII. Е.П.Б. к Г.С.О. 21 мая 1871 год',
            '55-65'),
        Part('IX. «Героические женщины»',
            '66-72'),
        Part('X. Е.П.Б. генералу Липпитту',
            '73-91'),
        Part('XI. Е.П.Б. и Г.С.О. генералу Липпитту',
            '92-114'),
        Part('XII. М.Ч.Б. (Батанелли) генералу Липпитту',
            '115-119'),
        Part('XIII. Е.П.Б. генералу Липпитту',
            '120-125'),
        Part('XIV. Е.П.Б. к «Пробужденной»',
            '126-135'),
        Part('XV. Отрывки из Дневника',
            '136-159'),
        Part('XVI. Отрывки из Дневника',
            '160-190'),
        Part('XVII. Е.П.Б. к мадемуазель Н.А.Фадеевой',
            '191-213'),
        Part('XVIII. Е.П.Б. к мадемуазель Н.А.Фадеевой',
            '214-257'),
        Part('XIX. Е.П.Б. генералу Липпитту 1880 год',
            '258-272'),
        ],
        '11-12'
    ),
    Chapter('Том II',
        [
        Part('Введение',
            '275-284'),
        Part('Письмо Е.П.Б. капитану А. де Бурбону',
            '285-292'),
        Part('Письма Е.П.Б. князю A.M. Дондукову- Корсакову',
            '293-422'),
        Part('Клевета в печати на Е.П.Б',
            '423-427'),
        Part('Петиция Е.П.Б. князю A.M. Дондукову- Корсакову',
            '428-430'),
        Part('Письмо от мадемуазель Глинки князю A.M. Дондукову-Корсакову',
            '431-433'),
        Part('Письма Блаватской генералу Ф.Дж. Липпиту',
            '434-456'),

        ],
        '273-274'
    ),
    ],
    [
    ],
    '1-10')
pages_dictionary = {
    7: 'Страница 7. Предисловие',
 }