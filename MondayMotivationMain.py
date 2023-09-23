# import smtplib
# email = "pythontest20000@gmail.com"
# password = "quiwkxuveovkdbaw"
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(from_addr=email,
#                         to_addrs="pythontest20000@yahoo.com",
#                         msg="Subject: SMTP email\n\nThis is my first email\nBlah Blah")

# import datetime
#
# now = datetime.datetime.now()
# print(now)
# year = now.year
# month = now.month
# day = now.day
# print(year)
# print(month)
# print(day)
# print(now.date())
# dob = datetime.datetime(year=1989, month=8, day=3, hour=17, minute=31)
# print(dob)

import random
import smtplib
import datetime as dt

with open("quotes.txt", mode="r", encoding="utf8") as quotes:
    data = quotes.readlines()
    # print(data)
    random_data = random.choice(data).encode("UTF-8")
    #print(random_data)
    date = dt.datetime.now()
    print(date.weekday())
    if date.weekday() == 0:
        email = "YOUR EMAIL"
        password = "XYZ"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email,
                            to_addrs="XYZ@yahoo.com",
                            msg=f"Subject: Monday motivation\n\n{random_data}")
