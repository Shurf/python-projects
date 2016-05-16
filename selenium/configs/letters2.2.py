# coding=utf-8

from collections import namedtuple

default_book_name = "____current_book"
# default_book_name = "Тест"
# default_book_name = "I. Космогенезис (космическая эволюция)"
Part = namedtuple("Part", "name pages num")
Part.__new__.__defaults__ = (None, None, None)
Chapter = namedtuple("Chapter", "name parts pages")
Book = namedtuple("Book", "name chapters parts pages")

# page_selector = "ЛД 'ТД ЕПБ' том 1 (.+)"
page_selector = '(.+)'
pdf_extension = '.pdf'
html_extension = '.html'
# book_number = '1431',
# book_number = '1230',
# book_number = '1220',
book_number = '9009'

# file_name_prefix = "ЛД 'ТД ЕПБ' том 3 "
# file_name_postfix = ".pdf"


# files_path = 'c:\\5\\Архив\\'
files_path = '/users/schrecknetuser/pdf-ocr/letters2.2'

shift_modifier = 0

book_structure = Book('__name__',
                      [],
                      [],
                      '1-342')
pages_dictionary = {
	1: '12 апреля 1933, среда, «Урусвати»',
	2: '13 апреля 1933, четверг',
	3: '14 апреля 1933, пятница',
	4: '15 апреля 1933, суббота',
	5: '16 апреля 1933, воскресенье, Пасха',
	6: '17 апреля 1933, понедельник',
	7: '18 апреля 1933, вторник',
	8: '19 апреля 1933, среда',
	9: '20 апреля 1933, четверг',
	10: '21 апреля 1933, пятница',
	11: '22 апреля 1933, суббота',
	12: '23 апреля 1933, воскресенье',
	13: '24 апреля 1933, понедельник',
	14: '25 апреля 1933, вторник',
	15: '26 апреля 1933, среда',
	16: '27 апреля 1933, четверг',
	17: '28 апреля 1933, пятница',
	18: '29 апреля 1933, суббота',
	19: '30 апреля 1933, воскресенье',
	20: '1 мая 1933, понедельник',
	21: '2 мая 1933, вторник',
	22: '3 мая 1933, среда',
	23: '4 мая 1933, четверг',
	24: '5 мая 1933, пятница',
	25: '6 мая 1933, суббота',
	26: '7 мая 1933, воскресенье',
	27: '8 мая 1933, понедельник',
	28: '9 мая 1933, вторник',
	29: '10 мая 1933, среда',
	30: '11 мая 1933, четверг, «Урусвати»',
	31: '12 мая 1933, пятница',
	32: '13 мая 1933, суббота',
	33: '14 мая 1933, воскресенье',
	34: '15 мая 1933, понедельник',
	35: '16 мая 1933, вторник',
	36: '17 мая 1933, среда',
	37: '18 мая 1933, четверг',
	38: '19 мая 1933, пятница',
	39: '20 мая 1933, суббота',
	40: '21 мая 1933, воскресенье',
	41: '22 мая 1933, понедельник',
	42: '23 мая 1933, вторник',
	43: '24 мая 1933, среда',
	44: '25 мая 1933, четверг',
	45: '26 мая 1933, пятница',
	46: '27 мая 1933, суббота',
	47: '28 мая 1933, воскресенье',
	48: '29 мая 1933, понедельник',
	49: '30 мая 1933, вторник',
	50: '31 мая 1933, среда',
	51: '1 июня 1933, четверг',
	52: '2 июня 1933, пятница',
	53: '3 июня 1933, суббота',
	54: '4 июня 1933, воскресенье',
	55: '5 июня 1933, понедельник',
	56: '6 июня 1933, вторник',
	57: '7 июня 1933, среда',
	58: '8 июня 1933, четверг',
	59: '9 июня 1933, пятница',
	60: '10 июня 1933, суббота',
	61: '11 июня 1933, воскресенье',
	62: '12 июня 1933, понедельник',
	63: '13 июня 1933, вторник',
	64: '14 июня 1933, среда',
	65: '15 июня 1933, четверг',
	66: '16 июня 1933, пятница',
	67: '17 июня 1933, суббота',
	68: '18 июня 1933, воскресенье',
	69: '19 июня 1933, понедельник',
	70: '20 июня 1933, вторник',
	71: '21 июня 1933, среда',
	72: '22 июня 1933, четверг',
	73: '23 июня 1933, пятница',
	74: '24 июня 1933, суббота',
	75: '25 июня 1933, воскресенье',
	76: '26 июня 1933, понедельник',
	77: '27 июня 1933, вторник',
	78: '28 июня 1933, среда',
	79: '29 июня 1933, четверг',
	80: '30 июня 1933, пятница',
	81: '1 июля 1933, суббота',
	82: '2 июля 1933, воскресенье',
	83: '3 июля 1933, понедельник',
	84: '4 июля 1933, вторник',
	85: '5 июля 1933, среда',
	86: '6 июля 1933, четверг',
	87: '7 июля 1933, пятница',
	88: '8 июля 1933, суббота',
	89: '9 июля 1933, воскресенье',
	90: '10 июля 1933, понедельник',
	91: '11 июля 1933, вторник',
	92: '12 июля 1933, среда',
	93: '13 июля 1933, четверг',
	94: '14 июля 1933, пятница',
	95: '15 июля 1933, суббота',
	96: '16 июля 1933, воскресенье',
	97: '17 июля 1933, понедельник',
	98: '18 июля 1933, вторник',
	99: '19 июля 1933, среда',
	100: '20 июля 1933, четверг',
	101: '21 июля 1933, пятница',
	102: '22 июля 1933, суббота',
	103: '23 июля 1933, воскресенье',
	104: '24 июля 1933, понедельник',
	105: '25 июля 1933, вторник',
	106: '26 июля 1933, среда',
	107: '27 июля 1933, четверг',
	108: '28 июля 1933, пятница',
	109: '29 июля 1933, суббота',
	110: '30 июля 1933, воскресенье',
	111: '31 июля 1933, понедельник',
	112: '1 августа 1933, вторник',
	113: '2 августа 1933, среда',
	114: '3 августа 1933, четверг',
	115: '4 августа 1933, пятница',
	116: '5 августа 1933, суббота',
	117: '6 августа 1933, воскресенье',
	118: '7 августа 1933, понедельник',
	119: '8 августа 1933, вторник',
	120: '9 августа 1933, среда',
	121: '10 августа 1933, четверг',
	122: '11 августа 1933, пятница',
	123: '12 августа 1933, суббота',
	124: '13 августа 1933, воскресенье',
	125: '14 августа 1933, понедельник',
	126: '15 августа 1933, вторник',
	127: '16 августа 1933, среда',
	128: '17 августа 1933, четверг',
	129: '18 августа 1933, пятница',
	130: '19 августа 1933, суббота',
	131: '20 августа 1933, воскресенье',
	132: '21 августа 1933, понедельник',
	133: '22 августа 1933, вторник',
	134: '23 августа 1933, среда',
	135: '24 августа 1933, четверг',
	136: '25 августа 1933, пятница',
	137: '26 августа 1933, суббота',
	138: '27 августа 1933, воскресенье',
	139: '28 августа 1933, понедельник',
	140: '29 августа 1933, вторник',
	141: '30 августа 1933, среда',
	142: '31 августа 1933, четверг',
	143: '1 сентября 1933, пятница',
	144: '2 сентября 1933, суббота',
	145: '3 сентября 1933, воскресенье',
	146: '4 сентября 1933, понедельник',
	147: '5 сентября 1933, вторник',
	148: '6 сентября 1933, среда',
	149: '7 сентября 1933, четверг',
	150: '8 сентября 1933, пятница',
	151: '9 сентября 1933, суббота',
	152: '10 сентября 1933, воскресенье',
	153: '11 сентября 1933, понедельник',
	154: '12 сентября 1933, вторник',
	155: '13 сентября 1933, среда',
	156: '14 сентября 1933, четверг',
	157: '15 сентября 1933, пятница',
	158: '16 сентября 1933, суббота',
	159: '17 сентября 1933, воскресенье',
	160: '18 сентября 1933, понедельник',
	161: '19 сентября 1933, вторник',
	162: '20 сентября 1933, среда',
	163: '21 сентября 1933, четверг',
	164: '22 сентября 1933, пятница',
	165: '23 сентября 1933, суббота',
	166: '24 сентября 1933, воскресенье',
	167: '25 сентября 1933, понедельник',
	168: '26 сентября 1933, вторник',
	169: '27 сентября 1933, среда',
	170: '28 сентября 1933, четверг',
	171: '29 сентября 1933, пятница',
	172: '30 сентября 1933, суббота',
	173: '1 октября 1933, воскресенье',
	174: '2 октября 1933, понедельник',
	175: '3 октября 1933, вторник',
	176: '4 октября 1933, среда',
	177: '5 октября 1933, четверг',
	178: '6 октября 1933, пятница',
	179: '7 октября 1933, суббота',
	180: '8 октября 1933, воскресенье',
	181: '9 октября 1933, понедельник',
	182: '10 октября 1933, вторник',
	183: '11 октября 1933, среда',
	184: '12 октября 1933, четверг',
	185: '13 октября 1933, пятница',
	186: '14 октября 1933, суббота',
	187: '15 октября 1933, воскресенье',
	188: '16 октября 1933, понедельник',
	189: '17 октября 1933, вторник',
	190: '18 октября 1933, среда',
	191: '19 октября 1933, четверг',
	192: '20 октября 1933, пятница',
	193: '21 октября 1933, суббота',
	194: '22 октября 1933, воскресенье',
	195: '23 октября 1933, понедельник',
	196: '24 октября 1933, вторник',
	197: '25 октября 1933, среда',
	198: '26 октября 1933, четверг',
	199: '27 октября 1933, пятница',
	200: '28 октября 1933, суббота',
	201: '29 октября 1933, воскресенье',
	202: '30 октября 1933, «Урусвати»',
	203: '31 октября 1933, вторник',
	204: '1 ноября 1933, среда',
	205: '2 ноября 1933, четверг',
	206: '3 ноября 1933, пятница',
	207: '4 ноября 1933, суббота',
	208: '5 ноября 1933, воскресенье',
	209: '6 ноября 1933, понедельник',
	210: '7 ноября 1933, вторник',
	211: '8 ноября 1933, среда',
	212: '9 ноября 1933, четверг',
	213: '10 ноября 1933, пятница',
	214: '11 ноября 1933, суббота',
	215: '12 ноября 1933, воскресенье',
	216: '13 ноября 1933, понедельник',
	217: '14 ноября 1933, вторник',
	218: '15 ноября 1933, среда',
	219: '16 ноября 1933, четверг',
	220: '17 ноября 1933, пятница',
	221: '18 ноября 1933, суббота',
	222: '19 ноября 1933, воскресенье',
	223: '20 ноября 1933, понедельник',
	224: '21 ноября 1933, вторник',
	225: '23 ноября 1933, четверг',
	226: '24 ноября 1933, пятница',
	227: '25 ноября 1933, суббота',
	228: '26 ноября 1933, воскресенье',
	229: '27 ноября 1933, понедельник',
	230: '28 ноября 1933, вторник',
	231: '29 ноября 1933, среда',
	232: '30 ноября 1933, четверг',
	233: '1 декабря 1933, пятница',
	234: '2 декабря 1933, суббота',
	235: '3 декабря 1933, воскресенье',
	236: '4 декабря 1933, понедельник',
	237: '5 декабря 1933, вторник',
	238: '6 декабря 1933, среда',
	239: '7 декабря 1933, четверг',
	240: '8 декабря 1933, четверг',
	241: '9 декабря 1933, суббота',
	242: '10 декабря 1933, воскресенье',
	243: '11 декабря 1933, понедельник',
	244: '12 декабря 1933, вторник',
	245: '13 декабря 1933, среда',
	246: '14 декабря 1933, четверг',
	247: '15 декабря 1933, пятница',
	248: '16 декабря 1933, суббота',
	249: '17 декабря 1933, воскресенье',
	250: '18 декабря 1933, понедельник',
	251: '19 декабря 1933, вторник',
	252: '20 декабря 1933, среда',
	253: '21 декабря 1933, четверг',
	254: '22 декабря 1933, пятница',
	255: '23 декабря 1933, суббота',
	256: '24 декабря 1933, воскресенье',
	257: '25 декабря 1933, понедельник',
	258: '26 декабря 1933, вторник',
	259: '27 декабря 1933, среда',
	260: '28 декабря 1933, четверг',
	261: '29 декабря 1933, пятница',
	262: '30 декабря 1933, суббота',
	263: '31 декабря 1933, воскресенье',
	264: '1 января 1934, понедельник',
	265: '2 января 1934, вторник',
	266: '3 января 1934, среда',
	267: '4 января 1934, четверг',
	268: '5 января 1934, пятница',
	269: '6 января 1934, суббота',
	270: '7 января 1934, воскресенье',
	271: '8 января 1934, понедельник',
	272: '9 января 1934, вторник',
	273: '10 января 1934, среда',
	274: '11 января 1934, четверг',
	275: '12 января 1934, пятница',
	276: '13 января 1934, суббота',
	277: '14 января 1934, воскресенье',
	278: '15 января 1934, понедельник',
	279: '16 января 1934, вторник',
	280: '17 января 1934, среда',
	281: '18 января 1934, четверг',
	282: '19 января 1934, [пятница]',
	283: '20 января 1934, суббота',
	284: '21 января 1934, воскресенье',
	285: '22 января 1934, понедельник',
	286: '23 января 1934, вторник',
	287: '24 января 1934, среда',
	288: '25 января 1934, четверг',
	289: '26 января 1934, пятница',
	290: '27 января 1934, суббота',
	291: '28 января 1934, воскресенье',
	292: '29 января 1934, понедельник',
	293: '30 января 1934, вторник',
	294: '31 января 1934, среда',
	295: '1 февраля 1934, четверг',
	296: '2 февраля 1934, пятница',
	297: '3 февраля 1934, суббота',
	298: '4 февраля 1934, воскресенье',
	299: '5 февраля 1934, понедельник',
	300: '6 февраля 1934, вторник',
	301: '7 февраля 1934, среда',
	302: '8 февраля 1934, четверг',
	303: '9 февраля 1934, пятница',
	304: '10 февраля 1934, суббота',
	305: '11 февраля 1934, воскресенье',
	306: '12 февраля 1934, понедельник',
	307: '13 февраля 1934, втоник',
	308: '14 февраля 1934, среда',
	309: '15 февраля 1934, четверг',
	310: '16 февраля 1934, пятница',
	311: '17 февраля 1934, суббота',
	312: '18 февраля 1934, воскресенье',
	313: '19 февраля 1934, понедельник',
	314: '20 февраля 1934, вторник',
	315: '21 февраля 1934, среда',
	316: '22 февраля 1934, четверг',
	317: '23 февраля 1934, пятница',
	318: '24 февраля 1934, суббота',
	319: '25 февраля 1934, воскресенье',
	320: '26 февраля 1934, понедельник',
	321: '27 февраля 1934, вторник',
	322: '28 февраля 1934, среда',
	323: '1 марта 1934, четверг',
	324: '2 марта 1934, пятница',
	325: '3 марта 1934, суббота',
	326: '4 марта 1934, воскресенье',
	327: '5 марта 1934, понедельник',
	328: '6 марта 1934, вторник',
	329: '7 марта 1934, среда',
	330: '8 марта 1934, четверг',
	331: '9 марта 1934, пятница',
	332: '10 марта 1934, суббота',
	333: '11 марта 1934, воскресенье',
	334: '12 марта 1934, понедельник',
	335: '13 марта 1934, вторник',
	336: '14 марта 1934, среда',
	337: '15 марта 1934, четверг',
	338: '16 марта 1934, пятница',
	339: '17 марта 1934, суббота',
	340: '18 марта 1934, воскресенье',
	341: '19 марта 1934, понедельник',
	342: '20 марта 1934, вторник'
}
