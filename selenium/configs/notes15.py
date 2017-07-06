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
files_path = '/users/schrecknetuser/pdf-ocr/letters4'

shift_modifier = 0

book_structure = Book('__name__',
                      [],
                      [],
                      '1-341')
pages_dictionary = {
	1: '19 октября 1935, суббота, «Урусвати»',
	2: '20 октября 1935, воскресенье',
	3: '21 октября 1935, понедельник',
	4: '22 октября 1935, вторник',
	5: '23 октября 1935, среда',
	6: '24 октября 1935, четверг',
	7: '25 октября 1935, пятница',
	8: '26 октября 1935, суббота',
	9: '27 октября 1935, воскресенье',
	10: '28 октября 1935, понедельник',
	11: '29 октября 1935, вторник',
	12: '30 октября 1935, среда',
	13: '31 октября 1935, четверг',
	14: '1 ноября 1935, пятница',
	15: '2 ноября 1935, суббота',
	16: '3 ноября 1935, воскресенье',
	17: '4 ноября 1935, понедельник',
	18: '5 ноября 1935, вторник',
	19: '6 ноября 1935, среда',
	20: '7 ноября 1935, четверг',
	21: '8 ноября 1935, пятница',
	22: '9 ноября 1935, суббота',
	23: '10 ноября 1935, воскресенье',
	24: '11 ноября 1935, понедельник',
	25: '12 ноября 1935, вторник',
	26: '13 ноября 1935, среда',
	27: '14 ноября 1935, четверг',
	28: '15 ноября 1935, пятница',
	29: '16 ноября 1935, суббота',
	30: '17 ноября 1935, воскресенье',
	31: '18 ноября 1935, понедельник',
	32: '19 ноября 1935, вторник',
	33: '20 ноября 1935, среда',
	34: '21 ноября 1935, четверг',
	35: '22 ноября 1935, пятница',
	36: '23 ноября 1935, суббота',
	37: '24 ноября 1935, воскресенье',
	38: '25 ноября 1935, понедельник',
	39: '26 ноября 1935, вторник',
	40: '27 ноября 1935, среда',
	41: '28 ноября 1935, четверг',
	42: '29 ноября 1935, пятница',
	43: '30 ноября 1935, суббота',
	44: '1 декабря 1935, воскресенье',
	45: '2 декабря 1935, понедельник',
	46: '3 декабря 1935, вторник',
	47: '4 декабря 1935, среда',
	48: '5 декабря 1935, четверг',
	49: '6 декабря 1935, пятница',
	50: '7 декабря 1935, суббота',
	51: '8 декабря 1935, воскресенье',
	52: '9 декабря 1935, понедельник',
	53: '10 декабря 1935, вторник',
	54: '11 декабря 1935, среда',
	55: '12 декабря 1935, четверг',
	56: '13 декабря 1935, пятница',
	57: '14 декабря 1935, суббота',
	58: '15 декабря 1935, воскресенье',
	59: '16 декабря 1935, понедельник',
	60: '17 декабря 1935, вторник, утро',
	61: '17 декабря 1935, вторник',
	62: '18 декабря 1935, среда',
	63: '19 декабря 1935, четверг',
	64: '20 декабря 1935, пятница',
	65: '21 декабря 1935, суббота',
	66: '22 декабря 1935, воскресенье',
	67: '23 декабря 1935, понедельник',
	68: '24 декабря 1935, вторник',
	69: '25 декабря 1935, среда',
	70: '26 декабря 1935, четверг',
	71: '27 декабря 1935, пятница',
	72: '28 декабря 1935, суббота',
	73: '29 декабря 1935, воскресенье',
	74: '30 декабря 1935, понедельник',
	75: '31 декабря 1935, вторник',
	76: '1 января 1936, среда',
	77: '2 января 1936, четверг',
	78: '3 января 1936, пятница',
	79: '4 января 1936, суббота',
	80: '5 января 1936, воскресенье',
	81: '6 января 1936, понедельник',
	82: '7 января 1936, вторник',
	83: '8 января 1936, среда',
	84: '9 января 1936, четверг',
	85: '10 января 1936, пятница',
	86: '11 января 1936, суббота',
	87: '12 января 1936, воскресенье',
	88: '13 января 1936, понедельник',
	89: '14 января 1936, вторник',
	90: '15 января 1936, среда',
	91: '16 января 1936, четверг',
	92: '17 января 1936, пятница',
	93: '18 января 1936, суббота',
	94: '19 января 1936, воскресенье',
	95: '20 января 1936, понедельник',
	96: '21 января 1936, вторник',
	97: '22 января 1936, среда',
	98: '23 января 1936, четверг',
	99: '24 января 1936, пятница',
	100: '25 января 1936, суббота',
	101: '26 января 1936, воскресенье',
	102: '27 января 1936, понедельник',
	103: '28 января 1936, вторник',
	104: '29 января 1936, среда',
	105: '30 января 1936, четверг',
	106: '31 января 1936, пятница',
	107: '1 февраля 1936, суббота',
	108: '2 февраля 1936, воскресенье',
	109: '3 февраля 1936, понедельник',
	110: '4 февраля 1936, вторник',
	111: '5 февраля 1936, среда',
	112: '6 февраля 1936, четверг',
	113: '7 февраля 1936, пятница',
	114: '8 февраля 1936, суббота',
	115: '9 февраля 1936, воскресенье',
	116: '10 февраля 1936, понедельник',
	117: '11 февраля 1936, вторник',
	118: '12 февраля 1936, среда',
	119: '13 февраля 1936, четверг',
	120: '14 февраля 1936, пятница',
	121: '15 февраля 1936, суббота',
	122: '16 февраля 1936, воскресенье',
	123: '17 февраля 1936, понедельник',
	124: '18 февраля 1936, вторник',
	125: '19 февраля 1936, среда',
	126: '20 февраля 1936, четверг',
	127: '21 февраля 1936, пятница',
	128: '23 февраля 1936, воскресенье',
	129: '24 февраля 1936, понедельник',
	130: '25 февраля 1936, вторник',
	131: '26 февраля 1936, среда',
	132: '27 февраля 1936, четверг',
	133: '28 февраля 1936, пятница',
	134: '29 февраля 1936, суббота',
	135: '1 марта 1936, воскресенье',
	136: '2 марта 1936, понедельник',
	137: '3 марта 1936, вторник',
	138: '4 марта 1936, среда',
	139: '5 марта 1936, четверг',
	140: '6 марта 1936, пятница',
	141: '7 марта 1936, суббота',
	142: '8 марта 1936, воскресенье',
	143: '9 марта 1936, понедельник',
	144: '10 марта 1936, вторник',
	145: '11 марта 1936, среда',
	146: '12 марта 1936, четверг',
	147: '13 марта 1936, пятница',
	148: '14 марта 1936, суббота',
	149: '15 марта 1936, воскресенье',
	150: '16 марта 1936, понедельник',
	151: '17 марта 1936, вторник',
	152: '18 марта 1936, среда',
	153: '19 марта 1936, четверг',
	154: '20 марта 1936, пятница',
	155: '21 марта 1936, суббота',
	156: '22 марта 1936, воскресенье',
	157: '23 марта 1936, понедельник',
	158: '24 марта 1936, вторник',
	159: '25 марта 1936, среда',
	160: '26 марта 1936, четверг',
	161: '27 марта 1936, пятница',
	162: '28 марта 1936, суббота',
	163: '29 марта 1936, воскресенье',
	164: '30 марта 1936, понедельник',
	165: '31 марта 1936, вторник',
	166: '1 апреля 1936, среда',
	167: '2 апреля 1936, четверг',
	168: '3 апреля 1936, пятница',
	169: '4 апреля 1936, суббота',
	170: '5 апреля 1936, воскресенье',
	171: '6 апреля 1936, понедельник',
	172: '7 апреля 1936, вторник',
	173: '8 апреля 1936, среда',
	174: '9 апреля 1936, четверг',
	175: '10 апреля 1936, пятница',
	176: '11 апреля 1936, суббота',
	177: '12 апреля 1936, Светлое Воскресенье',
	178: '13 апреля 1936, понедельник',
	179: '14 апреля 1936, вторник',
	180: '15 апреля 1936, среда',
	181: '16 апреля 1936, четверг',
	182: '17 апреля 1936, пятница',
	183: '18 апреля 1936, суббота',
	184: '19 апреля 1936, воскресенье',
	185: '20 апреля 1936, понедельник',
	186: '21 апреля 1936, вторник',
	187: '22 апреля 1936, среда',
	188: '23 апреля 1936, четверг',
	189: '24 апреля 1936, пятница',
	190: '25 апреля 1936, суббота',
	191: '26 апреля 1936, воскресенье',
	192: '27 апреля 1936, понедельник',
	193: '28 апреля 1936, вторник',
	194: '29 апреля 1936, среда',
	195: '30 апреля 1936, четверг',
	196: '1 мая 1936, пятница',
	197: '2 мая 1936, суббота',
	198: '3 мая 1936, воскресенье',
	199: '4 мая 1936, понедельник',
	200: '5 мая 1936, вторник',
	201: '6 мая 1936, среда',
	202: '7 мая 1936, четверг',
	203: '8 мая 1936, пятница',
	204: '9 мая 1936, суббота',
	205: '10 мая 1936, воскресенье',
	206: '11 мая 1936, понедельник',
	207: '12 мая 1936, вторник',
	208: '13 мая 1936, среда',
	209: '14 мая 1936, четверг',
	210: '15 мая 1936, пятница',
	211: '16 мая 1936, суббота',
	212: '17 мая 1936, воскресенье',
	213: '18 мая 1936, понедельник',
	214: '19 мая 1936, вторник',
	215: '20 мая 1936, среда',
	216: '21 мая 1936, четверг',
	217: '22 мая 1936, пятница',
	218: '23 мая 1936, суббота',
	219: '24 мая 1936, воскресенье',
	220: '25 мая 1936, понедельник',
	221: '26 мая 1936, вторник',
	222: '27 мая 1936, среда',
	223: '28 мая 1936, четверг',
	224: '29 мая 1936, пятница',
	225: '30 мая 1936, суббота',
	226: '31 мая 1936, воскресенье',
	227: '1 июня 1936, понедельник',
	228: '2 июня 1936, вторник',
	229: '3 июня 1936, среда',
	230: '4 июня 1936, четверг',
	231: '5 июня 1936, пятница',
	232: '6 июня 1936, суббота',
	233: '7 июня 1936, воскресенье',
	234: '8 июня 1936, понедельник',
	235: '9 июня 1936, вторник',
	236: '10 июня 1936, среда',
	237: '11 июня 1936, четверг',
	238: '12 июня 1936, пятница, «Урусвати»',
	239: '13 июня 1936, суббота',
	240: '14 июня 1936, воскресенье',
	241: '15 июня 1936, понедельник',
	242: '16 июня 1936, вторник',
	243: '17 июня 1936, среда',
	244: '18 июня 1936, четверг',
	245: '19 июня 1936, пятница',
	246: '20 июня 1936, суббота',
	247: '21 июня 1936, воскресенье',
	248: '22 июня 1936, понедельник',
	249: '23 июня 1936, вторник',
	250: '24 июня 1936, среда',
	251: '25 июня 1936, четверг',
	252: '26 июня 1936, пятница',
	253: '27 июня 1936, суббота',
	254: '28 июня 1936, воскресенье',
	255: '29 июня 1936, понедельник',
	256: '30 июня 1936, вторник',
	257: '1 июля 1936, среда',
	258: '2 июля 1936, четверг',
	259: '3 июля 1936, пятница',
	260: '4 июля 1936, суббота',
	261: '5 июля 1936, воскресенье',
	262: '6 июля 1936, понедельник',
	263: '7 июля 1936, вторник',
	264: '8 июля 1936, среда',
	265: '9 июля 1936, четверг',
	266: '10 июля 1936, пятница',
	267: '11 июля 1936, суббота',
	268: '12 июля 1936, воскресенье',
	269: '13 июля 1936, понедельник',
	270: '14 июля 1936, вторник',
	271: '15 июля 1936, среда',
	272: '16 июля 1936, четверг',
	273: '17 июля 1936, пятница',
	274: '18 июля 1936, суббота',
	275: '19 июля 1936, воскресенье',
	276: '20 июля 1936, понедельник',
	277: '21 июля 1936, вторник',
	278: '22 июля 1936, среда',
	279: '23 июля 1936, четверг',
	280: '24 июля 1936, пятница',
	281: '25 июля 1936, суббота',
	282: '26 июля 1936, воскресенье',
	283: '27 июля 1936, понедельник',
	284: '28 июля 1936, вторник',
	285: '29 июля 1936, среда',
	286: '30 июля 1936, четверг',
	287: '31 июля 1936, пятница',
	288: '1 августа 1936, суббота',
	289: '2 августа 1936, воскресенье',
	290: '3 августа 1936, понедельник',
	291: '4 августа 1936, вторник',
	292: '5 августа 1936, среда',
	293: '6 августа 1936, четверг',
	294: '7 августа 1936, пятница',
	295: '8 августа 1936, суббота',
	296: '9 августа 1936, воскресенье',
	297: '10 августа 1936, понедельник',
	298: '11 августа 1936, вторник',
	299: '12 августа 1936, среда',
	300: '13 августа 1936, четверг',
	301: '14 августа 1936, пятница',
	302: '15 августа 1936, суббота',
	303: '16 августа 1936, воскресенье',
	304: '17 августа 1936, понедельник',
	305: '18 августа 1936, вторник',
	306: '19 августа 1936, среда',
	307: '20 августа 1936, четверг',
	308: '21 августа 1936, пятница',
	309: '22 августа 1936, суббота',
	310: '23 августа 1936, воскресенье',
	311: '24 августа 1936, понедельник',
	312: '25 августа 1936, вторник',
	313: '26 августа 1936, среда',
	314: '27 августа 1936, четверг',
	315: '28 августа 1936, пятница',
	316: '29 августа 1936, суббота',
	317: '30 августа 1936, воскресенье',
	318: '31 августа 1936, понедельник',
	319: '1 сентября 1936, вторник',
	320: '2 сентября 1936, среда',
	321: '3 сентября 1936, четверг',
	322: '4 сентября 1936, пятница',
	323: '5 сентября 1936, суббота',
	324: '6 сентября 1936, воскресенье',
	325: '7 сентября 1936, понедельник',
	326: '8 сентября 1936, вторник',
	327: '9 сентября 1936, среда',
	328: '10 сентября 1936, четверг',
	329: '11 сентября 1936, пятница',
	330: '12 сентября 1936, суббота',
	331: '13 сентября 1936, воскресенье',
	332: '14 сентября 1936, понедельник',
	333: '15 сентября 1936, вторник',
	334: '16 сентября 1936, среда',
	335: '17 сентября 1936, четверг',
	336: '18 сентября 1936, пятница',
	337: '19 сентября 1936, суббота',
	338: '20 сентября 1936, воскресенье',
	339: '21 сентября 1936, понедельник',
	340: '22 сентября 1936, вторник',
	341: '23 сентября 1936, среда',
}
