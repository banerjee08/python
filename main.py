##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import csv
import datetime as dt
import random
import smtplib

birthdays = []

now = dt.datetime.now()
day = now.day
month = now.month

PLACEHOLDER = "[NAME]"
new_letter = ""

my_email = "banerjee.sumanto008@gmail.com"
app_password = "afwm bbdo ftqx imvs"

with open("birthdays.csv") as bday_file:
    bday = csv.reader(bday_file)
    for row in bday:
        # print(row[0])
        if row[3] != "month" and int(row[3]) == month:
            # print("It's your birthday month")
            if row[4] != "day" and int(row[4]) == day:
                # print("It's your birthday")

                random_letter_number = random.randint(1,3)


                with open (f"./letter_templates/letter_{random_letter_number}.txt") as raw_letter:
                    letter = raw_letter.read()
                    new_letter = letter.replace(PLACEHOLDER, row[0])
                    print(type(new_letter))

                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=app_password)

                    connection.sendmail(
                        from_addr=my_email,
                        to_addrs=row[1],
                        msg=f"Subject: Birthday Greeting\n\n{new_letter}"
                    )




