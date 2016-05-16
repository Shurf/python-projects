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
page_selector = 'think - (.+)'
pdf_extension = '.pdf'
html_extension = '.html'
#book_number = '1431'
#book_number = '1230'
#book_number = '1220'
book_number = '9001'

#file_name_prefix = "ЛД 'ТД ЕПБ' том 3 "
#file_name_postfix = ".pdf"


#files_path = 'c:\\5\\Архив\\'
files_path = '/users/schrecknetuser/pdf-ocr/think/think.pdf/'

shift_modifier=0

book_structure = Book('__name__',
    [
    Chapter('ON THE YOGA OF FIRE',
        [
        ],
        '9-30'
    ),
    Chapter('MESSENGERS OF LIGHT',
        [
        ],
        '31-249'
    ),
    ],
    [
    ],
    '1-8')
pages_dictionary = {
    10: 'Страница 10. WHAT DOES THE HAPPINESS OF HUMANITY DEPEND ON? HOW CAN YOU BECOME A MEMBER OF THE GREAT WHITE BROTHERHOOD?',
    11: 'Страница 11. OUR GREAT TEACHERS. THE NEW WORLD WILL START FROM CHILDREN FILLED WITH JOY. THE HYMN TO LIGHT SUNG BY THE CHILDREN OF EARTH OWING TO THE HERALD FROM A DISTANT WORLD – THE MESSENGER OF LIGHT.',
    12: 'Страница 12. NO SINGLE LEGEND IS LYING!',
    13: 'Страница 13. WHO TOLD THE LEGEND WE HAVE READ? AND WHO TRANSMITTED IT TO PEOPLE?',
    15: 'Страница 15. THE WORD INSCRIBED IS FIRE, BUT THE MEANIG IS MIND. MAN AND COSMOS.',
    18: 'Страница 18. NO SINGLE LEGEND IS LYING!',
    25: 'Страница 25. THE GIRL’S HEART RECOGNIZED!',
    27: 'Страница 27. SERVANT OF BEAUTY.',
    29: 'Страница 29. “…YOU MAY DRAW YOUR OWN CONCLUSIONS”',
    34: 'Страница 34. THE FLOWER PLANET',
    40: 'Страница 40. CALL OF THE MOUNTAINS.',
    48: 'Страница 48. HE WHO HASTETH',
    56: 'Страница 56. NO LEGEND IS LYING, OR THE MYSTERY OF ASGARTA CAVES',
    65: 'Страница 65. THE PRAYER',
    67: 'Страница 67. ACTION + LOVE = BEAUTY',
    72: 'Страница 72. THE TEACHER WILL NEVER DEMAND: “PAY YOUR RESPECT TO ME”',
    80: 'Страница 80. TEMPTATION',
    85: 'Страница 85. IF YOU HAVE NO ASPIRATION YET',
    90: 'Страница 90. LOW GRADE FOR A DREAM',
    105: 'Страница Страница 105. OVERCOME YOURSELF',
    109: 'Страница 109. THE TRIAL THAT PASSED UNNOTICED',
    119: 'Страница 119. THE GARDENER',
    128: 'Страница 128. AWAKENING OF THE HEART',
    138: 'Страница 138. THE HEART CANNOT BE DECEIVED',
    144: 'Страница 144. THE VOICE OF THE INVISIBLE TEACHER',
    150: 'Страница 150. ENLIGHTENMENT',
    158: 'Страница 158. A LUMP OF MUD HURLED AT THE TEACHER',
    162: 'Страница 162. TWO ENCOUNTERS WITH THE TEACHER',
    167: 'Страница 167. PROTECT!',
    176: 'Страница 176. UNPREPARED',
    184: 'Страница 184. BITS OF LOVE',
    187: 'Страница 187. DOESN\'T MATTER',
    195: 'Страница 195. NO CITY WILL STAND WITHOUT A SAINT',
    206: 'Страница 206. Part I. COMPASSION Part II. IT WAS DAY, IT WAS NIGHT…',
    215: 'Страница 215. IN SEARCH OF THE TEACHER',
    222: 'Страница 222. HE WHO HASTETH…',
    229: 'Страница 229. WHEN MIND IS DULL AND EYES ARE DIM A SONG TO HELP',
    235: 'Страница 235. A FEAT OF SELFLESS DEVOTION',
}