import time

import telebot
from telebot import types
import tg_analytic

bot = telebot.TeleBot("5456172758:AAGwQOy_GtNRjmCigMSEjCm1utWXG4Mewmc")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Русский")
    button2 = types.KeyboardButton("Казахский")
    button3 = types.KeyboardButton("English")
    markup.add(button1, button2, button3, )
    tg_analytic.statistics(message.chat.id, message.text)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Выбери язык".format(message.from_user) ,reply_markup=markup)
    bot.send_message(message.chat.id, text="Сәлем {0.first_name}! Тіліңізді таңдаңыз".format(message.from_user) ,reply_markup=markup)
    bot.send_message(message.chat.id, text="Hello {0.first_name}! Choose your language".format(message.from_user) ,reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == ""):
        bot.send_message(message.chat.id,text="")

    elif (message.text == "Как зарегистрироваться📝?"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Текст")
        button2 = types.KeyboardButton("Видео")
        button3 = types.KeyboardButton("👈Назад")
        markup.add(button1, button2, button3, )
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id, text="{0.first_name} Выберите что для вас будет удобнее".format(message.from_user),reply_markup=markup)

    elif (message.text == "👈Назад"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Забыл пароль")
        button2 = types.KeyboardButton("Создать личный кабинет")
        button3 = types.KeyboardButton("Как зарегистрироваться📝?")
        button4 = types.KeyboardButton("Успешно ли я зарегистрировался?")
        back = types.KeyboardButton("👈Вернуться назад")
        markup.add(button1, button2, button3, button4, back)
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id, text="Помощь по регистрации",reply_markup=markup)

    elif (message.text == "Видеo"):
        with open ('Video1.mp4', 'rb') as f1:
         bot.send_video(message.chat.id, f1)

    elif (message.text == "Создать личный кабинет"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Текcт")
        button2 = types.KeyboardButton("Видеo")
        button3 = types.KeyboardButton("👈Назад")
        markup.add(button1, button2, button3, )
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id,text="{0.first_name} Выберите что для вас будет удобнее".format(message.from_user),reply_markup=markup)

    elif (message.text == "Videо"):
        with open ('Video1.mp4', 'rb') as f1:
         bot.send_video(message.chat.id, f1)

    elif (message.text == "Create a personal account"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Тext")
        button2 = types.KeyboardButton("Videо")
        button3 = types.KeyboardButton("👈Skip")
        markup.add(button1, button2, button3, )
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id,text="{0.first_name} Выберите что для вас будет удобнее".format(message.from_user),reply_markup=markup)


    elif (message.text == "Текст"):
        bot.send_message(message.chat.id,"Для регистрации на мероприятие необходимо открыть интересующее Вас мероприятие на сайте www.athletex.kz и ознакомиться с положением соревнований, После этого нажать внизу страницы кнопку (Зарегистрироваться). Далее открыть (корзину), и нажать кнопку (Оплатить)")

    elif (message.text == "Видео"):
        with open('video.mp4', 'rb') as f1:
         bot.send_video(message.chat.id, f1)

    elif (message.text == "Video"):
        with open('video.mp4', 'rb') as f1:
         bot.send_video(message.chat.id, f1)

    elif (message.text == "How to register📝?"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Text")
        button2 = types.KeyboardButton("Video")
        button3 = types.KeyboardButton("👈Skip")
        markup.add(button1, button2, button3, )
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id, text="{0.first_name}".format(message.from_user),reply_markup=markup)

    elif (message.text == "👈Skip"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Forgot my password")
        button2 = types.KeyboardButton("Create a personal account")
        button3 = types.KeyboardButton("How to register📝?")
        button4 = types.KeyboardButton("Have I successfully registered?")
        back = types.KeyboardButton("👈Back")
        markup.add(button1, button2, button3, button4, back)
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id, text="Registration assistance", reply_markup=markup)

    elif (message.text == "Бейне"):
        with open('video.mp4', 'rb') as f1:
         bot.send_video(message.chat.id, f1)

    elif (message.text == "Қалай тіркелуге болады📝?"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Мәтін")
        button2 = types.KeyboardButton("Бейне")
        button3 = types.KeyboardButton("👈  Артқа")
        markup.add(button1, button2, button3, )
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id, text="{0.first_name} Сізге не ыңғайлы екенін таңдаңыз".format(message.from_user),reply_markup=markup)

    elif (message.text == "👈  Артқа"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Құпия сөзді ұмыттым")
        button2 = types.KeyboardButton("Жеке кабинет ашу")
        button3 = types.KeyboardButton("Қалай тіркелуге болады📝?")
        button4 = types.KeyboardButton("Тіркелуім сәтті өтті ме?")
        back = types.KeyboardButton("👈Артқа оралу")
        markup.add(button1, button2, button3, button4, back)
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id, text="Тіркелу бойынша көмек", reply_markup=markup)

    elif (message.text == "Русский"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Магазин🧦👟🕶️")
        button2 = types.KeyboardButton("🏃Соревнования🏃")
        markup.add(button1, button2, )
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id, text="{0.first_name} Чем могу помочь? Выберите нужный пункт из меню".format(message.from_user),reply_markup=markup)

    elif (message.text == "Магазин🧦👟🕶️"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Магазин Athletex Shop")
        btn2 = types.KeyboardButton("Режим работы⏰")
        btn3 = types.KeyboardButton("Местоположение Athletex Shop🌍🔍")
        btn4 = types.KeyboardButton("Контакты☎")
        back = types.KeyboardButton("👈Вернуться назад")
        markup.add(btn1, btn2, btn3, btn4, back)
        tg_analytic.statistics(message.chat.id, message.text)
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
        tg_analytic.statistics(message.chat.id, message.text)
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
        btn6 = types.KeyboardButton("Перерегистрация📝")
        btn7 = types.KeyboardButton("Далее")
        back = types.KeyboardButton("👈Вернуться назад")
        markup.add(button2, btn3, btn4, btn5, btn6, btn7, back)
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id, text="Помощь по регистрации",reply_markup=markup)

    elif (message.text == "Bидео"):
        with open('IMG_6934.MP4', 'rb') as f1:
         bot.send_video(message.chat.id, f1)

    elif (message.text == "Перерегистрация📝"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Teкcт")
        button2 = types.KeyboardButton("Bидео")
        button3 = types.KeyboardButton("👈Назaд")
        markup.add(button1, button2, button3, )
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id,text="{0.first_name} Выберите что для вас будет удобнее".format(message.from_user),reply_markup=markup)

    elif (message.text == "👈Назaд"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton("Смена дистанции")
        btn3 = types.KeyboardButton("Проблема с регистрацией")
        btn4 = types.KeyboardButton("Проблема с оплатой?💰")
        btn5 = types.KeyboardButton("Не могу найти себя в списке участников")
        btn6 = types.KeyboardButton("Перерегистрация📝")
        btn7 = types.KeyboardButton("Далее")
        back = types.KeyboardButton("👈Вернуться назад")
        markup.add(button2, btn3, btn4, btn5, btn6, btn7, back)
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id, text="Помощь по регистрации", reply_markup=markup)

    elif (message.text == "Проблема с оплатой?💰"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Карта Казахстанского банка💳")
        button2 = types.KeyboardButton("Карта НЕ Казахстанского банка💳")
        back = types.KeyboardButton("👈Вернуться назад")
        markup.add(button1, button2, back)
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id, text="Помощь по оплате", reply_markup=markup)

    elif (message.text == "Далее"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Отмена участия")
        btn2 = types.KeyboardButton("Трансфер")
        btn3 = types.KeyboardButton("НЕ нашли ответа?")
        back = types.KeyboardButton("👈Вернуться назад")
        markup.add(btn1, btn2, btn3, back)
        tg_analytic.statistics(message.chat.id, message.text)
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
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id, text="🚌", reply_markup=markup)

    elif (message.text == "👈 Назад"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Отмена участия")
        btn2 = types.KeyboardButton("Трансфер")
        btn3 = types.KeyboardButton("НЕ нашли ответа?")
        back = types.KeyboardButton("👈Вернуться назад")
        markup.add(btn1, btn2, btn3, back)
        tg_analytic.statistics(message.chat.id, message.text)
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
        bot.send_message(message.chat.id, "Этот вопрос решается в индивидуальном порядке и зависит от правил конкретного соревнования. Проверьте информацию об этом в положении соревнования и напишите нам на почту (help@athletex.kz)")

    elif (message.text == "Отмена трансфера"):
        bot.send_message(message.chat.id, "Пожалуйста, проверьте в положении (оно находится на странице соревнования) правила по поводу отмены трансфера. Если там Вы не нашли информации, напишите нам на почту (help@athletex.kz)")

    elif (message.text == "Как купить трансфер на нескольких людей?"):
        bot.send_message(message.chat.id,"К сожалению, на данный момент нет технической возможности купить трансфер одновременно на несколько человек. Но если это позволяют правила ( см. положение на странице соревнования), вы можете купить несколько трансферов поочередно.")

    elif (message.text == "Нет ваучера в личном кабинете."):
        bot.send_message(message.chat.id,"Напишите нам на почту (help@athletex.kz).")

    elif (message.text == "Как купить трансфер?"):
        bot.send_message(message.chat.id,"Чтобы купить трансфер отдельно от участия, Вам нужно зайти на страницу нужного соревнования, нажать Кнопку [участвовать]. Перейти в корзину, выбрать в графе дистанции [не участвую или оплатил участие ранее], а в следующей графе выбрать трансфер. Внизу появится стоимость только трансфера. Нажимаете [оформить заказ] и оплачиваете.После оплаты Вы найдете билет на трансфер  в личном кабинете, в разделе [аккаунт-сводка] - [мои покупки].")

    elif (message.text == "Как узнать место и время отправления автобуса?"):
        bot.send_message(message.chat.id,"Время и место отправления указаны в вашем ваучере")

    elif (message.text == "Teкcт"):
        bot.send_message(message.chat.id, "Для перерегистраци с одного участника на другого, напишите нам на почту (help@athletex.kz)")

    elif (message.text == "Забыл пароль"):
        bot.send_message(message.chat.id, "Нажмите кнопку [ЗАБЫЛИ ПАРОЛЬ], после чего введите свой e-mail на который у вас зарегистрирован личный кабинет, и нажмите кнопку [OK]. После этого Вам на указанную почту придет письмо с кнопкой восстановления пароля [Reset password]. Нажмите эту кнопку. У вас откроется окно,куда нужно ввести почту и новый пароль(два раза). Запомните этот пароль и используйте для последующего входа в свой аккаунт.")

    elif (message.text == "Текcт"):
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
        bot.send_message(message.chat.id, "Напишите нам на (help@athletex.kz)")
        bot.send_message(message.chat.id, "Мы ответим Вам в ближайшее время")

    elif (message.text == "Проблема с регистрацией"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Забыл пароль")
        button2 = types.KeyboardButton("Создать личный кабинет")
        button3 = types.KeyboardButton("Как зарегистрироваться📝?")
        button4 = types.KeyboardButton("Успешно ли я зарегистрировался?")
        back = types.KeyboardButton("👈Вернуться назад")
        markup.add(button1, button2, button3, button4, back)
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id, text="Помощь по регистрации",reply_markup=markup)

    elif (message.text == "Карта НЕ Казахстанского банка💳"):
        bot.send_message(message.chat.id, "Если при оплате выходит ошибка, для решения этой проблемы пожалуйста, свяжитесь с нами по почте (help@athletex.kz)")

    elif (message.text == "Карта Казахстанского банка💳"):
        bot.send_message(message.chat.id, "Пожалуйста, проверьте, нет ли у вас лимитов на интернет покупки или иных проблем, связанных с банком")

    elif (message.text == "Смена дистанции"):
        bot.send_message(message.chat.id, "После того как Вы зашли в аккаунт, нажмите кружок аватара справа сверху и нажмите на раздел (Аккаунт-сводка). В разделе Я УЧАСТВУЮ справа от соревнования Вы увидите кнопку ИЗМЕНИТЬ. Нажмите на неё, после чего выберите новую нужную Вам дистанцию и нажмите оплатить. Напоминаем что за любое изменение в уже оплаченной регистрации берется сервисный сбор 2000 тенге. Также, если Вы выбираете более дорогую дистанцию, Вам нужно будет доплатить разницу между стоимостью бывшей и нынешней (она рассчитывается автоматически). Если же дистанция более дешевая, разница в цене не учитывается и не возвращается. ")
        bot.send_message(message.chat.id, "Изменение возможно только при наличии свободных слотов на нужную вам дистанцию.")
        bot.send_message(message.chat.id, "После оплаты обязательно проверьте вашу дистанцию в списке участников на странице соревнования. Если она по какой-то причине не поменялась, свяжитесь с нами по почте help@athletex.kz")

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

    elif (message.text == "Местоположение Athletex Pro🌍🔍"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("2Gis", url="https://2gis.kz/almaty/geo/70000001027702222"))
        bot.send_message(message.chat.id, text="Местоположение", reply_markup=markup)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Яндекс Карты", url="https://yandex.ru/maps/-/CDQwEY5L"))
        bot.send_message(message.chat.id, text="Местоположение", reply_markup=markup)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Google maps", url="https://goo.gl/maps/jkSMLbiinKV2S4m48"))
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
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id, text="{0.first_name}! Чем могу помочь?".format(message.from_user),reply_markup=markup)

    elif (message.text == "English"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Shop🧦👟🕶️")
        button2 = types.KeyboardButton("🏃Competitions🏃")
        markup.add(button1, button2, )
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id, text="{0.first_name} How can we help you? Select the desired item in the menu ".format(message.from_user), reply_markup=markup)

    elif (message.text == "Text"):
        bot.send_message(message.chat.id,text="First you need to create your account on this site athletex.kz You need to click on the black head icon on the top right, click "create a personal account" ( "создать личный кабинет" ) and fill in all the fields. Click register. After that, you need to click on the circle on the top right, fill in the "personal information"("персональная информация") section and save the changes. After that, you need to click on the two bars on the top left. Click on "our competitions ("наши соревнования")", select the desired competition, click "participate"("участвовать"). Participation is already in your cart! (icon top right). Click on it. It remains only to choose the distance and click "place order" ( "оформить заказ"). Pay in a convenient way for you. After payment, check yourself in the list of participants (it is published on the competition page). If your surname appeared there, then everything is in order, the registration was successful and you can drive up for the starter pack at the time and place indicated in the regulation (which is published below the list of participants).")

    elif (message.text == "Shop🧦👟🕶️"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Athletex Shop")
        btn2 = types.KeyboardButton("Work time⏰")
        btn3 = types.KeyboardButton("Location Athletex Shop🌍🔍")
        btn4 = types.KeyboardButton("Contacts☎")
        back = types.KeyboardButton("👈Back")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="Shop Information", reply_markup=markup)

    elif (message.text == "🏃Competitions🏃"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Calendar🗓")
        button2 = types.KeyboardButton("Registration")
        button3 = types.KeyboardButton("Results🏅")
        button4 = types.KeyboardButton("Partners")
        button5 = types.KeyboardButton("Volunteer")
        back = types.KeyboardButton("👈Back")
        markup.add(button1, button2, button3, button4, button5, back)
        bot.send_message(message.chat.id, text="Competition Information", reply_markup=markup)

    elif (message.text == "Volunteer"):
        bot.send_message(message.chat.id, "Do you want to be useful?  ")
        bot.send_message(message.chat.id, "Join the sports crowd?  ")
        bot.send_message(message.chat.id,"Find out the whole kitchen of the organization of sports competitions from the inside?  ")
        bot.send_message(message.chat.id, "Go out into nature more often?   ")
        bot.send_message(message.chat.id, "Get slots for competitions for your efforts?  ")
        bot.send_message(message.chat.id, "Participate even if you can't run yourself?")
        bot.send_message(message.chat.id, "We invite you to become an Extreme Athletics volunteer!")
        bot.send_message(message.chat.id, "You'll get:  ")
        bot.send_message(message.chat.id, "Friendly positive team;  ")
        bot.send_message(message.chat.id, "Interesting and understandable tasks;")
        bot.send_message(message.chat.id, "Meet different people, explore new places;")
        bot.send_message(message.chat.id, "and much more!")
        bot.send_message(message.chat.id, "Have you decided? Call/write to us at: +77014100510,")
        bot.send_message(message.chat.id, "The next competition is just around the corner!")

    elif (message.text == "Partners"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("go", url="https://athletex.kz/presentation/event.pdf ()"))
        bot.send_message(message.chat.id, text="If you want to be our partners, please contact us:",reply_markup=markup)
        bot.send_message(message.chat.id, text="+7 705 602 42 49")

    elif (message.text == "Registration"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton("Change the distance")
        btn3 = types.KeyboardButton("Problem with registration")
        btn4 = types.KeyboardButton("Payment problem💰")
        btn5 = types.KeyboardButton("Can't find myself in the list of participants")
        btn6 = types.KeyboardButton("Next")
        back = types.KeyboardButton("👈Back")
        markup.add(button2, btn3, btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="Registration assistance", reply_markup=markup)

    elif (message.text == "Payment problem💰"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Kazakhstan Bank card💳")
        button2 = types.KeyboardButton("NON-Kazakhstan bank card  💳")
        back = types.KeyboardButton("👈Back")
        markup.add(button1, button2, back)
        bot.send_message(message.chat.id, text="Payment problem�", reply_markup=markup)

    elif (message.text == "Next"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Cancellation")
        btn2 = types.KeyboardButton("Transfer")
        btn3 = types.KeyboardButton("Didn't find an answer?")
        back = types.KeyboardButton("👈Back")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="👉", reply_markup=markup)

    elif (message.text == "Transfer"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("How to find out the place and time of departure of the bus?")
        btn2 = types.KeyboardButton("How to buy a transfer?")
        btn3 = types.KeyboardButton("There is no voucher in my personal account.")
        btn4 = types.KeyboardButton("How to buy a transfer for several people?")
        btn5 = types.KeyboardButton("Cancellation of the transfer")
        btn6 = types.KeyboardButton("Change of a transfer ticket to another person")
        back = types.KeyboardButton("👈Return")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="🚌", reply_markup=markup)

    elif (message.text == "👈Return"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Cancellation")
        btn2 = types.KeyboardButton("Transfer")
        btn3 = types.KeyboardButton("Didn't find an answer?")
        back = types.KeyboardButton("👈Back")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="👉", reply_markup=markup)

    elif (message.text == "Contacts☎"):
        bot.send_message(message.chat.id, "+7 777 312 36 29")

    elif (message.text == "I can't find myself in the list of participants"):
        bot.send_message(message.chat.id,"There is a search option at the top of the list - please use it to find your name.")
        bot.send_message(message.chat.id," Don't forget that your last name / name is displayed exactly as you wrote it in the PERSONAL DATA (ПЕРСОНАЛЬНЫЕ ДАННЫЕ ) section (in English or another language)")
        bot.send_message(message.chat.id,"It is not necessary to enter both the last name and the first name in the search bar - only the last name will be enough")
        bot.send_message(message.chat.id,"Check if registration payment was successful? Without payment, registration is considered incomplete.")
        bot.send_message(message.chat.id,"Everyone should have their own account - make sure the person you are looking for in the list is registered with his/her account.")

    elif (message.text == "Cancellation"):
        bot.send_message(message.chat.id,"The possibility of canceling participation depends on the rules of the particular competition - please check the information about this in the regulation on the competition page.")

    elif (message.text == "Re-registration of a transfer ticket to another person"):
        bot.send_message(message.chat.id,"This issue is decided on an individual basis and depends on the rules of a particular competition. Check the information about this in the regulation of the competition and write to us by mail (help@athletex.kz)")

    elif (message.text == "Cancellation of the transfer"):
        bot.send_message(message.chat.id,"Please check in the regulation (it is on the competition page) the rules about the cancellation of the transfer. If you didn't find any information there, write us an email (help@athletex.kz)")

    elif (message.text == "How to buy a transfer for several people?"):
        bot.send_message(message.chat.id,"Unfortunately, at the moment there is no technical possibility to buy a transfer for several people at the same time. But if the rules allow it (see the regulations on the contest page), you can buy several transfers in turn.")

    elif (message.text == "There is no voucher in my personal account."):
        bot.send_message(message.chat.id, "Write us an email (help@athletex.kz ).")

    elif (message.text == "How to buy a transfer?"):
        bot.send_message(message.chat.id,"To buy a transfer separately from participation, you need to go to the page of the desired competition, click the [participate/ участвовать] button. Go to the cart, select in the distance column [not participating or paid for participation earlier/ не участвую или оплатил участие ранее], and in the next column select transfer. So now, you will see cost of the transfer only.  Click [place an order/оформить заказ] and pay. After payment, you will find a transfer ticket in your personal account, in the section [account - brief / аккаунт-сводка] - [my purchases/ мои покупки].")

    elif (message.text == "How to find out the place and time of departure of the bus?"):
        bot.send_message(message.chat.id, "The time and place of departure are indicated in your voucher")

    elif (message.text == "Re-register📝"):
        bot.send_message(message.chat.id,"To re-register from one participant to another, write to us by email (help@athletex.kz)")

    elif (message.text == "Forgot my password"):
        bot.send_message(message.chat.id,"Click the button [FORGOT PASSWORD / ЗАБЫЛ ПАРОЛЬ], then enter your e-mail address to which you have registered your personal account, and click [OK]. After that, you will receive an email with a password reset button [Reset password] to the specified email. Click this button. When a special window opens, you need to enter your email and a new password (twice). Remember this password and use it to log in to your account later.")

    elif (message.text == "Тext"):
        bot.send_message(message.chat.id,"To create your account on this site, you need to: Click on the black head icon on the top right - [create a personal account/ создать личный кабинет]")
        bot.send_message(message.chat.id, "Fill in all the fields and click [register]..")
        bot.send_message(message.chat.id,"After that, go to the section (personal information/ персональная информация) and fill in all the fields there. ")
        bot.send_message(message.chat.id,"there are few fields here, and they are very important to correctly show information about you in the finish protocol.")

    elif (message.text == "How to register"):
        bot.send_message(message.chat.id, "To register:")
        bot.send_message(message.chat.id, "Click the two bars on the top left..")
        bot.send_message(message.chat.id,"Click on [our events/ наши события] - select a competition - click [participate/ участвовать]..")
        bot.send_message(message.chat.id,"Participation is already in your cart! (Icon on the top right). Click on it.")
        bot.send_message(message.chat.id,"now you just need to select the distance and click [place an order/ оформить заказ].")
        bot.send_message(message.chat.id, "The (Select Club/ Выбрать клуб) field is optional! You can skip it.")

    elif (message.text == "Didn't find an answer?"):
        bot.send_message(message.chat.id, "Write to us at (help@athletex.kz)")
        bot.send_message(message.chat.id, "We will reply to you soon")

    elif (message.text == "Problem with registration"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Forgot my password")
        button2 = types.KeyboardButton("Create a personal account")
        button3 = types.KeyboardButton("How to register📝?")
        button4 = types.KeyboardButton("Have I successfully registered?")
        back = types.KeyboardButton("👈Back")
        markup.add(button1, button2, button3, button4, back)
        bot.send_message(message.chat.id, text="Registration assistance", reply_markup=markup)

    elif (message.text == "NON-Kazakhstan bank card  💳"):
        bot.send_message(message.chat.id,"If there is an error during payment, to solve this problem, please contact us by mail (help@athletex.kz)")

    elif (message.text == "Kazakhstan Bank card💳"):
        bot.send_message(message.chat.id,"Please check if you have limits on online purchases or other problems related to the bank")

    elif (message.text == "Change the distance"):
        bot.send_message(message.chat.id,"After you have logged into your account, click the avatar circle on the top right and click on the section (Account - brief / Аккаунт-сводка). In the I PARTICIPATE/ Я УЧАСТВУЮ section to the right of the competition, you will see the CHANGE/ ИЗМЕНИТЬ button. After click on it, select the new distance you need and click PAY/ ОПЛАТИТЬ . We remind you that for any change in the already paid registration, a service fee of 2000 tenge is charged. Also, if you choose a more expensive distance, you need to pay the difference between the cost of the former and the current one (it is calculated automatically). If the distance is cheaper, the difference in price is not taken into account and is not returned.  ")
        bot.send_message(message.chat.id,"The change is possible only if there are free slots for the distance you need.")
        bot.send_message(message.chat.id,"After payment, you need to check your distance in the list of participants on the competition page. If for some reason it has not changed, please contact us by mail  ")

    elif (message.text == "Results🏅"):
        bot.send_message(message.chat.id,"Go to the page of an already completed competition and scroll down to the end of page - there you will see a big red button [RESULTS/Результаты] .  Click it, and you will be redirected to the finish protocol page.")

    elif (message.text == "Athletex Shop"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Go to website", url="https://athletex.kz/shop"))
        bot.send_message(message.chat.id, text="Sports goods store Athletex Shop", reply_markup=markup)

    elif (message.text == "Calendar�"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Go to website", url="https://athletex.kz/competitions"))
        bot.send_message(message.chat.id, text="calendar of events", reply_markup=markup)

    elif (message.text == "Location Athletex Shop🌍🔍"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("2Gis", url="https://go.2gis.com/hntit"))
        bot.send_message(message.chat.id, text="Location", reply_markup=markup)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Яндекс Карты",url="https://yandex.kz/maps/-/CDQwEClP"))
        bot.send_message(message.chat.id, text="Location", reply_markup=markup)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Google maps",url="https://goo.gl/maps/2g9K3c8TirfAiry48"))
        bot.send_message(message.chat.id, text="Location", reply_markup=markup)

    elif (message.text == "Work time⏰"):
        photo = open('img2.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "Please check the store's opening hours on weekends and holidays in advance.")

    elif (message.text == "Have I successfully registered?"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CallCenter, Колл Центр", url="https://web.telegram.org/z/#677006359"))
        bot.send_message(message.chat.id,text="Check your name in the list of participants on the competition page at athletex.kz  If you found yourself, it means that the registration was successful.  If not, then the registration is not completed, contact the consultant at phone/WhatsApp/ Telegram +77056024249 (rus, eng) +77767373667 (rus, kaz)",reply_markup=markup)
        bot.send_message(message.chat.id, "( call / whatsapp / telegram)")

    elif (message.text == "👈Back"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Shop🧦👟🕶️")
        button2 = types.KeyboardButton("🏃Competitions🏃")
        markup.add(button1, button2, )
        bot.send_message(message.chat.id, text="{0.first_name}! How can we help you".format(message.from_user), reply_markup=markup)

    elif (message.text == "Казахский"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Дүкен🧦👟🕶️")
        button2 = types.KeyboardButton("🏃Жарыстар🏃")
        markup.add(button1, button2, )
        bot.send_message(message.chat.id,text="{0.first_name} Сізге қандай көмек көрсете аламын? Мәзірден қажетті элементті таңдаңыз".format(message.from_user), reply_markup=markup)

    elif (message.text == "Қалай тіркелуге болады📝?"):
        bot.send_message(message.chat.id,text="Өтілетін іс-шараға тіркелу үшін www.athletex.kz  сайтында сізді қызықтыратын іс-шараны ашып, жарыстың ережесімен танысу қажет. Одан кейін беттің төменгі жағындағы (Тіркелу) түймесін басыңыз. Содан кейін (себетті) ашып, (Төлеу) түймесін басыңыз.")

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
        bot.send_message(message.chat.id, text="Біздің серіктесіміз болғыңыз келсе төмендегі телефон арқылы хабарласыңыз",
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
        button1 = types.KeyboardButton("Төлем картасы Қазақстан банкінің картасы💳")
        button2 = types.KeyboardButton("Төлем картасы Қазақстан банкінің картасы емес💳")
        back = types.KeyboardButton("👈Артқа оралу")
        markup.add(button1, button2, back)
        bot.send_message(message.chat.id, text="Помощь по оплате", reply_markup=markup)

    elif (message.text == "Ары қарай"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Қатысудан бас тарту")
        btn2 = types.KeyboardButton("Трансфер.")
        btn3 = types.KeyboardButton("Қажетті жауап табылмады")
        back = types.KeyboardButton("👈Артқа оралу")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="👉", reply_markup=markup)

    elif (message.text == "Трансфер."):
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
        bot.send_message(message.chat.id,"Бұл мәселе жеке негізде шешіледі және белгілі бір жарыстың ережелеріне байланысты. Бұл туралы ақпаратты жарыстың ережесінен қарап, бізге пошта арқылы жазыңыз (help@athletex.kz).")

    elif (message.text == "Трансферден бас тарту"):
        bot.send_message(message.chat.id,"Жарыс туралы ережеде (ол жарыс бетінде) трансферден бас тарту тәртібін  қараңыз. Егер Сіз ол жерден ақпаратты таба алмасаңыз, бізге пошта арқылы жазыңыз (help@athletex.kz).")

    elif (message.text == "Бірнеше адамға трансферді қалай сатып алуға болады?"):
        bot.send_message(message.chat.id,"Өкінішке орай, қазіргі уақытта бірыңғай бірнеше адамға трансферді сатып алуға техникалық мүмкіндік жоқ. Бірақ егер ережелер рұқсат етсе (жарыс бетіндегі ережені қараңыз), Сіз кезекпен бірнеше трансферді сатып ала аласыз.»")

    elif (message.text == "Жеке кабинетте ваучер жоқ."):
        bot.send_message(message.chat.id, "Біздің электрондық поштамызға жазыңыз (help@athletex.kz).")

    elif (message.text == "Трансферді қалай сатып алуға болады?"):
        bot.send_message(message.chat.id,"Қатысудан тыс трансферді сатып алу үшін Сіз қалаған жарыстың бетіне өтуіңіз керек, содан соң [қатысу] түймесін басыңыз. Себетке өтіп, қашықтық бағанында [Мен қатыспаймын немесе қатысу үшін бұрын төледім] таңдаңыз, ал келесі бағанда трансферді таңдаңыз. Төменде тек трансфер құны көрсетіледі. [тапсырысты рәсімдеу] түймесін басып, төлеңіз. Төлем өткеннен кейін Сіз өзіңіздің жеке кабинетіңізде [аккаунт ақпары] - [менің сатып алуларым] бөлімінде трансфер билетін табасыз.")

    elif (message.text == "Автобустың жөнелтілетін орны мен уақытын қалай білуге ​​болады?"):
        bot.send_message(message.chat.id, "Кету уақыты мен орны Сіздің ваучеріңізде көрсетілген")

    elif (message.text == "Қайта тіркелу 📝"):
        bot.send_message(message.chat.id,"Бір қатысушыдан екінші қатысушыға қайта тіркелу үшін бізге пошта арқылы жазыңыз (help@athletex.kz)")

    elif (message.text == "Құпия сөзді ұмыттым"):
        bot.send_message(message.chat.id," [ҚҰПИЯ СӨЗДІ ҰМЫТТЫМ] түймесін басыңыз, содан кейін жеке кабинетіңіз тіркелген электрондық поштаңызды енгізіңіз де, [OK] түймесін басыңыз. Осыдан кейін Сіз көрсетілген электрондық поштаңызға  құпия сөзді қалпына келтіру түймесі бар [Құпия сөзді қалпына келтіру] электрондық хат аласыз. Осы түймені басыңыз. Электрондық поштаңызды және жаңа құпия сөзді (екі рет) енгізуіңіз керек терезе ашылады. Бұл құпия сөзді есте сақтаңыз және оны кейінірек жеке кабинетіңізге кіру үшін пайдаланыңыз.")

    elif (message.text == "Жеке кабинет ашу"):
        bot.send_message(message.chat.id,"Осы сайтта жеке аккаунтыңызды ашу үшін сіз: жоғарғы оң жақтағы қара бас белгішесін басыңыз - [Жеке кабинет ашу]")
        bot.send_message(message.chat.id, "Барлық орындарды толтырып, тіркеу түймесін басыңыз.")
        bot.send_message(message.chat.id,"Осыдан кейін (жеке ақпарат)  бөліміне өтіп, тағы бірнеше орындарды толтырыңыз. ")
        bot.send_message(message.chat.id,"Толтырылуы керек ақпарат көп емес және олар мәре хаттамасында сіз туралы ақпаратты дұрыс көрсету үшін өте маңызды.")

    elif (message.text == "Мәтін"):
        bot.send_message(message.chat.id, "Тіркелу үшін:")
        bot.send_message(message.chat.id, "Жоғарғы сол жақтағы екі жолақты басыңыз.")
        bot.send_message(message.chat.id,"[Біздің оқиғалар] түймесін басыңыз - қажетті жарысты таңдаңыз - [қатысу] түймесін басыңыз.")
        bot.send_message(message.chat.id, "Қатысу себетіңізде бар! (Жоғарғы оң жақ белгіше). Соны басыңыз. ")
        bot.send_message(message.chat.id, "Қашықтықты таңдап, [тапсырысты рәсімдеу] түймесін басу ғана қалады.")
        bot.send_message(message.chat.id, "«Клубты таңдау» өрісі міндетті емес! Оны өткізіп жіберуге болады.")

    elif (message.text == "Қажетті жауап табылмады"):
        bot.send_message(message.chat.id, "Біздің (help@athletex.kz) электрондық поштамызға жазыңыз")
        bot.send_message(message.chat.id, "Біз Сізге мүмкіндігінше тезірек жауап береміз")

    elif (message.text == "Тіркелу мәселесі"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Құпия сөзді ұмыттым")
        button2 = types.KeyboardButton("Жеке кабинет ашу")
        button3 = types.KeyboardButton("Қалай тіркелуге болады📝?")
        button4 = types.KeyboardButton("Тіркелуім сәтті өтті ме?")
        back = types.KeyboardButton("👈Артқа оралу")
        markup.add(button1, button2, button3, button4, back)
        bot.send_message(message.chat.id, text="Тіркелу бойынша көмек", reply_markup=markup)

    elif (message.text == "Төлем картасы Қазақстан банкінің картасы емес💳"):
        bot.send_message(message.chat.id,"Төлем кезінде қате орын алса, бұл мәселені шешу үшін бізге пошта арқылы хабарласыңыз (help@athletex.kz)")

    elif (message.text == "Төлем картасы Қазақстан банкінің картасы💳"):
        bot.send_message(message.chat.id,"Сізде онлайн сатып алу шектеулері немесе банкке қатысты басқа мәселелер бар-жоғын тексеріңіз")

    elif (message.text == "Қашықтықты ауыстыру"):
        bot.send_message(message.chat.id,"Аккаунтыңызға кіргеннен кейін жоғарғы оң жақтағы аватар шеңберін басыңыз және (Аккаунт ақпары) бөліміне кіріңіз. Жарыстың оң жағындағы МЕН ҚАТЫСАМЫН бөлімінде ӨЗГЕРТУ түймесін көресіз. Оны басыңыз, содан кейін сізге қажетті жаңа қашықтықты таңдап, төлеу түймесін басыңыз. Естеріңізге сала кетейік, қазірдің өзінде төленген тіркеуді өзгерту үшін 2000 теңге қызмет ақысы алынады. Сондай-ақ, егер сіз қымбатырақ қашықтықты таңдасаңыз, бұрынғы мен ағымдағы құны арасындағы айырмашылықты төлеуіңіз керек (ол автоматты түрде есептеледі). Егер қашықтық арзанырақ болса, баға айырмашылығы есепке алынбайды және қайтарылмайды.")
        bot.send_message(message.chat.id, "Қажетті қашықтыққа бос слоттар болған жағдайда ғана өзгерту мүмкін болады.")
        bot.send_message(message.chat.id,"Төлегеннен кейін жарыс бетіндегі қатысушылар тізімінен қашықтықты тексеріңіз. Егер қандай да бір себептермен ол өзгермесе, бізге help@athletex.kz поштасы арқылы хабарласыңыз ")

    elif (message.text == "Нәтижелер🏅"):
        bot.send_message(message.chat.id,"Аяқталған байқаудың бетіне өтіп, төменге қарай жылжыңыз - сол жерде үлкен қызыл [НӘТИЖЕЛЕР] түймешігін көресіз. Осы түймешекті басқаннан кейін сіз нәтижелер туралы есеп бетіне бағытталасыз.")

    elif (message.text == "Дүкен Athletex Shop"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://athletex.kz/shop"))
        bot.send_message(message.chat.id, text="Спорт тауарлары дүкені Athletex Shop", reply_markup=markup)

    elif (message.text == "Күнтізбе🗓"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Сайтқа өтіңіз", url="https://athletex.kz/competitions"))
        bot.send_message(message.chat.id, text="оқиғалар күнтізбесі", reply_markup=markup)

    elif (message.text == "Орналасқан жері🌍🔍"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("2Gis", url="https://go.2gis.com/hntit"))
        bot.send_message(message.chat.id, text="Орналасқан жері", reply_markup=markup)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Яндекс Карты",url="https://yandex.kz/maps/-/CDQwEClP"))
        bot.send_message(message.chat.id, text="Орналасқан жері", reply_markup=markup)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Google maps",url="https://goo.gl/maps/2g9K3c8TirfAiry48"))
        bot.send_message(message.chat.id, text="Орналасқан жері", reply_markup=markup)

    elif (message.text == "Жұмыс уақыты⏰"):
        photo = open('img2.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,"Демалыс және мереке күндері дүкеннің жұмыс уақытын алдын ала анықтап алыңыз.")

    elif (message.text == "Тіркелуім сәтті өтті ме?"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CallCenter, Колл Центр", url="https://web.telegram.org/z/#677006359"))
        bot.send_message(message.chat.id,text="Аthletex.kz сайтындағы жарыс бетіндегі қатысушылар тізімінен өз аты-жөніңізді тексеріңіз. Егер сіз өзіңізді тапсаңыз, тіркеуді сәтті өттіңіз дегенді білдіреді. Ал егер табылмаса, тіркелуіңіз аяқталмаған, ол үшін кеңесшіге хабарласыңыз: +77056024249 (орыс және ағылшын тілінде), +77767373667 (орыс және қазақ тілінде)" ,reply_markup=markup)
        bot.send_message(message.chat.id, "( звонок/ ватсап/ телеграмм )")

    elif (message.text == "👈Артқа оралу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Дүкен🧦👟🕶️")
        button2 = types.KeyboardButton("🏃Жарыстар🏃")
        markup.add(button1, button2, )
        bot.send_message(message.chat.id, text="{0.first_name} Выберите нужный пункт из меню".format(message.from_user),reply_markup=markup)

    else:
        bot.send_message(message.chat.id, text="Пожалуйста выберите существующий раздел, в меню кнопок")
        bot.send_message(message.chat.id, text="Please select an existing section, in the buttons menu")
        bot.send_message(message.chat.id, text="Түйме мәзірінен бар бөлімді таңдаңыз")

    if message.text[:10] == 'athexe2006' or message.text[:10] == 'Athexe2006':
        st = message.text.split(' ')
        if 'txt' in st or 'тхт' in st:
            tg_analytic.analysis(st,message.chat.id)
            with open('%s.txt' %message.chat.id ,'r',encoding='UTF-8') as file:
                bot.send_document(message.chat.id,file)
                tg_analytic.remove(message.chat.id)
        else:
            messages = tg_analytic.analysis(st,message.chat.id)
            bot.send_message(message.chat.id, messages)
            #здесь могла быть ваша реклама


while True:
    try:
        bot.polling(none_stop=True)
        time.sleep(5)
    except:
        continue
