import telebot
from random import randint
import requests
#from PIL import Image
#from io import BytesIO
#import urllib

#kitchen21_bot 1006074917:AAEuQNPot-SYTvBRFsp0DQ0GeUZc1a4QXJI

telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot('1006074917:AAEuQNPot-SYTvBRFsp0DQ0GeUZc1a4QXJI')
"""
url='https://avatars.mds.yandex.net/get-zen_doc/196027/pub_5d716e4b92414d00adae74cf_5d7170da3f548700ae6b35f2/scale_1200'
f = open('out.jpg','wb')
f.write(urllib.request.urlopen(url).read())
f.close()
"""
flag = 0    # for confirmation
order = {}  # order of our client

bever = {
    '101':'water',
    '102':'tea',
    '103':'coffee',
}
salad = {
    '104':'Cherepashka',
    '105':'RussianSalad',
    '106':'Tsezar',
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
    '104':'Cherepashka',
    '105':'RussianSalad',
    '106':'Tsezar',
    '107':'pasta',
    '108':'soup',
    '109':'vegetables',
    '110':'grenki',
    '111':'bread',
}

price = {
    '101':'100',
    '102':'100',
    '103':'100',
    '104':'200',
    '105':'200',
    '106':'200',
    '107':'300',
    '108':'300',
    '109':'300',
    '110':'50',
    '111':'50',
}

short_description = {
    '101':'вода',
    '102':'чай',
    '103':'кофе',
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
    '101':'Вода негазированная',
    '102':'Чай как чай',
    '103':'Растворимый и не очень растворимый кофе можно добавить сахар/сироп по вкусу',
    '104':'Черепашка ингредиенты: грецкий орех, яйцо, яблоко, майонез',
    '105':'Оливье ингредиенты: докторская колбаса, картофель, морковь, майонез',
    '106':'Цезарь ингредиенты: курица, листья салата, греночки, майонез ',
    '107':'Котлетка с макарошкой - иногда можете получить пюрешку в качестве сюрприза',
    '108':'Крем-суп - не забудь взять ко мне гренки',
    '109':'Тушеные овощи - на гриле - самая полезная еда, которую ты видел сегодня',
    '110':'Греночки как греночки',
    '111':'Хлебушек свежий',
}
"""
@bot.message_handler(commands=['photo'])
def photo(message):
    user_id = message.chat.id
    response = requests.get('https://avatars.mds.yandex.net/get-zen_doc/196027/pub_5d716e4b92414d00adae74cf_5d7170da3f548700ae6b35f2/scale_1200')
    img = Image.open(BytesIO(response.content))
    photo = open('out.jpg', 'rb')
    bot.send_photo(user_id, photo)
    photo.close()
    #bot.send_photo(user_id, img)
"""
@bot.message_handler(commands=['start', 'help'])
def help(message):
    user_id = message.chat.id
    bot.send_message(user_id, "Сегодня в меню: \n" +
                     "/fullmenu \n/main \n/beverages \n/salads \n/snacks \n" +
                     "Моя корзина:\n /cart")

@bot.message_handler(commands=['fullmenu'])
def fullmenu(message):
    user_id = message.chat.id
    items = 'Choose:\n\n'
    for key, value in allmenu.items():
        items += short_description.get(key, 0) + " - "
        items += price.get(key) + "$\n"
        items += ' /' + value + "_description" + "\n"
        items += ' /' + value + "_add_to_cart" + "\n"
        items += '\n'
    bot.send_message(user_id, items)

@bot.message_handler(commands=['beverages'])
def beverages(message):
    user_id = message.chat.id
    items = 'Choose:\n\n'
    for key, value in bever.items():
        items += short_description.get(key, 0) + " - "
        items += price.get(key) + "$\n"
        items += ' /' + value + "_description" + "\n"
        items += ' /' + value + "_add_to_cart" + "\n"
        items += '\n'
    bot.send_message(user_id, items)

@bot.message_handler(commands=['salads'])
def salads(message):
    user_id = message.chat.id
    items = 'Choose:\n\n'
    for key, value in salad.items():
        items += short_description.get(key, 0) + " - "
        items += price.get(key) + "$\n"
        items += ' /' + value + "_description" + "\n"
        items += ' /' + value + "_add_to_cart" + "\n"
        items += '\n'
    bot.send_message(user_id, items)

