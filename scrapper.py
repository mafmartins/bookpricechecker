#!/usr/bin/python

from lxml import html
import re
import requests
import smtplib
import sys

from settings import GMAIL_ADDRESS, GMAIL_PASSWORD


def exit_fn(msg):
    print(msg)
    exit(1)


def email_msg(subject, msg):
    return "\r\n".join(
        [
            f"Subject: {subject}",
            "",
            msg,
        ]
    )


try:
    url = sys.argv[1]
    price_limit = float(sys.argv[2])
    email = sys.argv[3]
except IndexError:
    exit_fn("ERROR: An URL is needed for pricechecking...")

page = requests.get(url)
tree = html.fromstring(page.content)

try:
    price = tree.xpath('//span[@class="sale-price"]/text()')[0]
    price_float = float(re.findall(r"\d+\,\d+", price)[0].replace(",", "."))
except IndexError:
    exit_fn(
        "ERROR: We were not able to retrieve the price,"
        " please check the url entered..."
    )

if price_float < price_limit:
    if GMAIL_ADDRESS is None:
        exit_fn("ERROR: 'GMAIL_ADDRESS' env variable is missing...")
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
        server.sendmail(
            GMAIL_ADDRESS,
            email,
            email_msg(
                "Price drop!!!",
                f"You price on the following url has gone down!!!\n\n{url}",
            ),
        )
        server.close()
    except Exception as e:
        print(e)
        exit_fn("ERROR: Something went wrong with the email notification...")
