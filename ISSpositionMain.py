import smtplib

import requests
import datetime

my_latitude = 17.425840
my_longitude = 78.188850
email = "pythontest20000@gmail.com"
password = "quiwkxuveovkdbaw"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
# data = response.json()['timestamp']
# print(data)
# print(type(data))
issLatitude = float(response.json()['iss_position']['latitude'])
issLongitude = float(response.json()['iss_position']['longitude'])

# parameter = {
#              "lat": 17.425840,
#              "lng": 78.188850,
#              "formatted": 0,
#             }
# suntime = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
suntime = requests.get(url="https://api.sunrise-sunset.org/json?lat=17.425840&lng=78.188850&formatted=0")
suntime.raise_for_status()
# new_data = suntime.json()
# print(new_data)
# sunrise = suntime.json()['results']['sunrise'].split(':')[1].split(":")[0]
sunrise = int(suntime.json()['results']['sunrise'].split('T')[1].split(":")[0])
sunset = int(suntime.json()['results']['sunset'].split('T')[1].split(":")[0])
#print(sunset)
# actual hour
#print(sunrise)

now = datetime.datetime.now()
# print(now.hour)
#while True:
#    time.sleep(60) - to run the program every 60 seconds
if now.hour > sunset or now.hour < sunrise:
    if issLongitude == my_longitude and issLatitude == my_latitude:
        with smtplib.SMTP("smtp.google.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email,
                                    to_addrs="jeringm",
                                    msg="Subject: ISS is above your house\n\nThis is amazing\nGo to the roof and wave")



