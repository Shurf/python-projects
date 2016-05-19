# coding=utf-8

from collections import namedtuple

default_book_name = "____current_book"
# default_book_name = "Тест"
# default_book_name = "I. Космогенезис (космическая эволюция)"
Part = namedtuple("Part", "name pages num")
Part.__new__.__defaults__ = (None, None, None)
Chapter = namedtuple("Chapter", "name parts pages")
Book = namedtuple("Book", "name chapters parts pages")

page_selector = 'etika-2.1 - (.+)'
pdf_extension = '.pdf'
html_extension = '.html'
files_path = '/users/schrecknetuser/pdf-ocr/etika-2.1/etika-2.1.pdf/'

shift_modifier=6

book_structure = Book('__name__',
    [
    Chapter('Победившая Стража Порога',
        [
        Part('Учитель Серапис: "Это одно из самых тяжелых ее испытаний"',
            '11-17'),
        Part('"Если бы я даже была такой, какой они рисуют меня..."',
            '18-29'),
        Part('Письма Учителя Сераписа Генри Олькотту',
            '34-43'),
        Part('Братство имеет во всех веках особые Ашрамы',
            '30-43'),
        Part('Дополнение редакции к Заметкам',
            '44-46'),
        Part('Строки из Граней Агни Йоги',
            '47-47'),
        Part('Дополнение редакции. Несколько слов о Храме Человечества.',
            '48-48'),
        Part('Иисус и Его Страж Порога. Учитель Илларион: «Блаватская была представительницей  той самой группы Учитилей, которая направляла неофитов Храма Человечества',
            '49-51'),
        Part('Без семилетних суровых испытаний никто не может быть принят даже в качестве послушника. Стоит только вступить на путь испытуемого',
            '52-53'),
        Part('Ученичество обнажает скрытую суть человека',
            '54-54'),
        Part('Учитель Кут Хуми: "Если в нашу дверь постучится подходящий человек, ему всегда откроют"',
            '55-56'),
        Part('"Вестник"',
            '57-64'),
        ],
        '7-10'
    ),
    Chapter('"Я искала встречи с неведомым"',
        [
    Part('"Эта маленькая барышня отличается от всех вас"',
        '67-67'),
        Part('Учитель Мориа, Владыка Шамбалы',
            '68-69'),
        Part('Избрание Вестника. Или Путь на Голгофу.',
            '70-70'),
        Part('Вера Желиховская "Некоторое время она позволяла себе играть психическими силами..."',
            '71-79'),
        Part('Учитель Мориа, Владыка Шамбалы:',
            '80-85'),
        Part('Небольшое примечание редактора',
            '86-86'),
        Part('"С четырнадцатилетнего возраста я каждый свой день встречала в физическом теле, а ночи проводила в теле астральном"',
            '87-87'),
        Part('Учитель Кут Хуми',
            '88-89'),
        Part('Примечание редактора',
            '90-91'),
        Part('Нью-Йоркская газета «Tribune» на третий день после смерти Е.П. Блаватской (10 мая 1891г.)',
            '92-95'),
        Part('От редактора - два небольших дополнения',
            '96-96'),
        Part('Из воспоминаний Веры Желиховской о старшей сестре…',
            '97-100'),
        Part('"Мадам Блаватская вновь появилась в миру" после обучения в Гималайском Ашраме Шамбалы',
            '101-102'),

        ],
        '65-66'
    ),
    Chapter('"Я послана сюда, в эту страну, моей Ложей [Белым братством], дабы сказать правду о современном спиритуализме"',
        [
        Part('Ее обвиняли, что она выдумала Махатм',
            '105-105'),
        Part('Строки из Агни Йоги. Учитель Кут Хуми писал в 1881 году… Предсказание Йога Рамалингама',
            '106-107'),
        Part('"Меня приняли за русскую шпионку"',
            '108-108'),
        Part('"О, как бы мне хотелось научить вас тем вещам, о которых вы, по-видимому, пока еще ничего не знаете!" "Быть может, я появилась лет на 100 раньше, чем следовало..." .',
            '109-109'),
        Part('Доктор Гартман, получив письмо "ниоткуда", пошел к ясновидящей, желая удостовериться: не фокус ли это мадам Блаватской или таинственные Гималайские Учителя все же не миф?',
            '110-118'),
        Part('Мысли участников сеанса притягивают к медиуму распадающиеся астральные останки умерших, сбрасываемые душой.',
            '119-119'),
        Part('1881 год. Учитель Мориа, Владыка Шамбалы: "Лучше пусть погибнет Т.О., чем мы позволим ему превратиться в нечто вроде академии магии или салона оккультизма"',
            '120-120'),
        Part('"Вовлечение умерших в наш мир... превращает их посмертное существование в ад"',
            '121-122'),
        Part('Е. П. Блаватская: "Я борюсь... против откровенно абсурдных, однако возведенных в догму теорий, которые... гласят, что оккультные феномены производят души умерших людей, и только людей"',
            '123-123'),
        Part('1938 год. Учитель Мориа: "Нужно отставить слово оккультизм... теперь оно звучит бессмысленно"',
            '124-124'),
        Part('Душа человека "не приклеена" к физическому телу, это отдельная сущность, и в обычном человеке действует независимо во время сна, а в Посвященном Адепте - в любое время.',
            '125-127'),
        Part('Учитель Кут Хуми: жизни не хватит, чтобы убедить скептиков. Примечание редактора.',
            '128-130'),
        Part('"...неутешная Изида соберет разбросанные по всему Миру части растерзанного тела Озириса и воссоедит их" Строки из письма Е.И. Рерих от 13 апреля 1953 года. "Всемирное братство" не есть пустая фраза',
             '131-132'),
        Part('Дамодар К. Маваланкар: в физическом теле - за учителем по воде, словно по суше.',
            '133-133'),
        Part('"Бесполезно спорить с фанатиком"',
            '134-134'),
        Part('Астральная Елена идет по воде, как по суше. И о книге, перемещающейся по воздуху.',
            '135-135'),
        Part('"... я могу отправиться, когда захочу, хотя, уверяю вас, туда ни за что не проникнуть ни Пржевальскому, ни кому-либо из англичан"',
            '136-136'),
        Part('"Астральная душа шамана путешествовала, повинуясь нашему не высказанному вслух желанию"',
            '137-141'),
        Part('Она уже контролировала свои силы',
            '142-145'),
        Part('Астральный двойник может убить',
            '146-146'),
        Part('Она могла писать и рисовать в записной книжке, даже не прикоснувшись к ней, к тому же не своим почерком, к тому же книжка эта была за чужой пазухой',
            '147-148'),
        Part('Она читает, не распечатывая письма, и переносит в... запечатанный конверт рисунок, возникший в ее воображении способом "осаждения"',
            '149-150'),
        Part('Можно ли "приказать графитному порошку самому складываться в слова?"',
            '151-152'),
        Part('Передача писем с помощью мысли',
            '153-153'),
        Part('Блаватская: "что же мешает нам думать о пространстве с большим числом измерений?"',
            '154-158'),
        Part('От сознания - к сознанию. О передаче образов, которые воспроизводятся перед глазами, словно на экране телевизоров.',
            '159-159'),
    Part('Гномик Поу Дхи подшивает полотенца для Е.П.Б.',
            '160-160'),
        Part('"Теперь о Джоне Кинге - этом короле вредных негодников"',
            '161-167'),
        Part('"Почему Великие Учителя не допускают человечество к тайнам мира духов природы"',
            '168-170'),
        Part('Ей пришлось стать невидимой',
            '171-171'),
        Part('Волосы вдруг длинее - гипноз? Но, может, нечто другое?',
            '172-172'),
        Part('Ее светлокаштановый шелковистый локон почернел на глазах Олькотта - уж это точно не гипноз!',
            '173-173'),
        Part('Превращение одной личности в другую',
            '174-174'),
        Part('"Духи говорят: это подарок для мадам Блаватской"',
            '175-175'),
        Part('Свой ад творит сам человек',
            '176-177'),
        Part('Она производила феномены по своей воле',
            '178-179'),
        Part('Г. Олькотт: "Никто не знал ее так близко, как я"',
            '180-182'),
        Part('Учитель: "Я не могу утверждать, что я входил, но я посылал такие мощные токи..."',
            '183-183'),
        Part('Из дневниковых бесед Елены Рерих с ее Учителем Мориа, Владыкой Шамбалы',
            '184-185'),
        Part('Явление Учителя в астральном теле',
            '186-186'),
        Part('Из дневниковых бесед Елены Рерих с ее Учителем Мориа, Владыкой Шамбалы:',
            '187-187'),
        Part('Примечание редактора',
            '188-188'),
        Part('Дождь из роз',
            '189-189'),
        Part('Такое бывает не только в волшебных сказках. Или октябрь в Симле.',
            '190-197'),
        Part('Она сказала: "Поверните меня в сторону, где он живет, и письмо, которое вы требуете от британского представителя при дворе местного князя будет тут же получено"',
            '198-199'),
        Part('Даже хлебные крошки способны запечатлевать и отражать, т.е. фотографировать и воспроизводить в сознании ясновидца всю картину, с ними связанную.',
            '200-200'),
        Part('Учитель явился в астральном облике.',
            '201-203'),
        Part('Жить людям среди людей не совсем просто. Но как же сложно быть среди людей Вестником Света.',
            '204-205'),
        Part('Музыка, вызванная из пространства.',
            '206-206'),
        Part('Она переместила... атомы в связке ключей, чтобы, к радости детей, получился свисток, но сестре сказала, что она могла бы сделать и золото.',
            '207-207'),
        Part('Прощаясь, он сказал:"Я никогда больше не буду сомневаться". Но... не прошло и двух недель...',
            '208-210'),
        Part('Примечание редакции',
            '211-211'),
        Part('Друг испанского короля убежден, что Е. П. Б. однажды спасла ему жизнь… Над головой сверкнула молния, но она сказала: "Не обращайте внимания".',
            '212-212'),
        Part('"Уходя, он забыл убрать свою атмосферу" - гости незримые и зримые, но исчезающие.',
            '213-213'),
        Part('Ее внутреннее тело сияло, словно было из расплавленного золота.',
            '214-214'),
        Part('Таинственная рука',
            '215-217'),
        Part('Елена Рерих - об опасностях медиудизма',
            '218-221'),
        Part('Из дневниковых записей бесед Елены Рерих с ее Учителей Мориа, Владыкой Шамбалы.',
            '222-224'),
        Part('Из дневниковых записей бесед Елены Рерих с ее Учителей Мориа, Владыкой Шамбалы:',
            '225-225'),
        Part('Елена Блаватская: "Я - не медиум"',
            '226-226'),
        ],
        '103-104'
    ),
    Chapter('"Разоблаченная Изида" - великая книга мадам Блаватской"',
        [
        Part('От редакции - несколько предваряющих слов',
            '229-229'),
        Part('Е. П. Блаватская: "Меня обвиняют..."',
            '230-231'),
        Part('Е.П. Блаватская: "Как в волшебной панораме проходят предо мной столетие за столетием, образ за образом...мифы объясняются мне с событиями и людьми, существовавшими в действительности"',
            '232-234'),
        Part('Аббат Фретхейм: "Я могу сообщить мои мысли на расстоянии много сотен миль"',
            '235-235'),
        Part('Учитель Мориа, Владыка Шамбалы: "Знаменательным терафимом Братства является камень дальних миров"',
            '236-236'),
        Part('Когда пуля не берет, а огнем можно умыться. Или о психической силе амулетов.',
            '237-240'),
        Part('Фотография пейзажа, сделанная на крышке блюда только волей и светом. Чародеи Индии на ваших глазах могут посадить в землю семя и через час вырастить дерево, которое тут же покроется листвой, цветами и даст плоды, а так же они могут остановить и стрелу в полете',
            '241-241'),
        Part('При работе над "Разоблаченной Изидой" она часто бывала "кем-то другим"',
            '242-244'),
        Part('Фокус-покус? Иллюзия? - конечно!',
            '245-247'),
        Part('Елена Рерих: В теософ[ской] литературе можно найти указания, что Иисус был воплощением Учителя К[ут] Х[уми]',
            '248-249'),
        Part('Учитель Мориа: "Звезда Аллагабада указала путь.."',
            '250-250'),
        Part('Самый знаменитый фокусник сказал, что он может воспроизвести те же феномены, что и медиумы и индийские маги, но только при условии',
            '251-251'),
        Part('"Она просто переутомилась, а ее чуть не сожгли заживо"',
            '252-252'),
        Part('Монах, философ, ученый и маг Роджер Бекон',
            '253-255'),
        Part('Все места обитания Адептов Братства абсолютно защищены кольцом иллюзии, которую создают и поддерживают служащие им духи природы',
            '256-256'),
        Part('Феномен "воплощения" ламы в младенца.',
            '257-259'),
        Part('"...Е.П. Блаватская: "Мои книги написаны не против религии, не против Христа, а против трусливого лицемерия тех, кто убивал, сжигал людей на кострах во имя Всемогущего Сына Божьего, начав это делать практически сразу же после Его смерти на кресте..."',
            '260-262'),
        Part('Власть человеческой воли: тигры и кобры цепенеют; по просьбе людей, изнемогающих от жары льется дождь; на расстоянии бледнеет или гасится пламя, а диван движется',
            '263-263'),
        Part('Профессор Х. Корсон, когда его попросили назвать самого выдающегося из всех замечательных людей, которых он встречал в своей жизни, он назвал Блаватскую.',
            '264-269'),
        Part('А.П. Синнетт: "Разоблаченная Изида" - великая книга мадам Блаватской, но "нередко, пока мадам спала, изрядное количество подлинных страниц ее рукописи оказывалось написанным чужим почерком"',
            '270-272'),
        Part('Факиры сидят на воздухе, по земле ходят статуи, а камни превращаются в хлеб',
            '273-273'),
        Part('При написании "Разоблаченной Изиды" она для сверки... материализировала астральные страницы.',
            '274-275'),
        Part('Силой излучения глаз можно убить не только птицу и жабу...',
            '276-276'),
        Part('Учитель Мориа, Владыка Шамбалы:"В молитвах нередко упоминаются обращения"',
            '277-277'),
        Part('Чудеса, сотворенные силой воображения святого, и чудеса колдуна',
            '278-279'),
        Part('Примечание редактора. Колдовство священников… дыханием, после которого вдруг появляются… стигматы',
            '280-282'),
        Part('Феномены, сотворенные силой воображения и людей, и животных',
            '283-285'),
        Part('Таинственная связь дерева и человека',
            '286-286'),
        Part('Чудо-дерево, на всех листьях которого буквы и священные слова',
            '287-287'),
        Part('Ясновидящие и пророчествующие младенцы',
            '288-290'),
        Part('Пока малыш спал, листы бумаги под его головкой превращались в трактаты, написанные на древнем санскрите',
            '291-291'),
        Part('Грудные младенцы говорят на чистом французском',
            '292-296'),
        Part('"Чтобы прекратить психические расстройства трясунов или трясуний, надо было их только женить или выдать замуж!"',
            '297-297'),
        Part('Огнеупорные медиумы Востока и их гномы',
            '298-298'),
        Part('Битва окончилась четыреста лет тому назад, но кони все продолжают ржать и возгласы солдат все еще звучат над полем сражения.',
            '299-300'),
        Part('Утопленника отыскивает его одежда',
            '301-301'),
        Part('"Старинные вещи, ожерелья, кольца, древние камни на перекрестках дорог видели много и много хранят"',
            '302-302'),
        Part('Вампиры и призраки',
            '303-305'),
        Part('Дополнение редактора',
            '306-306'),
        Part('Талисман',
            '307-307'),
        Part('Можно заставить увидеть сон по приказу. Похоронили факира на шесть недель заживо, а потом оживили',
            '308-310'),
        Part('Хуан-Цзан вызывает Будду',
            '311-311'),
        Part('Посещение того света по просьбе',
            '312-312'),
        Part('Руки лежали на крышке рояля, но чего он только не играл!',
            '313-316'),
        Part('Статуя, убегающая в леса',
            '317-317'),
        Part('Через сотни километров, получив мысленный приказ прийти, он оставил на время свое физическое тело под надзором и мгновенно в тонком теле прибыл пред очи Шаберона',
            '318-320'),


        ],
        '227-228'
    ),
    Chapter('Учитель',
        [
        Part('Таинственный Радж-йог Гулаб-Лалл-Синг',
            '323-327'),
        Part('Опасное приключение в Бахгских пещерах',
            '328-328'),
        Part('Тайна Учителя',
            '329-331'),
        Part('Гулаб Лалл Синг в теле физическом? Или в теле из уплотненного астрала?',
            '332-333'),
        Part('От редакции - два небольших дополнения из книги Е. П. Блаватской "Гималайские Братья" и сборника "Письма Учителей Мудрости"',
            '334-339'),
        Part('Он не стареет',
            '340-343'),
        Part('Художник убежден, что он рисует то, что видят его глаза.',
            '344-345'),
        Part('Три факира из пагоды',
            '346-347'),
        Part('Может ли человек поменяться телом с другим человеком?',
            '348-349'),
        Part('Как рыбоглазая индийская богиня спасла от пожара коллектора-англичанина.',
            '350-351'),
        Part('Бесценный подарок в простой коробочке. Салиграм.',
            '352-355'),
        Part('Магический жезл из простой палки.',
            '356-357'),
        Part('Е.П. Блаватская: "В Тибете распространено пророчество..."',
            '358-358'),
        ],
        '321-322'
    ),
    Chapter('Мир обвинял ее в том, что она категорически... отрицала свою гениальность!',
        [
        Part('Учитель предложил выбор, и она выбрала труднейшее.',
            '361-361'),
        Part('Учитель Кут Хуми: «Все хорошие результаты для Индии существуют благодаря ее личным усилиям» Учитель Мориа, Владыка ШАмбалы: ничтожность барабанной шкуры. Несколько слов от редактора',
            '362-362'),
        Part('Из дневниковых бесед Елены Рерих с ее Учителем Мориа, Владыкой Шамбалы.',
            '363-363'),
        Part('Мохандас Ганди: "Я был бы более чем удовлетворен, если бы смог коснуться края одежды мадам Блаватской"',
            '364-366'),
        Part('"Тайная доктрина" - произведение Елены Блаватской, Учителя Мории и Учителя Кут Хуми.',
            '367-367'),
        Part('Джавахарлал Неру: "В тринадцать лет я вступил в Теософское общество"',
            '368-369'),
        Part('Успенский: "Книжка Всеволода Соловьева "Современная жрица Изиды", по которой многии [в России] знают о Блаватской, полна... злобы и вся состоит из сыщнического описания подсматриваний, подглядываний, выспрашиваний у прислуги"',
            '370-371'),
        Part('Индира Ганди: "Хорошо известна его [Теософского общества] роль в культурном и политическом возрождении Индии"',
            '372-373'),
        Part('Елена Рерих: "Соловьев не заметил, какой суровый приговор он подписал себе этой книгою!"',
            '374-375'),
        Part('В. Буренин: Или Соловьев «охотно привирает», или же во время своего знакомства со жрицей Изиды он… находился не совсем в здоровом состоянии. И’з дневниковых записей бесед Елены Рерих с ее Учителем Мориа, Владыкой Шамбалы (о Соловьеве)',
            '376-376'),
        Part('Учитель снова предложил выбор, и она опять избрала труднейшее.',
            '377-377'),
        Part('А. Брусилов: Благодаря оккультным истинам "с которыми она нас знакомила", "жизнь человеческая становится намного легче и светлее"',
            '378-378'),
        Part('Из дневниковых записей бесед Елены Рерих с ее Учителем Мориа, Владыкой Шамбалы.',
            '379-380'),
        Part('Основа «Тайной Доктрины» дана на тайном языке Великих Посвященных - на языке Сензар. Примечание редактора.',
            '381-381'),
        Part('Э. Ухтомский: "Для Индии настоящего и будущего Е.П. Блаватская не умерла и не умрет"',
            '382-383'),
        Part('Г. Олькотт: "Указав нам Путь, она вложила в нашу жизнь столько смысла, что мы не можем теперь испытывать к ней ничего, кроме благодарности"',
            '384-385'),
        Part('Е. П. Блаватская - архиепископу Кентерберийскому',
            '386-386'),
        Part('Елена Рерих: "...жестокие искажения претерпевались всеми великими людьми, не говоря уже об искаженных Обликах Вел[иких] Учителей человечества"',
            '387-388'),
        Part('Две стороны "священного слова чести". Или Об "ошибке" Вестника. Учитель Илларион: "Если тебе хочется понять различие между Сынами света и Сынами Тени..."',
            '389-391'),
        Part('1991 г., 8 мая. Стефан Хоэллер: "Что за чудо, что за тайна..."',
            '392-393'),
        Part('Известные ученые-буддисты ХХ века о Елене Блаватской. Герберт Барроу, лондонский рабочий, член парламента: "Только два года прошло с того момента, как я ее узнал", но они "были для меня так полны..."',
            '394-397'),
        Part('Елена Рерих - «Елена Блаватская - наша национальная гордость». Елена Блаватская - о "Тайной Доктрине"',
            '398-399'),
        Part('Учитель Мориа: «Мы указывали область…». Учитель Мориа, Владыка Шамбалы: "Могут спросить..."',
            '400-401'),
        Part('Елена Рерих, переводчик «Тайной Доктрины». Из дневниковых записей бесед Елены Рерих с Владыкой Шамбалы.Учитель Мориа - Елене Рерих: "Вижу, как твое желание дать русскому народу высшее знание исполнится…».',
            '402-402'),
        Part('Учитель Илларион: каждый шаг новой мысли - это знания, выданные миру по указу Белой ЛожиУчитель Кут Хуми: "точные науки... не имеют ничего общего с моралью"',
            '404-405'),
        Part('Уильям Джадж. Она мне писала: «Три обычных, здоровых человека едва могли бы делать то, что я должна делать одна. Учитель Мориа: "Знать о себе невозможно в телесной оболочке"',
            '406-409'),
        Part('В присутствии Скрябина "против Блаватской спорить было уже нельзя "',
            '410-413'),
        Part('Несколько слов Е.П. Блаватской о У.К. Джадже - он был для нее "другом, братом и сыном"',
            '414-415'),
        Part('УУчитель Кут Хуми: "Они общаются с нами посредством звука и цвета"',
            '416-416'),
        Part('Анни Безант: "Если ученик подавал надежды, она безжалостно боролась с его тщеславием, самомнением, претензиями на обладание знанием"',
            '417-417'),
        Part('Учитель Илларион: "Отвернувшийся от Е. П. Б. не может стать искренне преданным представителю Ложи"',
            '418-418'),
        Part('Е.П. Блаватская. "Инструкции для учеников внутренней группы"',
            '419-419'),
        Part('Заметка редактора. От редакции: Она не предугадала! Она знала! В "Тайной доктрине" Е. П. Блаватская доказывает, что Махатмы Шамбалы, задолго до ХХ века, знали то, что стало затем потрясающими сенсациями современной цивилизации.',
             '420-420'),
        Part('Раи Б. К. Лахири: «И неужели людям Запада недостаточно, если гордый брахман, который никогда ни перед кем не склонял головы, кроме Высшего Существа, если он перед этой белой йогиней Запада складывает руки, как послушное дитя?',
            '421-421'),
        Part('1. Р. Корсон. «Тайная Доктрина» — книга на все времена. Она должна стать учебником будущего.',
            '422-422'),
        Part('Кемпбел Фер Планк: «Я никогда не видал ее...',
            '423-426'),
        Part('Рангампалли Джаганнатхья: «В три дня она расправилась с багажом атеистических теорий, накопленных мною за семь лет',
            '427-428'),
        Part('Джордж Мид: «Она была титаном среди смертных',
            '429-430'),
        Part('Джеймс Прайс: «Она была отлита в форму титанов. Она не принадлежала своему веку» К десятилетию выхода «Тайной Доктрины» (1898).',
            '431-434'),
        Part('«...взглянуть на старые учения новым взглядом». Строки из Учения Храма, IV т. («Естественная Жизнь»).',
            '435-436'),
        Part('Николай Рерих',
            '437-437'),
        Part('Дополнение: Из письма Махатмы Шамбалы, написанного в 1883 году: солнце — «это гигантский шар электромагнитных сил». Строки из книги «Чаша Востока» о том, чего современная наука еще не знает.',
            '438-438'),
        Part('Художник Эдмунд Рассел: «Она удерживала любовью — не страхом» «Она была раскаленным железным бруском, который уподобляется огню».',
            '439-445'),
        Part('О смерчах светлых и смерчах темных.’ 2. Ю. Долгин: «Настоящий труд будет оправдан частично или целиком в XX столетии»',
            '446-446'),
        Part('Елена Блаватская: «Если Теософское Общество сумеет устоять в течение этого периода, это будет прекрасно; если же нет, то теософия выйдет из него живой и невредимой...',
            '447-447'),
        Part('Расшифровка Знака Теософского Общества',
            '448-450'),
        Part('Два отзыва Уильяма Стэда:',
            '451-462'),
        Part('Нью-Йоркская газета «Tribune»: «...почти двадцать лет она посвятила распространению учений, фундаментальные принципы которых носят самый возвышенный этический характер»...',
            '463-463'),
        Part('Учитель Илларион: Без интуиции тайну чисел не раскрыть.',
            '464-465'),
        Part('Дополнение редакции: О том, чего еще наука не знает. ЕЛЕНА РЕРИХ — о планете Урусвати, приближающейся к Земле из космических далей. О Камне с Ориона. О таинственном металле Мории, который скоро будет открыт наукой... Несколько строк из Космологических записей.',
            '466-466'),
        Part('Уильям К. Джадж: «Навеки Ваша, Е.П.Б»',
            '467-468'),
        Part('Иван Харченко, советник-посланник, Генеральный консул СССР в Индии в 1962-1966 гг., 1970-1975 гг.',
            '469-475'),
        Part('Учитель Илларион: «Чистая душа стояла на берегу Океана проявленной жизни...»',
            '476-477'),
        Part('Учитель Кут Хуми: «...когда сознание людей воспримет новые идеи ...мир двинется вперед»',
            '478-496'),


        ],
        '359-360'
    ),
    ],
    [
    ],
    '~5-6')
