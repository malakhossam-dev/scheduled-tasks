import datetime as dt
import pandas
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# read the file and extract data_birthday
data=pandas.read_csv("birthday_).csv")
dict_data=data.to_dict("records")


# find current day and weekday
now=dt.datetime.now()
current_day=now.day
month=now.month


# send the email and preparation message
for i in dict_data:

    if i["day"]==current_day and i["month"]==month:
        # reed file letter and preparation message
        with open("letter_templates/letter_3".txt", "r") as f:
            data=f.read()
            data=data.replace("[NAME]",i["name"])
            print(data)


        # send email
        connection=smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=i["email"],msg=f"subject:hello\n\n{data}")
        connection.close()
