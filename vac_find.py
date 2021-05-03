import requests
import json
import telegram_bot
from datetime import date

today = date.today()
PINCODES = ['516001','516002','516003','516004']
DATE='03-05-2021'
config = {
    'accept': 'application/json',
    'Accept-Language': 'hi_IN'
}

for PINCODE in PINCODES:
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=' + PINCODE + '&date=' + DATE
    result = requests.get(url, headers=config)
    json.loads(result.text)
    data = json.loads(result.text)
    for center in data['centers']:
        info = {}
        info['name'] = center['name']
        info['district_name'] = center['district_name']
        info['fee_type'] = center['fee_type']
        s = {}
        i = 1
        for session in center['sessions']:
            s['date'] = session['date']
            s['available_capacity'] = session['available_capacity']
            s['min_age_limit'] = session['min_age_limit']
            s['vaccine'] = session['vaccine']
            s['slots'] = session['slots']
            info['session_' + str(i)] = s
            i = i + 1
        obj = json.dumps(info, indent = 1)
        ans = telegram_bot.telegram_bot_sendtext(obj)
        
        