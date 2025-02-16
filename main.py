import requests
from bs4 import BeautifulSoup
import smtplib
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://uvce.ac.in/nirf.php")

# driver.quit()






























# EMAIL = "asampletest482@gmail.com"
# PASSWORD = "wihj ospi nobv uakm"


# url = "https://appbrewery.github.io/instant_pot/"
# response = requests.get(url)
# # print(response.text)

# soup = BeautifulSoup(response.content,"html.parser")

# price = soup.find(name="span",class_="a-offscreen").get_text()
# # print(price)

# price_without_currency = price.split("$")[1]
# print(price_without_currency)

# price_as_float = float(price_without_currency)
# print(price_as_float)

# title = soup.find(name="span",id="productTitle").get_text().strip()
# print(title)

# target_price = 100.0

# if price_as_float < target_price:
#     message = f"{title} is now {price}. Buy now!"

# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(user=EMAIL,password=PASSWORD)
#     connection.sendmail(
#         from_addr=EMAIL,
#         to_addrs="prathikcoorg5@gmail.com",
#         msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode('utf-8')
#     )





# url ="https://www.flipkart.com/nike-air-max-systm-sneakers-men/p/itm676b906c81cdc?pid=SHOHFT9H3MHZEQZ9&lid=LSTSHOHFT9H3MHZEQZ9AFPFCD&marketplace=FLIPKART&q=nike+sneakers&store=osp&srno=s_1_7&otracker=AS_Query_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_1_4_na_na_na&fm=search-autosuggest&iid=168a8aea-fbd7-4789-9be4-a1b806b41e7b.SHOHFT9H3MHZEQZ9.SEARCH&ppt=sp&ppn=sp&ssid=zt4we1vgu80000001736579488091&qH=08d4271ac333c7c9"


# headers = {
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
#           "Accept-Language": "en-US,en;q=0.9,kn;q=0.8", 

# }

# response = requests.get(url)
# # print(response.text)

# soup = BeautifulSoup(response.content,"html.parser")
# price = soup.find("div",class_="UOCQB1")
# print(price.text)

# title= soup.find("span",class_="VU-ZEz").text
# print("\n",title)

# # product_details = soup.find("div",class_="col col-11-12 rYpYQA").text
# # print(product_details)              

# details = soup.find_all("div",class_="_4aGEkW")
# print("\n",details[0].text)

# image = soup.find("img",class_="_53J4C- utBuJY")
# print("\n",image.get("src"))
























# headers= {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
#         "Accept-Encoding": "gzip, deflate, br, zstd", 
#         "Accept-Language": "en-US,en;q=0.9,kn;q=0.8", 
#         "Host": "httpbin.org", 
#         "Priority": "u=0, i", 
#         "Sec-Ch-Ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
#         "Sec-Ch-Ua-Mobile": "?0", 
#         "Sec-Ch-Ua-Platform": "\"Windows\"", 
#         "Sec-Fetch-Dest": "document", 
#         "Sec-Fetch-Mode": "navigate", 
#         "Sec-Fetch-Site": "cross-site", 
#         "Sec-Fetch-User": "?1", 
#         "Upgrade-Insecure-Requests": "1", 
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36", 
#         "X-Amzn-Trace-Id": "Root=1-67800cbb-6facddd229e36e824ee1e2b8"
#          }

# headers = {
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
#           "Accept-Language": "en-US,en;q=0.9,kn;q=0.8", 

# }
