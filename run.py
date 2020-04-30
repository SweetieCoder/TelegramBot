from uuid import uuid4

from telegram.ext import Updater, CommandHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext import InlineQueryHandler

from telegram.chataction import ChatAction

from telegram import ReplyKeyboardMarkup #for keyboard
from telegram import InlineKeyboardButton #for glass keyboard
from telegram import InlineKeyboardMarkup #for glass keyboard
from telegram import InputTextMessageContent
from telegram import InlineQueryResultArticle



updater = Updater('TOKEN')

def start(bot, update):
    #import pdb; pdb.set_trace()
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name

    bot.send_chat_action(chat_id, ChatAction.TYPING)
    bot.sendMessage(chat_id, 'به {} {} خوش آمدید'.format(first_name, last_name))

def service_keyboard(bot, update):
    chat_id = update.message.chat_id
    keyboard = [
                    ['آموزش پایتون'],
                    ['آموزش بات تلگرام', 'آموزش جنگو'],
                    ['آموزش بازی نویسی', 'آموزش گیت', 'آموزش رجکس']
               ]
    bot.sendMessage(chat_id, 'تمایل به تماشای کدام دوره اموزشی دارید؟', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True))


def favor_keyboard(bot, update):
    chat_id = update.message.chat_id

    keyboard = [
                    [
                        InlineKeyboardButton('پراوید', callback_data = '1'),
                        InlineKeyboardButton('پراوید پایتون', callback_data = '2'),
                    ],
                    [
                        InlineKeyboardButton('پراوید جنگو', callback_data = '3'),
                    ]
                ]
    bot.sendMessage(chat_id, 'دوره های آموزشی آموزشگاه پراوید', reply_markup = InlineKeyboardMarkup(keyboard))

def favor_handler_button(bot, update):
    # import pdb; pdb.set_trace()

    query = update.callback_query
    data = query.data
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    descrption = 'درباره دوره اینجا نوشته میشود، کد ارسال شده {} میباشد'.format(data)

    if data == '1':
        descrption = 'first condition'
    elif data == '2':
        descrption = 'second condition'
    else:
        descrption = 'third condition'

    bot.editMessageText(text = descrption, chat_id = chat_id, message_id = message_id)


def feature_inline_query(bot, update):
    import pdb; pdb.set_trace()
    query = update.inline_query.query
    results = list()

    results.append(InlineQueryResultArticle(id = uuid4(), title = "Uppercase", input_message_content = InputTextMessageContent(query.upper())))
    results.append(InlineQueryResultArticle(id = uuid4(), title = "Lowercase", input_message_content = InputTextMessageContent(query.lower())))

    bot.answerInlineQuery(results = results)


start_command = CommandHandler('start', start)
service_command = CommandHandler('service', service_keyboard)
favor_command = CommandHandler('favor', favor_keyboard)
favor_handler = CallbackQueryHandler(favor_handler_button)
feature_handler = InlineQueryHandler(feature_inline_query)


updater.dispatcher.add_handler(start_command)
updater.dispatcher.add_handler(service_command)
updater.dispatcher.add_handler(favor_command)
updater.dispatcher.add_handler(favor_handler)
updater.dispatcher.add_handler(feature_handler)


updater.start_polling()
updater.idle()
