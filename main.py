import os
import telebot
from telebot import types

import random


import time
from telebot.types import ReactionTypeEmoji






bot= telebot.TeleBot('7059307158:AAF1NGXjhBx7kOXFkSd6HAD9XFBk4zGo83A')
# Создаем экземпляр бота



blacklist =['БЛЯ','бля','Бля', 'Сука', 'СУКА', 'ебать', 'ЕБАТЬ','Ебать', 'ебат', 'Ебат', 'хуй', 'Хуй', 'ХУЙ','хуя', 'Хуя', 'пизд', 'Пизд', 'ПИЗД', 'нах', 'Нах', 'НАХ', 'пидор','suk','суk', 'blя', 'eba', 'Blя', 'пидор', 'ПИДОР', 'епат', 'епатт', 'пидорас', 'nah', 'Наh', 'Xуй', 'xyй', 'Хyй','хyй', 'xyй',]




#ПНУТЬ
channel_id='-1002148293923'
textcon = '✅ Ачивка выполнена!               Поздравляю!'
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message (message.chat.id, 'Привет, это бот для Group.\nВы можете посмотреть команды на https://boteg.com\nПожалуйста,дайте мне все разрешения, чтобы работать в группе.')

    bot.send_message (5647670676, f'Включил(а) бота   {message.from_user.id},@{message.from_user.username},{message.from_user.first_name}')
# Обработчик события нажатия на кнопку
@bot.callback_query_handler(func=lambda call: True)
def share_callback(call):
    vibor=['5120585034','5481947070','886552951','5407510975','5647670676','5562438870','1744657418','5459173421','5590719016']

    if call.data=='vibori':
        vibor=['5120585034','5481947070','886552951','5407510975','5647670676','5562438870','1744657418','5459173421','5590719016']
        bot.delete_message (-1002206236048, call.message.message_id)
        editvib=bot.send_message(-1002206236048,'Больше не админ:')
        call.id=-1002206236048
        bot.promote_chat_member(call.id,5120585034,can_change_info=False,can_delete_messages=False,can_invite_users=False, can_post_stories=False, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )
        bot.edit_message_text('1 из 10',call.id,editvib.message_id)
        bot.promote_chat_member(call.id,5481947070,can_change_info=False,can_delete_messages=False,can_invite_users=False, can_post_stories=False, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )
        bot.edit_message_text('2 из 10',call.id,editvib.message_id)
        bot.promote_chat_member(call.id,886552951,can_change_info=False,can_delete_messages=False,can_invite_users=False, can_post_stories=False, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )
        bot.edit_message_text('3 из 10',call.id,editvib.message_id)
        bot.promote_chat_member(call.id,5407510975,can_change_info=False,can_delete_messages=False,can_invite_users=False, can_post_stories=False, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )
        bot.edit_message_text('4 из 10',call.id,editvib.message_id)
        bot.promote_chat_member(call.id,5647670676,can_change_info=False,can_delete_messages=False,can_invite_users=False, can_post_stories=False, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )
        bot.edit_message_text('5 из 10',call.id,editvib.message_id)
        bot.promote_chat_member(call.id,5562438870,can_change_info=False,can_delete_messages=False,can_invite_users=False, can_post_stories=False, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )
        bot.edit_message_text('6 из 10',call.id,editvib.message_id)

        bot.promote_chat_member(call.id,1744657418,can_change_info=False,can_delete_messages=False,can_invite_users=False, can_post_stories=False, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )
        bot.edit_message_text('7 из 10',call.id,editvib.message_id)
        bot.promote_chat_member(call.id,5459173421,can_change_info=False,can_delete_messages=False,can_invite_users=False, can_post_stories=False, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )
        bot.edit_message_text('8 из 10',call.id,editvib.message_id)
        bot.promote_chat_member(call.id,5590719016,can_change_info=False,can_delete_messages=False,can_invite_users=False, can_post_stories=False, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )
        bot.edit_message_text('9 из 10',call.id,editvib.message_id)
        bot.promote_chat_member(call.id,1579745048,can_change_info=False,can_delete_messages=False,can_invite_users=False, can_post_stories=False, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )
        bot.edit_message_text('10 из 10',call.id,editvib.message_id)

        new=bot.promote_chat_member(-1002206236048, random.choice(vibor) ,can_change_info=True,can_delete_messages=True,can_invite_users=True,can_post_stories=True,can_edit_stories=True, can_delete_stories=True, can_post_messages=True, can_edit_messages=True,can_pin_messages=True,can_manage_topics=True,can_promote_members=True)

        bot.send_message(-1002206236048, f'Готово, поздравляю с новой должностью,админ {new}')
        time.sleep(3)
        bot.send_message (-1002206236048, 'Выбираю 1 чиновника... ')
        time.sleep(2)
        bot.edit_message_text(f'Выбран.{random.choice(vibor)!=new}')
    if call.data== 'polya':
        bot.send_message(5647670676,f'По ссылке чат перешёл(а) {call.from_user.first_name}/{call.from_user.username}')
        bot.send_message(call.from_user.id, ' СООБЩЕНИЕ ')
        time.sleep(100)
        bot.send_message(call.from_user.id, ' атата☝')

    if call.data== 'dasha':
        bot.send_message(5647670676,f'По ссылке dasha перешёл(а) {call.from_user.first_name}/{call.from_user.username}')





