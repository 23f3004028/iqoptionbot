from iqoptionapi.stable_api import IQ_Option
import logging
import pandas as pd
import iqoptionapi
import time
import sys
import requests

def telegram_bot_sendtext(bot_message):
    bot_token = '5936883139:AAEUscW6GqEbwTyW0KZbQ3nSu_phhbytHTM'
    bot_chatID = '1155462778'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=MarkdownV2&text=' + str(bot_message).replace('.', '\\.')  # Escape the dot character
    response = requests.get(send_text)
    return response.json()


logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
I_want_money=IQ_Option("twotest@twotest.com","twotest@twotest.com")
#Default is "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
header={"User-Agent":r"Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0"}
cookie={"I_want_money":"GOOD"}
MODE="PRACTICE"
I_want_money.set_session(header,cookie)
I_want_money.connect()#connect to iqoption
#print(I_want_money.check_connect())
I_want_money.connect()
I_want_money.get_server_timestamp()
I_want_money.change_balance(MODE)
                        #MODE: "PRACTICE"/"REAL"
I_want_money.get_balance()

API = IQ_Option("twotest@twotest.com", "twotest@twotest.com")
check, reason = API.connect()
if not check:
    telegram_bot_sendtext("Connection failed.")
    exit()
telegram_bot_sendtext("Connection successful")
k = I_want_money.get_balance()
telegram_bot_sendtext(k)
#parameters
bollinger_length = 20  #std length
bollinger_deviation = 2.4
EMA_length = 30
HMA1_length = 20 
HMA2_length = 25
x = 5
trade_placed = False

start_time = time.time()

def get_remaining_seconds(x):
    current_time = time.localtime()
    current_minute = current_time.tm_min
    remaining_seconds = (x - (current_minute % x)) * 60 - current_time.tm_sec
    return remaining_seconds
while True:
    