import requests
from bs4 import BeautifulSoup
import smtplib
from selenium import webdriver


EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"


url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.content,"html.parser")

price = soup.find(name="span",class_="a-offscreen").get_text()
# print(price)

price_without_currency = price.split("$")[1]
print(price_without_currency)

price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(name="span",id="productTitle").get_text().strip()
print(title)

target_price = 100.0

if price_as_float < target_price:
    message = f"{title} is now {price}. Buy now!"

with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    connection.login(user=EMAIL,password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs="EMAIL",
        msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode('utf-8')
    )