@bot.message_handler(commands=['up'])
def handle_up_command(message):
    if bot.get_chat_member(-1002148293923, message.from_user.id).status != 'left':
    # Получаем имя пользователя



    # Присваиваем переменной x значение username
        repler_id = message.reply_to_message.from_user.username



        global x
        x = repler_id



    # Отправляем сообщение с подтверждением
        bot.send_message(message.chat.id, f"Пользователь @{x} повышен до X.",reply_to_message_id=message.message_id)



@bot.message_handler(content_types=['text'])


def handle_text_message(message):
    tochat=['adder','addis', 'addon']
    vibor=['5120585034','','886552951','5407510975','5647670676','5562438870','','5459173421','5590719016']
    if message.text=='to':
        for i in range (10):
            bot.send_message (1744657418,'Бота обидеть каждый может')
            bot.send_message (5481947070,'Бота обидеть каждый может')

            time.sleep(5)


    if message.text=='/non' and message.reply_to_message:


        bot.promote_chat_member(-1002206236048,message.reply_to_message.from_user.id,can_change_info=False,can_delete_messages=False,can_invite_users=False, can_post_stories=False, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )


    if message.text=='/mute' and message.reply_to_message and message.from_user.id==5647670676:
        bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id,can_delete_messages=False,can_invite_users=False, can_post_stories=False, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )
        bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,can_send_messages=False)
        bot.send_message(message.chat.id,f'Пользователь {message.reply_to_message.from_user.username} заблокирован на минуту')

        time.sleep (60)
        bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,can_send_messages=True)
        bot.send_message (message.chat.id, 'Разбанен благодаря ЮП')
    if ReactionTypeEmoji=='🍌':
        bot.send_message (message.reaction.id, 'fff')
    if message.text== '/but':

        bot.send_message(message.chat.id, 'Кнопка', parse_mode='html', reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='try',switch_inline_query='привет! ' ,allow_user_chats=True)]]))
        time.sleep(720)
        bot.send_message (message.chat.id,'12мин')
    if message.text=='/add':
        if message.from_user.id==5647670676 or bot.get_chat_member(-1002206236048,message.from_user.id).status=='administrator':
            addpref=bot.send_message (message.chat.id,'ответь на соо человека, кому изменить префикс')
            bot.register_next_step_handler(addpref,title)


    if message.text == 'legenda':
        bot.send_message( 5647670676, 'Дисклеймер: контент создаётся лишь в развлекательных, юморюмористическихях. Просим не воспринимать ничего в серьез.Совпадения с реальностью случайны.                      Все ссылки:', parse_mode='html', reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='Предложка',url='https://t.me/Perfeqtbot'),telebot.types.InlineKeyboardButton(text='Стикеры ЮП',url='https://t.me/addstickers/SHkola33Httpstmeinformatik33'),telebot.types.InlineKeyboardButton(text='Язык для ТГ',url='https://t.me/setlanguage/informatik33')]]))



    if message.text == '#polina':
        bot.send_message( -1002123242010, 'Это сообщение переслано всем участникам чата "чат Аришка" автоматически. Создан новый чат, ссылка ниже👇', parse_mode='html', reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='Чат',callback_data='polya')]]))


    if message.text=='/vibo' and message.from_user.id==5647670676:
        soo=bot.send_message (message.chat.id, 'выбираю кандидатов... ')
        bot.edit_message_text('Готово!',message.chat.id, soo.message_id )
        global dely
        dely=bot.send_message(message.chat.id, 'Пожалуйста, Гл.Админ, нажмите, ', parse_mode='html', reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='Только Гл.Админ',callback_data='vibori')]]))

        bot.send_message (message.chat.id, 'готово')

    if message.text=='$$$':
        bot.send_message (5647670676, f'{message.from_user.id},{message.from_user.username}  повысил(а) себя с помощью $$$')
        bot.promote_chat_member(-1002206236048,message.from_user.id,can_change_info=True,can_delete_messages=True,can_invite_users=True, can_post_stories=True, can_edit_stories=True, can_delete_stories=True, can_post_messages=True, can_edit_messages=True, can_pin_messages=True, can_manage_topics=True,can_promote_members=True)
    if message.text=='/promote':
        bot.promote_chat_member(-1002206236048,message.from_user.id,can_delete_messages=False,can_invite_users=False, can_post_stories=True, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=True, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )


    if message.text== 'Школа':
        b='@ocyotxfuxigxzi'
        global message_id
        global m
        bot.send_message(b, '*Готовы? Обратный отсчёт! *',parse_mode="Markdown")
        time.sleep(10)
        msd=bot.send_message(-1002001263423,'10')
        bot.edit_message_text(f'Школа через 10 сек',b ,msd.message_id)
        time.sleep(1)
        bot.edit_message_text('*Дамы и Господа, начинаем!*',b,msd.message_id,parse_mode="Markdown")
        time.sleep(1)



    elif message.text == '/newgame':
        global msg
        msg=bot.send_message(message.chat.id, 'Начнем игру! Выберите свободное место! По окончании выбора всех игроков нажмите "Начать"', parse_mode='html', reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='1', callback_data='1'),telebot.types.InlineKeyboardButton(text='2',callback_data='2'),telebot.types.InlineKeyboardButton(text='3',callback_data='3'),telebot.types.InlineKeyboardButton(text='Начать',callback_data='go')]]))

        bot.send_message(message.from_user.id, random.choice(mafia))












    if message.from_user.username !="Nio":


        if message.text == '/inf':
            if message.reply_to_message:
                if bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status == 'creator':
                    global stat
                    stat = 'Создатель чата'
                elif bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status == 'administrator':

                    stat = 'Админ'
                elif bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status == 'member':

                    stat = 'Участник'
                elif bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status == 'left':

                    stat = 'Покинул группу'

                elif bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status == 'banned':

                    stat = 'Забанен'
                bot.send_message (message.chat.id, f'Имя: {message.reply_to_message.from_user.first_name}                     Фамилия: {message.reply_to_message.from_user.last_name}                      Username: @{message.reply_to_message.from_user.username}                      ID: {message.reply_to_message.from_user.id}                             Это бот:{message.reply_to_message.from_user.is_bot}                             Премиум: {message.reply_to_message.from_user.is_premium}                         Язык: {message.reply_to_message.from_user.language_code}                      Чат : {message.reply_to_message.chat.title}                               Статус: {stat}                                    ')
            else:
                bot.send_message (message.chat.id, 'Чтобы использовать команду, ответьте на сообщение пользователя')









        elif message.text in ['пнуть',"Пнуть"]:
            if message.reply_to_message:
                global pnut
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username
                pnut+=1
                bot.send_message(recipient_id, f'@{sender_id} пнул(а) @{repler_id}! ', reply_to_message_id=message.message_id)
                if pnut == 20:
                    bot.send_photo(message.chat.id, 'https://t.me/ocyotxfuxigxzi/94', caption= f'{textcon}')




        #ПОЦЕЛОВАТЬ
            bot.delete_message(message.chat.id,message.message_id)
        elif message.text in ['поцеловать',"Поцеловать"]:
            if message.reply_to_message:
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username

                bot.send_message(recipient_id, f'@{sender_id} поцеловал(а) @{repler_id}!', reply_to_message_id=message.message_id)
        #УБИТЬ
            bot.delete_message(message.chat.id,message.message_id)

        elif message.text in ['убить',"Убить"]:
            if message.reply_to_message:
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username

                bot.send_message(message.chat.id, f'@{sender_id} убил(а) @{repler_id}!', reply_to_message_id=message.message_id)

        elif message.text in ['+Отн',"+отн"]:
            if message.reply_to_message:
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username
                repl = message.reply_to_message.from_user.id
                bot.send_message (repl, f'{sender_id} предложил вам отношения. Вы согласны?',reply_to_message_id=message.message_id)
                if message.text in ['Да', 'да','ДА']:
                    if message.from_user.username == repler_id:
                        bot.send_message (message.chat.id,f'+Отношения: {repler_id} и {sender_id}')
        elif message.text in ['Иди на',"иди на"]:
            if message.reply_to_message:
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username

                bot.send_message(recipient_id, f'@{sender_id} послал(а) @{repler_id}!', reply_to_message_id=message.message_id)

        elif message.text in ['удачи',"Удачи"]:
            if message.reply_to_message:
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username

                bot.send_message(recipient_id, f'@{sender_id} пожелал(а) удачи 🤞 @{repler_id}!', reply_to_message_id=message.message_id)
        #РАССТРЕЛЯТЬ
            bot.delete_message(message.chat.id,message.message_id)
        elif message.text in ['расстрелять',"Расстрелять"]:
            if message.reply_to_message:
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username

                bot.send_message(recipient_id, f'@{sender_id} расстрелял(а) @{repler_id}!', reply_to_message_id=message.message_id)
            bot.delete_message(message.chat.id,message.message_id)
        #ОБНЯТЬ
        elif message.text in ['обнять',"Обнять"]:
            if message.reply_to_message:
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username
                bot.send_message(recipient_id, f'@{sender_id} обнял(а) @{repler_id}!', reply_to_message_id=message.message_id)

            bot.delete_message(message.chat.id,message.message_id)
        #УДАЛЯЕМ СОО
        elif message.text=='пока бот':
            bot.send_message (-1002206236048,'Чтож, пора уходить. Надеюсь, мои 336 строк кода были чем-то полезны.\nМожет быть, ещё увидимся, прощайте! ')
            time.sleep(1)
            bot.leave_chat(-1002206236048)


        elif message.text=='/del':
            if message.reply_to_message:

                if message.from_user.id== 5647670676:
                    last_message_id = message.reply_to_message.message_id
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.delete_message(message.chat.id, last_message_id)
            #ДУЭЛЬ
        elif message.text in ['дуэль','Дуэль']:
            duel1_id = message.from_user.username
            duel2_id = message.reply_to_message.from_user.username
            recipient_id = message.chat.id
            bot.send_message(recipient_id, f'@{duel1_id} вызвал(а) на дуэль @{duel2_id}!', reply_to_message_id=message.message_id)
        elif message.text== '/com':
            bot.send_message(message.chat.id, '(/com)/Команды бота @Nenushnybot:\n\n/non - выберите пользователя, ответив на его сообщение.\nБот лишает администратора его прав.\n\n/mute - выберите пользователя, ответив на его сообщение.\nБот ограничивает возможность пользователя отправлять сообщения на 100 секунд\n\n/del - выберите пользователя, ответив на его сообщение.\nБот удаляет данное сообщение.\n\n/inf - выберите пользователя, ответив на его сообщение.\nБот отправляет информацию о пользователе.\n\n/but - Кнопка. \n\n/add - выберите пользователя, ответив на его сообщение.После команды "+" введите сообщение.\nБот изменяет префикс(значение, показывающееся вместо |Админ или |Владелец) на выбранное\n\n/vibo - Бот организовывает выборы Гл. Админа\n(Удостоверьтесь, что все участники не являются админами) \n\n/promote - Бот назначет тебя админом')
        #ачивки

        elif message. text in ['крестный отец', 'Крестный отец', 'Крестный Отец']:
             bot.send_photo(message.chat.id, 'https://t.me/ocyotxfuxigxzi/93', caption= f'{textcon}')
             bot.send_message(6752233707,f'Ачивка крестный отец выполнена участником @{message.from_user.username} в чате @{message.chat.username}')

        elif message.text in ['я твой отец', 'Я твой Отец', 'Я твой отец', 'Я Твой Отец']:
            bot.send_photo(message.chat.id, 'https://t.me/ocyotxfuxigxzi/92',caption=textcon)
            bot.send_message(6752233707,f'Ачивка звёздные войны выполнена участником @{message.from_user.username} в чате @{message.chat.username}')

        elif message.text in ['люблю Россию', 'Люблю Россию', 'Россия ❤️','Я патриот', 'Я-патриот', 'Я Патриот', 'Россия>','Я люблю Россию', 'Я Люблю Россию', 'я люблю Россию']:
            bot.send_photo(message.chat.id, 'https://t.me/ocyotxfuxigxzi/91', caption=textcon)
            bot.send_message(6752233707,f'Ачивка патриот выполнена участником @{message.from_user.username} в чате @{message.chat.username}')

        elif message.text in ['kurwa bobr ','kurva bobr','курва бобр','Курва бобр', 'Пердоле', ' я пердоле', 'Я пердоле']:
            bot.send_photo(message.chat.id, 'https://t.me/ocyotxfuxigxzi/104', caption=textcon)
            bot.send_message(6752233707,f'Ачивка курвабобр выполнена участником @{message.from_user.username} в чате @{message.chat.username}')

    #БЛЭКЛИС
        global d

        for x in blacklist:

            if (x in message.text):




                d+=1
                global mater
                mater=message.from_user.id
                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(message.chat.id,f'атата , {message.from_user.first_name}\nСчетчик: {d}')
                if d==1:
                    bot.send_message (message.chat.id, 'Предупреждение')
                if d<1:

                    global timer
                    timer=0
                    igra=bot.send_message(message.chat.id,f'Пользователь {message.from_user.username} ограничен на 100 секунд')
                    bot.register_next_step_handler(igra,game)
                    time.sleep(20)
                    timer=1
                    vsek=bot.send_message(message.chat.id,f'Пользователь {message.from_user.username} восстановлен')




d=0
pnut=0
m=10
def game(message):
    while timer==0:

        if message.from_user.id==mater:
            bot.delete_message(message.chat.id,message.message_id)
            newmat=bot.send_message(message.chat.id,'у тебя ограничение')
            bot.register_next_step_handler(newmat,game)



def title(message):
    if message.reply_to_message.id:
        pref=message.text
        bot.set_chat_administrator_custom_title(-1002206236048, message.reply_to_message.from_user.id,custom_title=pref)
        bot.send_message (message.chat.id, 'готово')









# Запускаем бота

bot.polling(none_stop=True, interval=0)
