import smtplib
import datetime
import pandas
import random

c = []
with open("quotes.txt") as a:
    for b in a:
        c.append(b)

a = smtplib.SMTP("smtp.gmail.com", 587)
a.starttls()
a.login("obadah2109@gmail.com", "nyiliysupagfwsdj")
b = datetime.datetime.now()
if b.weekday() == 1:
    a.sendmail("obadah2109@gmail.com", "obadah272@gmail.com", f"Subject: Famous quotes\n\n{random.choice(c)}")