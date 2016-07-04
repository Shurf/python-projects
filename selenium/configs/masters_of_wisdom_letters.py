# coding=utf-8

from collections import namedtuple

default_book_name = "____current_book"
# default_book_name = "Тест"
# default_book_name = "I. Космогенезис (космическая эволюция)"
Part = namedtuple("Part", "name pages num")
Part.__new__.__defaults__ = (None, None, None)
Chapter = namedtuple("Chapter", "name parts pages")
Book = namedtuple("Book", "name chapters parts pages")


#file_name_prefix = "ЛД 'ТД ЕПБ' том 3 "
#file_name_postfix = ".pdf"


#files_path = 'c:\\5\\Архив\\'
files_path = '/users/schrecknetuser/pdf-ocr/masters_of_wisdom_letters/'

shift_modifier=0

page_selector = '(.+)'
pdf_extension = '.pdf'
html_extension = '.html'
# book_number = '1431',
# book_number = '1230',
# book_number = '1220',
book_number = '9008'

book_structure = Book('__name__',
                      [],
                      [],
                      '1-150')


pages_dictionary = {
	1: 'ПИСЬМА МАСТЕРОВ МУДРОСТИ',
    #2: 'Составитель и автор примечаний . С. Джинараджадаса',
	3: 'ПРЕДИСЛОВИЕ',
	4: 'I. ТЕОСОФСКОЕ ОБЩЕСТВО',
	5: 'Теософское Общество и его деятельность. Письмо 1',
	6: 'Теософское Общество и его деятельность. Письмо 2',
	7: 'Теософское Общество и его деятельность. Письмо 3',
	8: 'Теософское общество и его деятельность. Письмо 4',
	9: 'Теософское общество и его деятельность. Письмо 5',
	10: 'II. ПУТЬ УЧЕНИЧЕСТВА',
	11: 'Путь ученичества. Письмо 6',
    #12: 'Путь ученичества. * * *',
	13: 'Путь ученичества. Письмо 7',
	14: 'Путь ученичества. Письмо 8',
	15: 'Путь ученичества. Письмо 9',
	16: 'Путь ученичества. Письмо 10',
	17: 'Путь ученичества. Письмо 11',
	18: 'III. ИНДИЯ',
	19: 'Индия и теософское движение. Письмо 12',
	20: 'Индия и теософское движение. Письмо 13',
	21: 'Индия и теософское движение. Письмо 14',
	22: 'Индия и теософское движение. Письмо 15',
	23: 'IV. ПИСЬМА ЛИЧНОГО ХАРАКТЕРА',
	24: 'Письма личного характера. Письмо 16',
	25: 'Письма личного характера. Письмо 17',
	26: 'Письма личного характера. Письмо 18',
	27: 'Письма личного характера. Письмо 19',
	28: 'Письма личного характера. Письмо 20',
	29: 'Письма личного характера. Письмо 21',
	30: 'Письма личного характера. Письмо 22',
	31: 'Письма личного характера. Письмо 23',
	32: 'Письма личного характера. Письмо 24',
	33: 'Письма личного характера. Письмо 25',
	34: 'V. О Д. К. МАВАЛАНКАРЕ',
	35: 'О Д. К. Маваланкаре. Письмо 26',
	36: 'О Д. К. Маваланкаре. Письмо 27',
	37: 'О Д. К. Маваланкаре. Письмо 28',
	38: 'О Д. К. Маваланкаре. Письмо 29',
	39: 'VI. ПИСЬМА ОБЩЕГО СОДЕРЖАНИЯ',
	40: 'Письма общего содержания. Письмо 30',
	41: 'Письма общего содержания. Письмо 31',
	42: 'Письма общего содержания. ***',
	43: 'Письма общего содержания. Письмо 32',
	44: 'Письма общего содержания. Письмо 33',
	45: 'VII. ЗАМЕЧАНИЯ НА ПОЛЯХ ПИСЕМ',
	46: 'Замечания на полях писем. Письмо 34',
	47: 'Замечания на полях писем. Письмо 35',
	48: 'Замечания на полях писем. Письмо 36',
	49: 'Замечания на полях писем. Письмо 37',
	50: 'VIII. ПИСЬМА В АМЕРИКУ',
	51: 'Письма в Америку',
	52: 'Письмо 38',
	53: 'Доб. К  письму 38',
	54: 'Письма в Америку. Письмо 39',
	55: 'Письма в Америку. Письмо 40',
	56: 'Письма в Америку. Письмо 41',
	57: 'Письма в Америку. Письмо 42',
	58: 'Письма в Америку. Письмо 43',
    #59: 'Письма в Америку. * * *',
	60: 'Письма в Америку. Письмо 44',
	61: 'Письма в Америку. Письмо 45',
	62: 'Письма в Америку. Письмо 46',
	63: 'Письма в Америку. Письмо 47',
	64: 'Письма в Америку. Письмо 48',
	65: 'Письма в Америку. Письмо 49',
	66: 'Письма в Америку. Письмо 50',
	67: 'Письма в Америке. Письмо 51',
	68: 'Письма в Америке. Письмо 52',
	69: 'Письма в Америку. Письмо 53',
	70: 'Письма в Америку. Письмо 54',
	71: 'Письма в Америку. ВЫДЕРЖКИ ИЗ ПИСЕМ',
	72: 'Письма в Америку. Письмо 55',
	73: 'Письма в Америку. Письмо 56',
	74: 'Письма в Америку. Письмо 57',
	75: 'Письма в Америку. Письмо 58',
	76: 'Письма в Америку. Письмо 59',
	77: 'Письма в Америку. Письмо 60',
	78: 'IX. ПИСЬМА Г. С. ОЛЬКОТТУ',
    #79: '*  *  *. Прежде чем приступить к чтению писем 61-82, адресованных Учителями полковнику Олькотту, хорошо было бы не обманываться насчет их характера: некоторые из них являются просто выговорами, а это могло бы вызвать нежелательное предположение о том, что он был неспособным человеком. Как раз все наоборот. Именно потому, что его Учитель очень доверял ему, я привожу здесь в первую очередь письмо 61. Учителя не имели лучшего сотрудника, он был беззаветно предан Им и Их делу.',
	80: 'Письма Г. С. Олькотту. Письмо 61',
	81: 'Письма Г. С. Олькотту. Письмо 62',
    #82: 'Письма Г. С. Олькотту. *  *  *',
	83: 'Письма Г. С. Олькотту. Письмо 63',
	84: 'Письма Г. С. Олькотту. Письмо 64',
	85: 'Письма Г. С. Олькотту. Письмо 65',
	86: 'Письма Г. С. Олькотта. Письмо 66',
	87: 'Письма Г. С. Олькотту. Письмо 67',
	88: 'Письмо Г. С. Олькотту. Письмо 68',
	89: 'Письма Г. С. Олькотту. Письмо 69',
	90: 'Письма Г. С. Олькотту. Письмо 70',
	91: 'Письма Г. С. Олькотту. Письмо 71',
	92: 'Письма к Г. С. Олькотту. Письмо 72',
	93: 'Письма Г. С. Олькотту. Письмо 73',
	94: 'Письма Г. С. Олькоту. Письмо 74',
	95: 'Письма Г. С. Олькотту. Письмо 75',
	96: 'Письма Г. С. Олькотту. Письмо 76',
	97: 'Письма Г. С. Олькотту. Письмо 77',
	98: 'Письма Г. С. Олькотту. Письмо 78',
	99: 'Письма Г. С. Олькотту. Письмо 79',
	100: 'Письма Г. С. Олькотту. Письмо 80',
	101: 'Письма Г. С. Олькотту. Письмо 81',
	102: 'Письма Г. С. Олькотту. Письмо 82',
	103: 'X. ПИСЬМА ИНДИЙСКИМ ЧЕЛА',
    #104: '***. Письма 83-91 получены весьма преданным теософом, покойным С. Рамасвамиром из Тинневелли. Он получил первое письмо от Учителя М[ории] 28 сентября 1881 г. В следующем году он отправился в Сикким и 6 октября встретился там с глазу на глаз со своим Учителем. Его рассказ об этой встрече приводится в Приложении 1.',
	105: 'Письма индийским чела. Письмо 83',
	106: 'Письма индийских чела. Письмо 84',
	107: 'Письма индийским чела. Письмо 85',
	108: 'Письма индийским чела. Письмо 86',
	109: 'Письма индийским чела. Письмо 87',
	110: 'Письма индийским чела. Письмо 88',
	111: 'Письма индийским чела. Письмо 89',
	112: 'Письма индийским чела. Письмо 90',
	113: 'Письма индийским чела. Письмо 91',
    #114: '* * *. Одним из группы выдающихся индийцев, которые трудились с целью продвинуть теософские идеи на Запад, является Мохини Мохан Чаттерджи. Когда в 1882 г. он был привлечен к теософии, то обнаружилось, что он одарен необычайно проницательным философским умом. Учитель К[ут] Х[уми] принял его в ученики, и он подавал большие надежды. Однако к 1886 г. после нескольких лет блестящего служения он разошелся во взглядах с Е. П. Блаватской и мало-помалу потерял интерес к Теософскому Обществу.',
	115: 'Письма индийским чела. Письмо 92',
	116: 'Письма индийским чела. Письмо 93',
	117: 'Письма индийским чела. Письмо 94',
	118: 'Письма индийским чела. Письмо 95',
	119: 'Письма индийским чела. Письмо 96',
	120: 'Письма индийским чела. Письмо 97',
	121: 'Письма индийским чела. Письмо 98',
    #122: '* * *. Письма 99-102 получены м-ром Р. Кешава Пиллаи, инспектором полиции, обретавшемся тогда в Неллоре, округ Мадрас. Основатели в мае 1882 г. посетили Неллору, и там 8-го числа был создан филиал Общества во главе с секретарем м-ром Кешава Пиллаи, а президентом стал состоятельный индус, помощник коллектора. Посетив другие города, 24-го числа Основатели вернулись в Неллору. Тем временем английский коллектор, местный представитель британского правительства, оказав давление на президента, заставил его отказаться от президентства — на этот случай ссылается К[ут] Х[уми] в письме 99. М-р Кешава был взят Учителем на испытание, но ничуть не продвинулся вперед. Позднее он потерял интерес к Т[еософскому] О[бществу], и его жизнь принесла ему чрезвычайно много разочарований в этом мире. За несколько лет до смерти он отдал полковнику Олькотту письма, которые получил, и я переписал их с подлинников, хранящихся в Адьяре.',
	123: 'Письма индийским чела. Письмо 99',
	124: 'Письма индийским чела. Письмо 100',
	125: 'Письма индийским чела. Письмо 101',
	126: 'Письма индийским чела. Письмо 102',
	127: 'XI. ПИСЬМА НЕМЕЦКИМ ТЕОСОФАМ',
	128: 'Письма немецким теософам. Письмо 103',
	129: 'Письма немецким теософам. Письмо 104',
	130: 'Письма немецким теософам. Письмо 105',
	131: 'Письма немецким теософам. Письмо 106',
	132: 'Письма немецким теософам. Письмо 107',
	133: 'Письма немецким теософам. Письмо 108',
	134: 'XII. РАЗНЫЕ ПИСЬМА',
	135: 'Разные письма. Письмо 109',
	136: 'Разные письма. Письмо 110',
	137: 'Разные письма. Письмо 111',
	138: 'Разные письма. Письмо 112',
	139: 'Разные письма. Письмо 113',
	140: 'Разные письма. Письмо 114',
	141: 'Разные письма. Письмо 115',
	142: 'Разные письма. Письмо 116',
	143: 'Разные письма. Письмо 117',
	144: 'Разные письма. Письмо 118',
	145: 'Разные письма. Письмо 119',
	146: 'Разные письма. Письмо 120',
	147: 'Приложение 1. КАК ЧЕЛА НАШЕЛ СВОЕГО ГУРУ',
	148: 'Приложение 2. ГИМАЛАЙСКИЕ БРАТЬЯ — СУЩЕСТВУЮТ ЛИ ОНИ?',
	149: 'Приложение 3. ВСТРЕЧА С МОИМ УЧИТЕЛЕМ',
	150: 'Из дневника Г.С.Олькотта. (1883 г.)',
}
