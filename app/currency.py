import requests
from bs4 import BeautifulSoup as BS

def get_usd_chy():
    url = "https://myfin.by/converter/usd-cny/1"
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    curs = soup.find("span", {"class": "converter-100__info-currency-bold"})
    return float(curs.text[:-4])

def get_usd_rub():
    url = "https://myfin.by/converter/usd-rub/1"
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    curs = soup.find("span", {"class": "converter-100__info-currency-bold"})
    return float(curs.text[:-4])

def get_usd_byn():
    url = "https://myfin.by/converter/usd-byn/1"
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    curs = soup.find("span", {"class": "converter-100__info-currency-bold"})
    return float(curs.text[:-4])
