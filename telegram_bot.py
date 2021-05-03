import configparser
import requests

def telegram_bot_sendtext(bot_message):
    configParser = configparser.RawConfigParser()   
    configFilePath = r'config.txt'
    configParser.read(configFilePath)
    bot_token = str(configParser.get('tele-config', 'bot_token'))
    # print(type(bot_token))
    bot_chatID = str(configParser.get('tele-config', 'bot_chatID'))
    # print(bot_chatID)
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    print(send_text)
    response = requests.get(send_text)
    return response.json()

