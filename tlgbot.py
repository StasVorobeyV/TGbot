import telebot.wikipedia

#созданием экземпляр бота
bot = telebot.TeleBot('5785862157:AAE9KcMlHn7l6xmBSyEzEOD4hmWyERJZOtQ')

wikipedia.set_lang("ru")

#читсим текст статьи
def getwiki(s):
    try:
        ny = wikipedia.page(s)

        #получаем первую тысячу символов
        wikitext = ny.content[:1000]

        #разделяем по точкам
        wikimas = wikitext.split('.')

        #отбарсываем все после последней точки
        wikimas = wikimas[:1]

        #создаем пустую переменную для текста
        wikitext2 = ''

        #проходим по строкам гед нет занков равно (т.е. есть всеБ кроме заголовков)
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip()))>3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
#теперь при помощи регулярных выражений убираем разметку
        wikitext = re.sub('\([^()]*\)', '', wikitext2)
        wikitext = re.sub('\([^()]*\)', '', wikitext2)
        wikitext = re.sub('\{[^\{\}]*\}', '', wikitext2)

#возвращаем текстовую строку
        return wikitext2

#обрабатываем исключеник, которое мог вернутьт модуль wikipedia при запросе
    except Exception as e:
        return 'в энциклопедии нет информации об этом'


    #функция обрабатывает команду / start
@bot.send_message_handler(commamds=["start"])
def start(m, res=False, chat=None):
    bot.send_message(m, chat.id, "отправьте мне любое слово, и я найду его значение в Wikipedia")


    #получение сообщений от user
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))

#запускаем бота
bot.polling(none_stop=True, interval=0)