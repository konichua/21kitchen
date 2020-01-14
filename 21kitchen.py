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

short_description = {
    '101':'че смотришь, обычная вода',
    '102':'пакетик чая',
    '103':'растворимый и не очень растворимый кофе',
    '104':'черепашка',
    '105':'оливье',
    '106':'цезарь',
    '107':'котлетка с макарошкой',
    '108':'крем-суп',
    '109':'тушеные овощи',
    '110':'греночки',
    '111':'хлебушек',
}

long_description = {
    '101':'вода вода вода вода вода',
    '102':'чай как чай',
    '103':'растворимый и не очень растворимый кофе можно добавить сахар/сироп по вкусу',
    '104':'черепашка ингредиенты: грецкий орех, яйцо, яблоко, майонез',
    '105':'оливье ингредиенты: докторская колбаса, картофель, морковь, майонез',
    '106':'цезарь ингредиенты: курица, листья салата, греночки, майонез ',
    '107':'котлетка с макарошкой - иногда можете получить пюрешку в качестве сюрприза',
    '108':'крем-суп - не забудь взять ко мне гренки',
    '109':'тушеные овощи - на гриле - самая полезная еда, которую ты видел сегодня',
    '110':'греночки как греночки',
    '111':'хлебушек свежий',
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
        #items += key
        items += ' /' + value + "_description" + "\n"
        items += ' /' + value + "_add_to_cart" + "\n"
        items += short_description.get(key, 0)
        items += '\n'
    items += '\nType number to add to cart.'
    bot.send_message(user_id, items)

@bot.message_handler(commands=['beverages'])
def beverages(message):
    user_id = message.chat.id
    items = 'Choose:\n\n'
    for key, value in bever.items():
      #  items += key
        items += ' /' + value + "_description" + "\n"
        items += ' /' + value + "_add_to_cart" + "\n"
        items += short_description.get(key, 0)
        items += '\n'
    items += '\nType number to add to cart.'
    bot.send_message(user_id, items)

@bot.message_handler(commands=['salads'])
def salads(message):
    user_id = message.chat.id
    items = 'Choose:\n\n'
    for key, value in salad.items():
    #    items += key
        items += ' /' + value + "_description" + "\n"
        items += ' /' + value + "_add_to_cart" + "\n"
        items += short_description.get(key, 0)
        items += '\n'
    items += '\nType number to add to cart.'
    bot.send_message(user_id, items)

@bot.message_handler(commands=['snacks'])
def snacks(message):
    user_id = message.chat.id
    items = 'Choose:\n\n'
    for key, value in snack.items():
    #    items += key
        items += ' /' + value + "_description" + "\n"
        items += ' /' + value + "_add_to_cart" + "\n"
        items += short_description.get(key, 0)
        items += '\n'
    items += '\nType number to add to cart.'
    bot.send_message(user_id, items)

@bot.message_handler(commands=['main'])
def maining(message):
    user_id = message.chat.id
    items = 'Choose:\n\n'
    for key, value in main.items():
     #   items += key
        items += ' /' + value + "_description" + "\n"
        items += ' /' + value + "_add_to_cart" + "\n"
        items += short_description.get(key, 0)
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
        confirm_code = randint(1000, 9999)
        bot.send_message(user_id, "Your confirmation code is " + confirm_code.__str__()
                     + "\nAverage delivery time is 60 min")

"""    
@bot.message_handler(content_types=['text'])
def delete(message):
    user_id = message.chat.id
    num = ''
    num = message.text
    print(num)
    print(num.isdigit())
    if (num.isdigit() == True):
        num = int(num)
        if (num > 0 & num < 100):
            #delete
            bot.send_message(user_id, "number")
        else:
            bot.send_message(user_id, "Please, write propper order to delete.")
#    else: above
"""
    
@bot.message_handler(func=lambda message: message.text.split('_')[-1] == 'cart')
def add_to_cart(message):
    user_id = message.chat.id
    list = message.text.split('_')
    thing = list[0]
    thing = thing[1:]
    for i in allmenu.values():
        if i == thing:
            if user_id not in order:
                order[user_id] = thing
            else:
                order[user_id] += '\n' + thing
            bot.send_message(user_id, thing + " is added to cart successfully.\n" + 'Type /cart to see your order.')

@bot.message_handler(func=lambda message: message.text.split('_')[-1] == 'description')
def description(message):
    user_id = message.chat.id
    list = message.text.split('_')
    thing = list[0]
    thing = thing[1:]
    for key, value in allmenu.items():
        if value == thing:
            bot.send_message(user_id, thing + ":\n" + long_description.get(key))
            photo = open(f'{thing}.jpg', 'rb')
            bot.send_photo(user_id, photo)

@bot.message_handler(content_types=['text'])
def remember(message):
    user_id = message.chat.id
    bot.send_message(user_id, "Hiii /help /start")
"""
    item = allmenu.get(message.text, 0)
    if (item != 0):
        if user_id not in order:
            order[user_id] = item.upper()
        else:
            order[user_id] += '\n' + item.upper()
        bot.send_message(user_id, item.upper() + ' added to cart successfully.\n' + 'Type /cart to see your order.')
    else:
        bot.send_message(user_id, "Type number to add an item to cart \nor /help")
"""

bot.polling(none_stop=True, timeout=60)