@bot.message_handler(commands=['snacks'])
def snacks(message):
    user_id = message.chat.id
    items = 'Choose:\n\n'
    for key, value in snack.items():
        items += short_description.get(key, 0) + " - "
        items += price.get(key) + "$\n"
        items += ' /' + value + "_description" + "\n"
        items += ' /' + value + "_add_to_cart" + "\n"
        items += '\n'
    bot.send_message(user_id, items)

@bot.message_handler(commands=['main'])
def maining(message):
    user_id = message.chat.id
    items = 'Choose:\n\n'
    for key, value in main.items():
        items += short_description.get(key, 0) + " - "
        items += price.get(key) + "$\n"
        items += ' /' + value + "_description" + "\n"
        items += ' /' + value + "_add_to_cart" + "\n"
        items += '\n'
    bot.send_message(user_id, items)

@bot.message_handler(commands=['cart'])
def show_cart(message):
    user_id = message.chat.id
    if user_id not in order:
        bot.send_message(user_id, "Ваша корзина пуста.\n/help")
    else:
        str = order[user_id]
        str = str.split('\n')
        res = 0
        str2 = ""

        for i in str:
            str2 += i
            for key, value in allmenu.items():
                if value == i:
                    num = price.get(key) # стоимость одного
                    str2 = str2 + " - " + num + "\n"
                    res += int(num)  # общая стоимость
                    break
        bot.send_message(user_id,
                      "Ваша корзина:" + '\n\n' + str2
                     + f"\nОбщая стоимость: {res}\n"
                     + "\nУдалить товар: /delete"
                     + "\nМеню: /fullmenu"
                     + "\nПодтвердить заказ: /confirm")


@bot.message_handler(commands=['delete'])
def delete_item(message):
    user_id = message.chat.id
    if user_id not in order or order[user_id] == "":
        bot.send_message(user_id, "Ваша корзина пуста.\n/help")
    else:
        list = "Что удалить?\n/"
        for i in order[user_id]:
            if (i == '\n'):
                list += "_delete" + i + "/"
            else:
                list += i
        bot.send_message(user_id, list)

@bot.message_handler(commands=['confirm'])
def confirm(message):
    user_id = message.chat.id
    if user_id not in order or order[user_id] == "":
        bot.send_message(user_id, "Ваша корзина пуста.\n/help")
    else:
        global flag
        flag = 1
        str = order[user_id].split("\n")
        str2 = ""
        res = 0

        for i in str:
            str2 += i
            for key, value in allmenu.items():
                if value == i:
                    num = price.get(key)  # стоимость одного
                    str2 = str2 + " - " + num + "\n"
                    res += int(num)  # общая стоимость
                    break

        bot.send_message(user_id, f"Подтвердить заказ?\n\n{str2}\nОбщая стоимость: {res}\n/yes_confirm")

@bot.message_handler(commands=['yes_confirm'])
def yes_confirm(message):
    user_id = message.chat.id
    if(flag == 0):
        bot.send_message(user_id, "Пожалуйста, сначала подтвердите заказ.\n/confirm")
    else:
        confirm_code = randint(1000, 9999)
        bot.send_message(user_id, "Ваш код подтверждения " + confirm_code.__str__()
                     + "\nAverage delivery time is 60 min")
    
@bot.message_handler(func=lambda message: message.text.split('_')[-1] == 'cart')
def add_to_cart(message):
    user_id = message.chat.id
    list = message.text.split('_')
    thing = list[0]
    thing = thing[1:]
    for i in allmenu.values():
        if i == thing:
            if user_id not in order:
                order[user_id] = thing + "\n"
            else:
                order[user_id] += thing + "\n"
            bot.send_message(user_id, thing + " успешно добавлено в корзину.\n" + 'Ваша корзина: /cart')

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


@bot.message_handler(func=lambda message: message.text.split('_')[-1] == 'delete')
def description(message):
    user_id = message.chat.id
    list = message.text.split('_')
    thing = list[0]
    thing = thing[1:] + "\n"    # товар который нужно удалить
    if user_id in order and thing in order[user_id] != -1:    # ищем подстроку в строке - есть ли товар который хотят удалить в корзине
        str = order[user_id]  # строка с нашими товарами через бекслешэн
        start = str.find(thing)
        end = start + len(thing)
        str = str[:start] + str[end:]
        order[user_id] = str
        bot.send_message(user_id, "Успешною")
        show_cart(message)
    else:
        bot.send_message(user_id, f"Вы не можете удалить {thing}\nПроверьте корзину /cart")

@bot.message_handler(content_types=['text'])
def remember(message):
    user_id = message.chat.id
    bot.send_message(user_id, "Приветик) /help")
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