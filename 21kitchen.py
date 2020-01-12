import json
import telebot
from random import randint
import requests

#kitchen21_bot 1006074917:AAEuQNPot-SYTvBRFsp0DQ0GeUZc1a4QXJI

telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

bot = telebot.TeleBot('1006074917:AAEuQNPot-SYTvBRFsp0DQ0GeUZc1a4QXJI')

flag = 0
bever = {
    '101':'water',
    '102':'tea',
    '103':'coffee',
}
salad = {
    '104':'salad4',
    '105':'salad5',
    '106':'salad6',
}
main = {
    '107':'pasta',
    '108':'soup',
    '109':'vegetables',
}
snack = {
    '110':'grenki',
    '111':'bread',
}

#allmenu = [bever, salad, main, snack]
allmenu = {
    '101':'water',
    '102':'tea',
    '103':'coffee',
    '104':'salad4',
    '105':'salad5',
    '106':'salad6',
    '107':'pasta',
    '108':'soup',
    '109':'vegetables',
    '110':'grenki',
    '111':'bread',
}


order = {} #order of our client

@bot.message_handler(commands=['start', 'help'])
def help(message):
    user_id = message.chat.id
    bot.send_message(user_id, "Today we have: \n" +
                     "/fullmenu \n/main \n/beverages \n/salads \n/snacks \n" +
                     "Show my order:\n /cart")

@bot.message_handler(commands=['fullmenu'])
def fullmenu(message):
    user_id = message.chat.id
    items = 'Choose:\n\n'
    for key, value in allmenu.items():
        items += key
        items += ' '
        items += value
        items += '\n'
    items += '\nType number to add to cart.'
    bot.send_message(user_id, items)

@bot.message_handler(commands=['beverages'])
def beverages(message):
    user_id = message.chat.id
    items = 'Choose:\n\n'
    for key, value in bever.items():
        items += key
        items += ' '
        items += value
        items += '\n'
    items += '\nType number to add to cart.'
    bot.send_message(user_id, items)

@bot.message_handler(commands=['salads'])
def salads(message):
    user_id = message.chat.id
    items = 'Choose:\n\n'
    for key, value in salad.items():
        items += key
        items += ' '
        items += value
        items += '\n'
    items += '\nType number to add to cart.'
    bot.send_message(user_id, items)

@bot.message_handler(commands=['snacks'])
def snacks(message):
    user_id = message.chat.id
    items = 'Choose:\n\n'
    for key, value in snack.items():
        items += key
        items += ' '
        items += value
        items += '\n'
    items += '\nType number to add to cart.'
    bot.send_message(user_id, items)

@bot.message_handler(commands=['main'])
def maining(message):
    user_id = message.chat.id
    items = 'Choose:\n\n'
    for key, value in main.items():
        items += key
        items += ' '
        items += value
        items += '\n'
    items += '\nType number to add to cart.'
    bot.send_message(user_id, items)

@bot.message_handler(commands=['cart'])
def show_cart(message):
    user_id = message.chat.id
    if user_id not in order:
        bot.send_message(user_id, "Your cart is empty.\n/help")
    else:
        bot.send_message(user_id, "Your cart:" + '\n\n' + order[user_id] + '\n'
                     + "\nDelete any item:" + "\n/delete"
                     + "\nSee more:" + "\n/fullmenu"
                     + "\nConfirm order:" + "\n/confirm")

@bot.message_handler(commands=['delete'])
def delete_item(message):
    user_id = message.chat.id
    if user_id not in order:
        bot.send_message(user_id, "Sorry, you can't delete. \nYour cart is empty.\n/help")
    else:
        count = 1
        bot.send_message(user_id, "Which item do u want to delete?\n")# + order[user_id])
        list = ''
        for i in order[user_id]:
            if (i == '\n'):
                list += ' - ' + count.__str__() + i
                count += 1
            else:
                list += i
        list += ' - ' + count.__str__()
        bot.send_message(user_id, list)

@bot.message_handler(commands=['confirm'])
def confirm(message):
    user_id = message.chat.id
    if user_id not in order:
        bot.send_message(user_id, "Sorry, you can't confirm.\nYour cart is empty.\n/help")
    else:
        global flag
        flag = 1
        bot.send_message(user_id, "Confirm order?\n\n" + order[user_id] + "\n/yes_confirm")

@bot.message_handler(commands=['yes_confirm'])
def yes_confirm(message):
    user_id = message.chat.id
    if(flag == 0):
        bot.send_message(user_id, "Please, confirm your order first.\n/confirm")
    else:
        confirm_code = randint(10000, 1000000)
        bot.send_message(user_id, "Your confirmation code is " + confirm_code.__str__()
                     + "\nAverage delivery time is 60 min")

@bot.message_handler(content_types=['text'])
def remember(message):
    user_id = message.chat.id
    item = allmenu.get(message.text, 0)
    if (item != 0):
        if user_id not in order:
            order[user_id] = item.upper()
        else:
            order[user_id] += '\n' + item.upper()
        bot.send_message(user_id, item.upper() + ' added to cart successfully.\n' + 'Type /cart to see your order.')
    else:
        bot.send_message(user_id, "Type number to add an item to cart \nor /help")

bot.polling()