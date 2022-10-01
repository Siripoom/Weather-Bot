import requests
import json
import schedule
import time

url = "https://notify-api.line.me/api/notify"
apiKey = "your api key"
lineToken = "your line Token"
url = "https://notify-api.line.me/api/notify"
url = "https://api.openweathermap.org/data/2.5/weather?id=1150953&units=metric&appid=" + apiKey
r = requests.get(url)
data = json.loads(r.text)
print(data)

temp = data["main"]["temp"]
temp_max = data["main"]["temp_max"]
temp_min = data["main"]["temp_min"]
weather = data["weather"][0]["description"].capitalize()

msg = "%s\n 🌡Current temperature: %s°C\n 💌Highest temperature: %s\n 💌Lowest temperature: %s\n 💧%s" %(data['name'],temp,temp_max,temp_min,weather)

payload = {"message": {msg}}
headers = {"Authorization": "Bearer " + lineToken}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

schedule.every().day.at("07:30").do((lineToken,msg))
schedule.every(10).seconds.do((lineToken))
while True:
     schedule.run_pending()
     time.sleep(1)