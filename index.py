# Python smsbomber bot telegram
# From github aminrngbr1122 :: https://github.com/aminrngbr1122

# ? install lib
import os
os.system('-m pip install requests')
os.system('-m pip install art')
os.system('-m pip install re')

# ? Check system
def clear():
    import platform
    ui = platform.system()
    if ui == 'Windows':
        os.system('cls')
    if ui == 'Linux':
        os.system('clear')
        
clear()
        
from re import match
import art
from jojo import sms
from sys import exit
from time import sleep
from colorama import Fore
import requests

# ? use lib

art.tprint('AMINRNGBR1122 FROM GITHUB')

# ? Get token
token = input('\n \n Token : \n')
url = f'https://api.telegram.org/bot{token}/'
clear()
print(f'\n Login to telegram token : {token} \n \n pls wait ... \n \n')
try:
    data = requests.get(f'{url}getUpdates')
except:
    print(Fore.RED, '\n Network Error ! \n \n')
    exit()
if data.status_code == 404:
    clear()
    print(Fore.RED, '\n Login Error ! \n \n')
    exit()
if data.status_code == 200:
    clear()
    print(Fore.GREEN, '\n Login ok --- \n \n bot smsbomber run --- \n \n')

# ? function bot
def get_chat_id(update):
    return update['message']['chat']['id']


def get_message_text(update):
    return update['message']['text']


def last_update(url):
    response = requests.get(url+"getUpdates")
    response = response.json()
    result = response['result']
    total_updates = len(result) - 1
    return result[total_updates]


def send(url, chat_id, params, caption='.', types='sendmessage'):
    if types == 'sendmessage':
        par = {'chat_id': chat_id, 'text': text, 'parse_mode': 'html'}
        requests.post(url+'sendmessage', data=par)
    if types == 'sendvideo':
        par = {'chat_id': chat_id, 'video': params,
               'parse_mode': 'html', 'caption': caption}
        requests.post(url+'sendvideo', data=par)
    if types == 'sendphoto':
        par = {'chat_id': chat_id, 'photo': params,
               'parse_mode': 'html', 'caption': caption}
        requests.post(url+'sendphoto', data=par)
    if types == 'sendaudio':
        par = {'chat_id': chat_id, 'audio': params,
               'parse_mode': 'html', 'caption': caption}
        requests.post(url+'sendaudio', data=par)
    if types == 'senddocument':
        par = {'chat_id': chat_id, 'document': params,
               'parse_mode': 'html', 'caption': caption}
        requests.post(url+'senddocument', data=par)


def main(url):
    while True:
        idd = last_update(url)['update_id']
        update = last_update(url)
        if get_message_text(update).lower() == '/start':
            send(url, get_chat_id(update), '<b>Phone:</b>', types='sendmessage')
        if match('0(.*)[11]', get_message_text(update)):
            phone = get_message_text(update)
            number = get_message_text(update)
            send(url, get_chat_id(update), '<b>pls wait ...</b>', types='sendmessage')
            sleep(2)
            send(url, get_chat_id(update), '<b>While attacking the desired target, please wait and don,t send msg...</b>', types='sendmessage')
            sms(get_message_text(update), get_message_text(update))
            send(url, get_chat_id(update), '<b>End phone attacking ...</b>', types='sendmessage')
                
        idd = []
        update = []


if __name__ == '__main__':
    main(url)
