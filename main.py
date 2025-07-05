import requests
from datetime import datetime
import smtplib

MY_LAT = 28.613939
MY_LONG = 77.209023
is_close = False
is_dark = False

my_email = "banerjee.sumanto008@gmail.com"
app_password = "afwm bbdo ftqx imvs"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()

latitude = float(data["iss_position"]["latitude"])
longitude = float(data["iss_position"]["longitude"])
print(longitude)
# print(type(longitude))
print(latitude)
# print(type(latitude))

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

if (latitude > (latitude - 5) or latitude < (latitude + 5)) and (longitude > (longitude - 5) or longitude < (longitude + 5)):
    is_close = True
    print(is_close)

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
print(sunrise)
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunset)

time_now = datetime.now()
current_hour = time_now.hour
print(current_hour)

if current_hour <= sunrise and current_hour >= sunset:
    is_dark = True
    print(is_dark)

if is_close and is_dark:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs="banerjee.sumanto08@gmail.com",
            msg="ISS overhead\n\nLook above! Iss is in the sky above you"
        )