pages_dictionary = {
    7: 'Страница 7. Письма Учителя Сераписа с предварительными Заметками редактора сборника Л. Дмитриевой о тайне "периода перехода" Елены Блаватской, совпавшего с ее вторым замужеством.',
    11: 'Страница 11. Заметки редактора, предваряющие письма Великого Гималайского Учителя Сераписа, адресованные Генри Олькотту летом 1875 года',
    47: 'Страница 47. В рай не попасть, если не победить Стража Порога.',
    52: 'Страница 52. Предупреждение Е.П. Блаватской всем эзотерикам',
    54: 'Страница 54. Из письма Учителя Кут Хуми - Ч. Ледбитеру',
    57: 'Страница 57. Философско-поэтический эскиз Ларисы Дмитриевой к одноименной картине Н. К. Рериха',
    65: 'Страница 65. Ученые провозгласили, что "век чудес прошел". Но Гималайский Учитель Кут Хуми утверждает, что такой век "никогда не существовал".',
    68: 'Страница 68. Пусть дети вспоминают из своей сокровищницы',
    70: 'Страница 70. Из книги Ларисы Дмитриевой "Посланник Утренней Звезды Христос и Его Учение в свете Сокровенного Учения Шамбалы"',
    80: 'Страница 80. Строки из Агни Йоги',
    96: 'Страница 96. 1 Перстень "сообщил": "Ее уже в земном мире нет"',
    98: 'Страница 98. 2. Краткая родословная Е. П. Блаватской.',
    103: 'Страница 103. О медиумах, медиаторах и психологических феноменах',
    119: 'Страница 119. Дополнение к предыдущему',
    131: 'Страница 131. Из письма Махатмы Кут Хуми - А. П. Спиннетту',
    134: 'Страница 134. Несколько слов из "Разоблаченной Изиды" (т I. Наука)',
    137: 'Страница 137. Интересное дополнение к вышеприведенному письму об одной встрече Е. П. Блаватской при ее прорыве на Тибет, о которой она рассказала в "Разоблаченной Изиде"',
    151: 'Страница 151. Снова о методе "осаждения"',
    176: 'Страница 176. Два воспоминания об одном и том же случае',
    190: 'Страница 190. Из воспоминаний полковника Г. Олькотта и А. Синнета об одном и том же феномене, свидетелями которого они стали.',
    208: 'Страница 208. Или - просто о скептицизме.',
    218: 'Страница 218. Строки из писем',
    227: 'Страница 227. Несколько самых разных чудес из великой книги.',
    273: 'Страница 273. Или Об Индийских мистических чарах.',
    292: 'Страница 292. и о других невероятных чудесах жителей Севенны',
    313: 'Страница 313. "А потом мы увидели, как... умирал Бетховен"',
    334: 'Страница 334. 1. Блаватская: Махатмы могут в астральном теле путешествовать в пространстве по континентам...',
    336: 'Страница 336. 2. Как найти Учителя?',
    348: 'Страница 348. Или Рассказ о чудном "воскрешении" внука махараджи Бэртпурского.',
    389: 'Страница 389. Глава из книги Ларисы Дмитриевой.',
    431: 'Страница 431. К десятилетию выхода «Тайной Доктрины» (1898)',
    435: 'Страница 435. Строки из Учения Храма, IV т. («Естественная Жизнь»)',
    438: 'Страница 438. Строки из книги «Чаша Востока» о том, его современная наука еще не знает',

    451: 'Страница 451. 1. «Госпожа Блаватская... заставила англо-индийцев поверить в ее миссию в самый разгар русофобии»',
    455: 'Страница 455. 2. «Не говорите мне о ее феноменах. Какое их значение, когда эта великая женщина, в наш век безверия, свершила феномен духовный, — феномен небывалый...»',
    466: 'Страница 466. Несколько строк из Космологических записей',

}