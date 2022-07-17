import telebot
from telebot import types

bot = telebot.TeleBot("5302098913:AAHXMROYNHDlU7YMFBpxPIpm97TVuFGZkrc")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Русский")
    button2 = types.KeyboardButton("Казахский")
    markup.add(button1, button2,)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Выбери язык".format(message.from_user) ,reply_markup=markup)
    bot.send_message(message.chat.id, text="Сәлем {0.first_name}! Тіліңізді таңдаңыз".format(message.from_user) ,reply_markup=markup)
    bot.send_message(message.chat.id, text="Hello {0.first_name}! Choose your language".format(message.from_user) ,reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Қалай тіркелуге болады📝?"):
        bot.send_message(message.chat.id,text="Для регистрации на мероприятие необходимо открыть интересующее Вас мероприятие на сайте www.athletex.kz и ознакомиться с положением соревнований, После этого нажать внизу страницы кнопку (Зарегистрироваться). Далее открыть (корзину), и нажать кнопку (Оплатить)")


    elif (message.text == "Казахский"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Дүкен🧦👟🕶️")
        button2 = types.KeyboardButton("🏃Жарыстар🏃")
        markup.add(button1, button2, )
        bot.send_message(message.chat.id,text="{0.first_name} Сізге қандай көмек көрсете аламын? Мәзірден қажетті элементті таңдаңыз".format(message.from_user), reply_markup=markup)

    elif (message.text == "Дүкен🧦👟🕶️"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Дүкен Athletex Shop")
        btn2 = types.KeyboardButton("Жұмыс уақыты⏰")
        btn3 = types.KeyboardButton("Орналасқан жері🌍🔍")
        btn4 = types.KeyboardButton("Байланыстар☎")
        back = types.KeyboardButton("👈Артқа оралу")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="Дүкен ақпараты", reply_markup=markup)

    elif (message.text == "🏃Жарыстар🏃"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Күнтізбе🗓")
        button2 = types.KeyboardButton("Тіркелу")
        button3 = types.KeyboardButton("Нәтижелер🏅")
        button4 = types.KeyboardButton("Серіктестер үшін")
        button5 = types.KeyboardButton("Еріктілер қатарына қосылу")
        back = types.KeyboardButton("👈Артқа оралу")
        markup.add(button1, button2, button3, button4, button5, back)
        bot.send_message(message.chat.id, text="Информация по соревнованиям", reply_markup=markup)

    elif (message.text == "Еріктілер қатарына қосылу"):
        bot.send_message(message.chat.id, "Сіз пайдалы болғыңыз келе ме? ")
        bot.send_message(message.chat.id, "Спорттық кешке қатысқыңыз келе ме? ")
        bot.send_message(message.chat.id, "Барлығын іштей білгіңіз келе ме? ")
        bot.send_message(message.chat.id, "Табиғатқа жиі шығасыз ба? ")
        bot.send_message(message.chat.id, "Жарыстарға арналған слоттарды ақшасыз алғыңыз келе ме? ")
        bot.send_message(message.chat.id, "Өзіңіз жүгірмесеңіз де, біздің жарыстарға қызығасыз ба?")
        bot.send_message(message.chat.id, "Солай ма? Онда болса Экстремаллды Атлетиканың  еріктісі болыңыз!")
        bot.send_message(message.chat.id, "Сізді: ")
        bot.send_message(message.chat.id, "Тату әрі позитивті команда; ")
        bot.send_message(message.chat.id, "Қызықты және түсінікті тапсырмалар;")
        bot.send_message(message.chat.id, "Жаңа адамдар, қызықты танысулар және жаңа орындар;")
        bot.send_message(message.chat.id, "және тағы басқа қызықты сәттер күтіп тұр!")
        bot.send_message(message.chat.id, "Шешім қабылдасаңыз, онда  +77014100510 нөміріне қоңырау шалыңыз / жазыңыз,")
        bot.send_message(message.chat.id, "Келесі жарыс жақындап қалды!")

    elif (message.text == "Серіктестер үшін"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти", url="https://athletex.kz/presentation/event.pdf ()"))
        bot.send_message(message.chat.id, text="Если Вы хотите стать нашими партнерами, свяжитесь с нами по  телефону",
                         reply_markup=markup)
        bot.send_message(message.chat.id, text="+7 705 602 42 49")

    elif (message.text == "Тіркелу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton("Қашықтықты ауыстыру")
        btn3 = types.KeyboardButton("Тіркелу мәселесі")
        btn4 = types.KeyboardButton("Төлем мәселесі?💰")
        btn5 = types.KeyboardButton("Қатысушылар тізімінен өзімді таба алмай жатырмын")
        btn6 = types.KeyboardButton("Ары қарай")
        back = types.KeyboardButton("👈Артқа оралу")
        markup.add(button2, btn3, btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="Тіркелу бойынша көмек", reply_markup=markup)

    elif (message.text == "Төлем мәселесі?💰"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(" Төлем картасы Қазақстан банкінің картасы💳")
        button2 = types.KeyboardButton(" Төлем картасы Қазақстан банкінің картасы емес💳")
        back = types.KeyboardButton("👈Артқа оралу")
        markup.add(button1, button2, back)
        bot.send_message(message.chat.id, text="Помощь по оплате", reply_markup=markup)

    elif (message.text == "Ары қарай"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Қатысудан бас тарту")
        btn2 = types.KeyboardButton("Трансфер")
        btn3 = types.KeyboardButton("Қажетті жауап табылмады")
        back = types.KeyboardButton("👈Артқа оралу")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="👉", reply_markup=markup)

    elif (message.text == "Трансфер"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Автобустың жөнелтілетін орны мен уақытын қалай білуге ​​болады?")
        btn2 = types.KeyboardButton("Трансферді қалай сатып алуға болады?")
        btn3 = types.KeyboardButton("Жеке кабинетте ваучер жоқ")
        btn4 = types.KeyboardButton("Бірнеше адамға трансферді қалай сатып алуға болады?")
        btn5 = types.KeyboardButton("Трансферден бас тарту")
        btn6 = types.KeyboardButton("Трансферді басқа адамға аудару ")
        back = types.KeyboardButton("👈 Aртқа")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="🚌", reply_markup=markup)

    elif (message.text == "👈 Aртқа"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Қатысудан бас тарту")
        btn2 = types.KeyboardButton("Трансфер")
        btn3 = types.KeyboardButton("Қажетті жауап табылмады")
        back = types.KeyboardButton("👈Артқа оралу")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="👉", reply_markup=markup)

    elif (message.text == "Байланыстар☎"):
        bot.send_message(message.chat.id, "+7 777 312 36 29")

    elif (message.text == "Қатысушылар тізімінен өзімді таба алмай жатырмын"):
        bot.send_message(message.chat.id,"Тізімнің жоғарғы жағында іздеу жолағы бар - оны фамилияңызды табу үшін пайдаланыңыз.")
        bot.send_message(message.chat.id,"Сіздің тегіңіз ЖЕКЕ ДЕРЕКТЕР бөлімінде (орыс немесе ағылшын тілінде) жазғаныңыздай дәл көрсетілетінін ұмытпаңыз.)")
        bot.send_message(message.chat.id,"Іздеу жолағында фамилияны да, атын да енгізу қажет емес - тегі жеткілікті болады")
        bot.send_message(message.chat.id,"Тіркеу төлемінің өткенін тексеріңіз. Төлемсіз тіркеу аяқталмаған болып саналады")
        bot.send_message(message.chat.id," Әрбір қатысушының жеке аккаунты болуы керек - тізімде Cіз іздеген адам өз аккаунтында тіркелгеніне көз жеткізіңіз.")

    elif (message.text == "Қатысудан бас тарту"):
        bot.send_message(message.chat.id,"Қатысудан бас тарту белгілі бір конкурстың ережелеріне байланысты - бұл туралы ақпаратты жарыс туралы ережеден қараңыз.")

    elif (message.text == "Трансферді басқа адамға аудару"):
        bot.send_message(message.chat.id,"Бұл мәселе жеке негізде шешіледі және белгілі бір жарыстың ережелеріне байланысты. Бұл туралы ақпаратты жарыстың ережесінен қарап, бізге пошта арқылы жазыңыз (tengriultra@gmail.com).")

    elif (message.text == "Трансферден бас тарту"):
        bot.send_message(message.chat.id,"Жарыс туралы ережеде (ол жарыс бетінде) трансферден бас тарту тәртібін  қараңыз. Егер Сіз ол жерден ақпаратты таба алмасаңыз, бізге пошта арқылы жазыңыз (tengriultra@gmail.com).")

    elif (message.text == "Бірнеше адамға трансферді қалай сатып алуға болады?"):
        bot.send_message(message.chat.id,"Өкінішке орай, қазіргі уақытта бірыңғай бірнеше адамға трансферді сатып алуға техникалық мүмкіндік жоқ. Бірақ егер ережелер рұқсат етсе (жарыс бетіндегі ережені қараңыз), Сіз кезекпен бірнеше трансферді сатып ала аласыз.»")

    elif (message.text == "Жеке кабинетте ваучер жоқ."):
        bot.send_message(message.chat.id, "Біздің электрондық поштамызға жазыңыз (tengriultra@gmail.com).")

    elif (message.text == "Трансферді қалай сатып алуға болады?"):
        bot.send_message(message.chat.id,"Қатысудан тыс трансферді сатып алу үшін Сіз қалаған жарыстың бетіне өтуіңіз керек, содан соң [қатысу] түймесін басыңыз. Себетке өтіп, қашықтық бағанында [Мен қатыспаймын немесе қатысу үшін бұрын төледім] таңдаңыз, ал келесі бағанда трансферді таңдаңыз. Төменде тек трансфер құны көрсетіледі. [тапсырысты рәсімдеу] түймесін басып, төлеңіз. Төлем өткеннен кейін Сіз өзіңіздің жеке кабинетіңізде [аккаунт ақпары] - [менің сатып алуларым] бөлімінде трансфер билетін табасыз.")

    elif (message.text == "Автобустың жөнелтілетін орны мен уақытын қалай білуге ​​болады?"):
        bot.send_message(message.chat.id, "Кету уақыты мен орны Сіздің ваучеріңізде көрсетілген")

    elif (message.text == "Қайта тіркелу 📝"):
        bot.send_message(message.chat.id,"Бір қатысушыдан екінші қатысушыға қайта тіркелу үшін бізге пошта арқылы жазыңыз (tengriultra@gmail.com)")

    elif (message.text == "Құпия сөзді ұмыттым"):
        bot.send_message(message.chat.id," [ҚҰПИЯ СӨЗДІ ҰМЫТТЫМ] түймесін басыңыз, содан кейін жеке кабинетіңіз тіркелген электрондық поштаңызды енгізіңіз де, [OK] түймесін басыңыз. Осыдан кейін Сіз көрсетілген электрондық поштаңызға  құпия сөзді қалпына келтіру түймесі бар [Құпия сөзді қалпына келтіру] электрондық хат аласыз. Осы түймені басыңыз. Электрондық поштаңызды және жаңа құпия сөзді (екі рет) енгізуіңіз керек терезе ашылады. Бұл құпия сөзді есте сақтаңыз және оны кейінірек жеке кабинетіңізге кіру үшін пайдаланыңыз.")

    elif (message.text == "Жеке кабинет ашу"):
        bot.send_message(message.chat.id,"Осы сайтта жеке аккаунтыңызды ашу үшін сіз: жоғарғы оң жақтағы қара бас белгішесін басыңыз - [Жеке кабинет ашу]")
        bot.send_message(message.chat.id, "Барлық орындарды толтырып, тіркеу түймесін басыңыз.")
        bot.send_message(message.chat.id,"Осыдан кейін (жеке ақпарат)  бөліміне өтіп, тағы бірнеше орындарды толтырыңыз. ")
        bot.send_message(message.chat.id,"Толтырылуы керек ақпарат көп емес және олар мәре хаттамасында сіз туралы ақпаратты дұрыс көрсету үшін өте маңызды.")

    elif (message.text == "Қалай тіркелуге болады"):
        bot.send_message(message.chat.id, "Тіркелу үшін:")
        bot.send_message(message.chat.id, "Жоғарғы сол жақтағы екі жолақты басыңыз.")
        bot.send_message(message.chat.id,"[Біздің оқиғалар] түймесін басыңыз - қажетті жарысты таңдаңыз - [қатысу] түймесін басыңыз.")
        bot.send_message(message.chat.id, "Қатысу себетіңізде бар! (Жоғарғы оң жақ белгіше). Соны басыңыз. ")
        bot.send_message(message.chat.id, "Қашықтықты таңдап, [тапсырысты рәсімдеу] түймесін басу ғана қалады.")
        bot.send_message(message.chat.id, "«Клубты таңдау» өрісі міндетті емес! Оны өткізіп жіберуге болады.")

    elif (message.text == "Қажетті жауап табылмады"):
        bot.send_message(message.chat.id, "Біздің (tengriultra@gmail.com) электрондық поштамызға жазыңыз")
        bot.send_message(message.chat.id, "Біз Сізге мүмкіндігінше тезірек жауап береміз")

    elif (message.text == "Тіркелу мәселесі"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Құпия сөзді ұмыттым")
        button2 = types.KeyboardButton("Жеке кабинет ашу")
        button3 = types.KeyboardButton("Қалай тіркелуге болады")
        button4 = types.KeyboardButton("Тіркелуім сәтті өтті ме?")
        back = types.KeyboardButton("👈Артқа оралу")
        markup.add(button1, button2, button3, button4, back)
        bot.send_message(message.chat.id, text="Тіркелу бойынша көмек", reply_markup=markup)

    elif (message.text == " Төлем картасы Қазақстан банкінің картасы емес💳"):
        bot.send_message(message.chat.id,"Төлем кезінде қате орын алса, бұл мәселені шешу үшін бізге пошта арқылы хабарласыңыз (tengriultra@gmail.com)")

    elif (message.text == " Төлем картасы Қазақстан банкінің картасы💳"):
        bot.send_message(message.chat.id,"Сізде онлайн сатып алу шектеулері немесе банкке қатысты басқа мәселелер бар-жоғын тексеріңіз")

    elif (message.text == "Қашықтықты ауыстыру"):
        bot.send_message(message.chat.id,"Аккаунтыңызға кіргеннен кейін жоғарғы оң жақтағы аватар шеңберін басыңыз және (Аккаунт ақпары) бөліміне кіріңіз. Жарыстың оң жағындағы МЕН ҚАТЫСАМЫН бөлімінде ӨЗГЕРТУ түймесін көресіз. Оны басыңыз, содан кейін сізге қажетті жаңа қашықтықты таңдап, төлеу түймесін басыңыз. Естеріңізге сала кетейік, қазірдің өзінде төленген тіркеуді өзгерту үшін 2000 теңге қызмет ақысы алынады. Сондай-ақ, егер сіз қымбатырақ қашықтықты таңдасаңыз, бұрынғы мен ағымдағы құны арасындағы айырмашылықты төлеуіңіз керек (ол автоматты түрде есептеледі). Егер қашықтық арзанырақ болса, баға айырмашылығы есепке алынбайды және қайтарылмайды.")
        bot.send_message(message.chat.id, "Қажетті қашықтыққа бос слоттар болған жағдайда ғана өзгерту мүмкін болады.")
        bot.send_message(message.chat.id,"Төлегеннен кейін жарыс бетіндегі қатысушылар тізімінен қашықтықты тексеріңіз. Егер қандай да бір себептермен ол өзгермесе, бізге tengriultra@gmail.com поштасы арқылы хабарласыңыз ")

    elif (message.text == "Нәтижелер🏅"):
        bot.send_message(message.chat.id,"Зайдите на страницу уже завершенного соревнования и прокрутите её вниз до конца - там вы увидите большую красную кнопку [РЕЗУЛЬТАТЫ]. После нажатия Вас перенаправит на страницу финишного протокола.")

    elif (message.text == "Дүкен Athletex Shop"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://athletex.kz/shop"))
        bot.send_message(message.chat.id, text="Магазин спорт товаров Athletex Shop", reply_markup=markup)

    elif (message.text == "Күнтізбе🗓"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Сайтқа өтіңіз", url="https://athletex.kz/competitions"))
        bot.send_message(message.chat.id, text="оқиғалар күнтізбесі", reply_markup=markup)

    elif (message.text == "Орналасқан жері🌍🔍"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("2Gis", url="https://2gis.kz/almaty/firm/70000001032749432"))
        bot.send_message(message.chat.id, text="Орналасқан жері", reply_markup=markup)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Яндекс Карты",url="https://yandex.kz/maps/162/almaty/house/Y08Yfg9gT0YDQFppfX51cX1gZg==/?ll=76.880633%2C43.240132&z=17"))
        bot.send_message(message.chat.id, text="Орналасқан жері", reply_markup=markup)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Google maps",url="https://www.google.com/maps/place/%D1%83%D0%BB%D0%B8%D1%86%D0%B0+%D0%A2%D1%83%D1%80%D0%BA%D0%B5%D0%B1%D0%B0%D0%B5%D0%B2%D0%B0+208,+%D0%90%D0%BB%D0%BC%D0%B0%D1%82%D1%8B+050000/@43.2400987,76.8783921,17z/data=!3m1!4b1!4m5!3m4!1s0x388369c5170d5c33:0x40192730afc01c6d!8m2!3d43.2400987!4d76.8805808?shorturl=1"))
        bot.send_message(message.chat.id, text="Орналасқан жері", reply_markup=markup)

    elif (message.text == "Жұмыс уақыты⏰"):
        photo = open('img2.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,"Пожалуйста, заранее узнавайте часы работы магазина в выходные и праздничные дни.")

    elif (message.text == "Тіркелуім сәтті өтті ме?"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CallCenter, Колл Центр", url="https://web.telegram.org/z/#677006359"))
        bot.send_message(message.chat.id,text="Проверьте свою фамилию в списке участников на страничке соревнования на athletex.kz Если Вы себя нашли - это значит регистрация прошла успешно. Если нет, то регистрация не завершена, обратитесь к консультанту по номеру +77056024249 (рус, eng) +77767373667 (рус, каз)",reply_markup=markup)
        bot.send_message(message.chat.id, "( звонок/ ватсап/ телеграмм )")

    elif (message.text == "👈Артқа оралу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Дүкен🧦👟🕶️")
        button2 = types.KeyboardButton("🏃Жарыстар🏃")
        markup.add(button1, button2, )
        bot.send_message(message.chat.id, text="{0.first_name}Выберите нужный пункт из меню".format(message.from_user),reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Түйме мәзірінен бар бөлімді таңдаңыз  ")


while True:
    try:
        bot.polling(none_stop=True)
    except:
        continue
