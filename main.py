import telebot
from telebot import types
import os

os.system('python filename.py')


bot = telebot.TeleBot("5456172758:AAGwQOy_GtNRjmCigMSEjCm1utWXG4Mewmc")

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
    if (message.text == "Как зарегистрироваться📝?"):
        bot.send_message(message.chat.id,text="Для регистрации на мероприятие необходимо открыть интересующее Вас мероприятие на сайте www.athletex.kz и ознакомиться с положением соревнований, После этого нажать внизу страницы кнопку (Зарегистрироваться). Далее открыть (корзину), и нажать кнопку (Оплатить)")


    elif (message.text == "Русский"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Магазин🧦👟🕶️")
        button2 = types.KeyboardButton("🏃Соревнования🏃")
        markup.add(button1, button2, )
        bot.send_message(message.chat.id, text="{0.first_name} Чем могу помочь? Выберите нужный пункт из меню".format(message.from_user),reply_markup=markup)

    elif (message.text == "Магазин🧦👟🕶️"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Магазин Athletex Shop")
        btn2 = types.KeyboardButton("Режим работы⏰")
        btn3 = types.KeyboardButton("Местоположение Athletex Shop🌍🔍")
        btn4 = types.KeyboardButton("Контакты☎")
        back = types.KeyboardButton("👈Вернуться назад")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="Информация по магазину", reply_markup=markup)

    elif (message.text == "🏃Соревнования🏃"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Календарь🗓")
        button2 = types.KeyboardButton("Регистрация")
        button3 = types.KeyboardButton("Результаты🏅")
        button4 = types.KeyboardButton("Партнерам")
        button5 = types.KeyboardButton("Стать волонтером")
        back = types.KeyboardButton("👈Вернуться назад")
        markup.add(button1, button2, button3, button4, button5, back)
        bot.send_message(message.chat.id, text="Информация по соревнованиям",reply_markup=markup)

    elif (message.text == "Стать волонтером"):
        bot.send_message(message.chat.id, "Хочешь быть полезным? ")
        bot.send_message(message.chat.id, "Влиться в спортивную тусовку? ")
        bot.send_message(message.chat.id, "Узнать всю кухню организации спортивных соревнований изнутри? ")
        bot.send_message(message.chat.id, "Чаще  выезжать на природу? ")
        bot.send_message(message.chat.id, "Получать слоты на соревнования не за деньги? ")
        bot.send_message(message.chat.id, "Участвовать даже если сам не можешь бежать?")
        bot.send_message(message.chat.id, "Да? Становись волонтером Экстремальной Атлетики!")
        bot.send_message(message.chat.id, "Тебя ждет: ")
        bot.send_message(message.chat.id, "Дружная позитивная команда; ")
        bot.send_message(message.chat.id, "Интересные и понятные задачи;")
        bot.send_message(message.chat.id, "Новые люди, интересные знакомства и новые места;")
        bot.send_message(message.chat.id, "и многое другое!")
        bot.send_message(message.chat.id, "Решился? Звони/пиши на номер: +77014100510,")
        bot.send_message(message.chat.id, "Следующее соревнование не за горами!")

    elif (message.text == "Партнерам"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти", url="https://athletex.kz/presentation/event.pdf ()"))
        bot.send_message(message.chat.id, text="Если Вы хотите стать нашими партнерами, свяжитесь с нами по  телефону", reply_markup=markup)
        bot.send_message(message.chat.id, text="+7 705 602 42 49")

    elif (message.text == "Регистрация"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton("Смена дистанции")
        btn3 = types.KeyboardButton("Проблема с регистрацией")
        btn4 = types.KeyboardButton("Проблема с оплатой?💰")
        btn5 = types.KeyboardButton("Не могу найти себя в списке участников")
        btn6 = types.KeyboardButton("Далее")
        back = types.KeyboardButton("👈Вернуться назад")
        markup.add(button2, btn3, btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="Помощь по регистрации",reply_markup=markup)

    elif (message.text == "Проблема с оплатой?💰"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Карта Казахстанского банка💳")
        button2 = types.KeyboardButton("Карта НЕ Казахстанского банка💳")
        back = types.KeyboardButton("👈Вернуться назад")
        markup.add(button1, button2, back)
        bot.send_message(message.chat.id, text="Помощь по оплате", reply_markup=markup)

    elif (message.text == "Далее"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Отмена участия")
        btn2 = types.KeyboardButton("Трансфер")
        btn3 = types.KeyboardButton("НЕ нашли ответа?")
        back = types.KeyboardButton("👈Вернуться назад")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="👉", reply_markup=markup)

    elif (message.text == "Трансфер"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как узнать место и время отправления автобуса?")
        btn2 = types.KeyboardButton("Как купить трансфер?")
        btn3 = types.KeyboardButton("Нет ваучера в личном кабинете.")
        btn4 = types.KeyboardButton("Как купить трансфер на нескольких людей?")
        btn5 = types.KeyboardButton("Отмена трансфера")
        btn6 = types.KeyboardButton("Перерегистрация трансфера на другого человека")
        back = types.KeyboardButton("👈 Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="🚌", reply_markup=markup)

    elif (message.text == "👈 Назад"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Отмена участия")
        btn2 = types.KeyboardButton("Трансфер")
        btn3 = types.KeyboardButton("НЕ нашли ответа?")
        back = types.KeyboardButton("👈Вернуться назад")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="👉", reply_markup=markup)

    elif (message.text == "Контакты☎"):
        bot.send_message(message.chat.id,"+7 777 312 36 29")

    elif (message.text == "Не могу найти себя в списке участников"):
        bot.send_message(message.chat.id, "В начале списка есть строка поиска - пожалуйста воспользуйтесь ей, чтобы найти свою фамилию.")
        bot.send_message(message.chat.id, "Не забудьте, что Ваша фамилия отображается именно так, как вы написали ее в разделе ПЕРОНАЛЬНЫЕ ДАННЫЕ (на русском или английском языке)")
        bot.send_message(message.chat.id, "В строку поиска не обязательно вводить и фамилию и имя - фамилии будет достаточно")
        bot.send_message(message.chat.id, "Проверьте, прошла ли оплата за регистрацию? Без оплаты регистрация считается незавершенной.")
        bot.send_message(message.chat.id, "У каждого участника должен быть свой аккаунт - убедитесь, что тот, кого вы ищите в списке, зарегистрирован со своего аккаунта.")

    elif (message.text == "Отмена участия"):
        bot.send_message(message.chat.id, "Вопрос об отмене участия зависит от правил конкретного соревнования - пожалуйста, проверьте информацию об этом в положении на страничке соревнования.")

    elif (message.text == "Перерегистрация трансфера на другого человека"):
        bot.send_message(message.chat.id, "Этот вопрос решается в индивидуальном порядке и зависит от правил конкретного соревнования. Проверьте информацию об этом в положении соревнования и напишите нам на почту (tengriultra@gmail.com)")

    elif (message.text == "Отмена трансфера"):
        bot.send_message(message.chat.id, "Пожалуйста, проверьте в положении (оно находится на странице соревнования) правила по поводу отмены трансфера. Если там Вы не нашли информации, напишите нам на почту (tengriultra@gmail.com)")

    elif (message.text == "Как купить трансфер на нескольких людей?"):
        bot.send_message(message.chat.id,"К сожалению, на данный момент нет технической возможности купить трансфер одновременно на несколько человек. Но если это позволяют правила ( см. положение на странице соревнования), вы можете купить несколько трансферов поочередно.")

    elif (message.text == "Нет ваучера в личном кабинете."):
        bot.send_message(message.chat.id,"Напишите нам на почту (tengriultra@gmail.com).")

    elif (message.text == "Как купить трансфер?"):
        bot.send_message(message.chat.id,"Чтобы купить трансфер отдельно от участия, Вам нужно зайти на страницу нужного соревнования, нажать Кнопку [участвовать]. Перейти в корзину, выбрать в графе дистанции [не участвую или оплатил участие ранее], а в следующей графе выбрать трансфер. Внизу появится стоимость только трансфера. Нажимаете [оформить заказ] и оплачиваете.После оплаты Вы найдете билет на трансфер  в личном кабинете, в разделе [аккаунт-сводка] - [мои покупки].")

    elif (message.text == "Как узнать место и время отправления автобуса?"):
        bot.send_message(message.chat.id,"Время и место отправления указаны в вашем ваучере")

    elif (message.text == "Перерегистрация📝"):
        bot.send_message(message.chat.id, "Для перерегистраци с одного участника на другого, напишите нам на почту (tengriultra@gmail.com)")

    elif (message.text == "Забыл пароль"):
        bot.send_message(message.chat.id, "Нажмите кнопку [ЗАБЫЛИ ПАРОЛЬ], после чего введите свой e-mail на который у вас зарегистрирован личный кабинет, и нажмите кнопку [OK]. После этого Вам на указанную почту придет письмо с кнопкой восстановления пароля [Reset password]. Нажмите эту кнопку. У вас откроется окно,куда нужно ввести почту и новый пароль(два раза). Запомните этот пароль и используйте для последующего входа в свой аккаунт.")

    elif (message.text == "Создать личный кабинет"):
        bot.send_message(message.chat.id, "Чтобы создать свой аккаунт на этом сайте, Вы: Нажимаете на иконку черной головы справа сверху - [создать личный кабинет]")
        bot.send_message(message.chat.id, "Заполняете все поля и нажимаете зарегистрироваться.")
        bot.send_message(message.chat.id, "После этого переходите в раздел (персональная информация) и заполняете еще несколько полей. ")
        bot.send_message(message.chat.id, "Их немного, и они очень важны для правильного отображения информации о Вас в финишном протоколе.")

    elif (message.text == "Как зарегистрироваться"):
        bot.send_message(message.chat.id, "Чтобы зарегистрироваться:")
        bot.send_message(message.chat.id, "Нажмите две полоски слева сверху.")
        bot.send_message(message.chat.id, "Нажмите на [наши события] - выберете нужное соревнование - нажмите [участвовать].")
        bot.send_message(message.chat.id, "Участие уже в вашей корзине! (Значок справа сверху). Нажмите на нее. ")
        bot.send_message(message.chat.id, "Осталось лишь выбрать дистанцию и нажать [оформить заказ].")
        bot.send_message(message.chat.id, "Поле «Выбрать клуб» - необязательное к заполнению! Вы можете его пропустить.")

    elif (message.text == "НЕ нашли ответа?"):
        bot.send_message(message.chat.id, "Напишите нам на (tengriultra@gmail.com)")
        bot.send_message(message.chat.id, "Мы ответим Вам в ближайшее время")

    elif (message.text == "Проблема с регистрацией"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Забыл пароль")
        button2 = types.KeyboardButton("Создать личный кабинет")
        button3 = types.KeyboardButton("Как зарегистрироваться")
        button4 = types.KeyboardButton("Успешно ли я зарегистрировался?")
        back = types.KeyboardButton("👈Вернуться назад")
        markup.add(button1, button2, button3, button4, back)
        bot.send_message(message.chat.id, text="Помощь по регистрации",reply_markup=markup)

    elif (message.text == "Карта НЕ Казахстанского банка💳"):
        bot.send_message(message.chat.id, "Если при оплате выходит ошибка, для решения этой проблемы пожалуйста, свяжитесь с нами по почте (tengriultra@gmail.com)")

    elif (message.text == "Карта Казахстанского банка💳"):
        bot.send_message(message.chat.id, "Пожалуйста, проверьте, нет ли у вас лимитов на интернет покупки или иных проблем, связанных с банком")

    elif (message.text == "Смена дистанции"):
        bot.send_message(message.chat.id, "После того как Вы зашли в аккаунт, нажмите кружок аватара справа сверху и нажмите на раздел (Аккаунт-сводка). В разделе Я УЧАСТВУЮ справа от соревнования Вы увидите кнопку ИЗМЕНИТЬ. Нажмите на неё, после чего выберите новую нужную Вам дистанцию и нажмите оплатить. Напоминаем что за любое изменение в уже оплаченной регистрации берется сервисный сбор 2000 тенге. Также, если Вы выбираете более дорогую дистанцию, Вам нужно будет доплатить разницу между стоимостью бывшей и нынешней (она рассчитывается автоматически). Если же дистанция более дешевая, разница в цене не учитывается и не возвращается. ")
        bot.send_message(message.chat.id, "Изменение возможно только при наличии свободных слотов на нужную вам дистанцию.")
        bot.send_message(message.chat.id, "После оплаты обязательно проверьте вашу дистанцию в списке участников на странице соревнования. Если она по какой-то причине не поменялась, свяжитесь с нами по почте tengriultra@gmail.com")

    elif (message.text == "Результаты🏅"):
        bot.send_message(message.chat.id, "Зайдите на страницу уже завершенного соревнования и прокрутите её вниз до конца - там вы увидите большую красную кнопку [РЕЗУЛЬТАТЫ]. После нажатия Вас перенаправит на страницу финишного протокола.")

    elif (message.text == "Магазин Athletex Shop"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://athletex.kz/shop"))
        bot.send_message(message.chat.id, text="Магазин спорт товаров Athletex Shop",reply_markup=markup)

    elif (message.text == "Календарь🗓"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://athletex.kz/competitions"))
        bot.send_message(message.chat.id, text="Календарь событий", reply_markup=markup)

    elif (message.text == "Местоположение Athletex Shop🌍🔍"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("2Gis", url="https://2gis.kz/almaty/firm/70000001032749432"))
        bot.send_message(message.chat.id, text="Местоположение", reply_markup=markup)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Яндекс Карты", url="https://yandex.kz/maps/162/almaty/house/Y08Yfg9gT0YDQFppfX51cX1gZg==/?ll=76.880633%2C43.240132&z=17"))
        bot.send_message(message.chat.id, text="Местоположение", reply_markup=markup)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Google maps", url="https://www.google.com/maps/place/%D1%83%D0%BB%D0%B8%D1%86%D0%B0+%D0%A2%D1%83%D1%80%D0%BA%D0%B5%D0%B1%D0%B0%D0%B5%D0%B2%D0%B0+208,+%D0%90%D0%BB%D0%BC%D0%B0%D1%82%D1%8B+050000/@43.2400987,76.8783921,17z/data=!3m1!4b1!4m5!3m4!1s0x388369c5170d5c33:0x40192730afc01c6d!8m2!3d43.2400987!4d76.8805808?shorturl=1"))
        bot.send_message(message.chat.id, text="Местоположение", reply_markup=markup)

    elif (message.text == "Режим работы⏰"):
        photo = open('img2.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "Пожалуйста, заранее узнавайте часы работы магазина в выходные и праздничные дни.")

    elif(message.text == "Успешно ли я зарегистрировался?"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CallCenter, Колл Центр", url="https://web.telegram.org/z/#677006359"))
        bot.send_message(message.chat.id, text="Проверьте свою фамилию в списке участников на страничке соревнования на athletex.kz Если Вы себя нашли - это значит регистрация прошла успешно. Если нет, то регистрация не завершена, обратитесь к консультанту по номеру +77056024249 (рус, eng) +77767373667 (рус, каз)", reply_markup=markup)
        bot.send_message(message.chat.id, "( звонок/ ватсап/ телеграмм )")

    elif (message.text == "👈Вернуться назад"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Магазин🧦👟🕶️")
        button2 = types.KeyboardButton("🏃Соревнования🏃")
        markup.add(button1, button2, )
        bot.send_message(message.chat.id, text="{0.first_name}! Чем могу помочь?".format(message.from_user),reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Пожалуйста выберите существующий раздел, в меню кнопок")

while True:
    try:
        bot.polling(none_stop=True)
    except:
        continue