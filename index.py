# Python smsbomber bot telegram
# From github aminrngbr1122 :: https://github.com/aminrngbr1122

# ? install lib
import os
os.system('-m pip install requests')
os.system('-m pip install art')

# ? Check system
def clear():
    import platform
    ui = platform.system()
    if ui == 'Windows':
        os.system('cls')
    if ui == 'Linux':
        os.system('clear')
        
clear()
        
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
idd = int(input('\n Chat_id : \n \n'))
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


def send(url, chat_id, params):
    par = {'chat_id':chat_id, 'text':params, 'parse_mode':'html'}
    requests.post(url+'sendmessage', data=par)


def main(url, idd):
    phone = int(input('\n phone : \n'))
    clear()
    send(url, idd, 'pls wait ...')
    sleep(2)
    send(url, idd, 'While attacking the desired target, please wait and don,t send msg...')
    sms(phone, phone)
    send(url, idd, 'End phone attacking ...')
    clear()
    main(url, idd)
        
if __name__ == '__main__':
    main(url, idd)
