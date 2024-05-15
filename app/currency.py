import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup as BS
import json
import schedule

headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
def get_usd_chy():
    url = "https://www.bestchange.com/tether-trc20-to-alipay.html"

    r = requests.get(url, headers=headers)
    soup = BS(r.text, "lxml")
    curs = soup.find_all("td", class_="bi")
    ya = curs[1].text
    return float(ya[:6])

def get_usd_rub():
    url = "https://myfin.by/converter/usd-rub/1"
    r = requests.get(url, headers=headers)
    soup = BS(r.text, 'lxml')
    curs = soup.find("span", {"class": "converter-100__info-currency-bold"})
    return float(curs.text[:-4])

def get_usd_byn():
    url = "https://myfin.by/converter/usd-byn/1"
    r = requests.get(url, headers=headers)
    soup = BS(r.text, 'lxml')
    curs = soup.find("span", {"class": "converter-100__info-currency-bold"})
    return float(curs.text[:-4])

def update_currs():
    dict = {
        "usd_chy": get_usd_chy(),
        "usd_rub": get_usd_rub(),
        "usd_byn": get_usd_byn(),
        "datetime": str(datetime.now())
    }
    with open("data.json", "w") as f:
        json.dump(dict, f)

update_currs()
schedule.every(4).hours.do(update_currs)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except:
        print("Программа остановленна")
        break