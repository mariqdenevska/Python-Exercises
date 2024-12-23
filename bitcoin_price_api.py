from datetime import datetime
import requests

URL = 'https://data-api.ccdata.io/index/cc/v1/historical/days'
PARAMS =  {
    "market":"cadli",
    "instrument":"BTC-USD",
    "limit":10,
    "aggregate":1,
    "fill":"true",
    "apply_mapping":"true",
    "response_format":"JSON",
    "api_key":"aad336b3c693008f2bcfebda95fe645f5fa7591c0406e8d55f857d02d6b0ba15"
    }
HEADER = {"Content-type":"application/json; charset=UTF-8"}

response = requests.get(URL, params=PARAMS, headers=HEADER,timeout=10)

json_response = response.json()

for day in json_response['Data']:
    timestamp = day.get('TIMESTAMP')
    price_open = round((day.get('OPEN')),2)
    price_high = round((day.get('HIGH')),2)
    price_low = round((day.get('LOW')),2)
    volume = day.get('VOLUME')

    date = datetime.fromtimestamp(timestamp)

    print(f"Date: {date}")
    print(f"    Price Open: {price_open} ; High Price: {price_high} ; Low Price: {price_low} ; Volume: {volume}")
