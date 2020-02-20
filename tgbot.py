import telebot
import time

TOKEN = "1092994551:AAF5qCBmMA7ynk8YcWQe6sViVq0WsnNwlJw"

bot = telebot.TeleBot(TOKEN)

questions = ("Какая столица России ?", "Москва", "Не ездок, а со шпорами, Не будильник, а всех будит.", "Петух",
             "Кто говорит на всех языках?", "Эхо", "Шесть ног, две головы, а хвост один. Что это такое?", "Всадник",
             "Что это такое: синий, большой, с рогами полностью набит зайцами?", "Троллейбус",
             "Вот полозья, спинка, планки — А всё вместе это — …", "Санки")

#users = [{'id': 7336354760, 'actualQuestion': 1, 'correctAnswers': 0}]
users = [{'id': 7336354760, 'actualQuestion': 1, 'correctAnswers': 0}]


@bot.message_handler(content_types=["text"])
def answer(message):
    global user
    for us in users:
        if us.get('id') == message.chat.id:
            user = us
            try:
                if message.text == questions[user.get('actualQuestion')]:
                    bot.send_message(message.chat.id, f'Ответ {message.text} верный. Идем дальше.')
                    us['actualQuestion'] += 2
                    break
                q = questions[user.get('actualQuestion') - 1]
                bot.send_message(message.chat.id, 'Загадка:')
                bot.send_message(message.chat.id, q)
                break
            except:
                bot.send_message(message.chat.id,
                                 'Загадки закончились. Начнем с начала, возможно, что уже появились новые загадки =)')
                us['actualQuestion'] = 1

    if us.get('id') != message.chat.id:
        bot.send_message(message.chat.id,
                         "Добро пожаловать! Давай сыграем в игру. Я задаю тебе загадку, а ты пишешь ответ сюда. Для начала отправь мне любое сообщение.")
        users.append({'id': message.chat.id, 'actualQuestion': 1, 'correctAnswers': 0})


if __name__ == '__main__':
    user = {}
    bot.polling(none_stop=True)
