import requests
import time
def telegram_bot_sendtext(bot_message):
    bot_token = '6283203048:AAGgOl-o6Itm3D1mw4_Omcf-g4t260vixN8'
    bot_chatID = '1155462778'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=MarkdownV2&text=' + str(bot_message).replace('.', '\\.')  # Escape the dot character
    response = requests.get(send_text)
    return response.json()
print("Good till now : sending medsage")
time.sleep(5)
telegram_bot_sendtext("Connection successful")
time.sleep(5)
i=6369877.269
telegram_bot_sendtext(i)