import smtplib
import datetime as dt
import random

# Load in quotes
quotes_file = open("quotes.txt", "r")
quotes = quotes_file.readlines()

# Get current datetime
now = dt.datetime.now()

# If it is monday, send motivational email
if now.weekday() == 0:
    my_email = "me@email.com"
    password = "password"

    with smtplib.SMTP("smtp.live.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg="Subject:Happy monday!\n\n "
                                f"{random.choice(quotes)}")
