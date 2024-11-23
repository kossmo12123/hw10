from bs4 import BeautifulSoup
import requests

def get_usd_exchange_rate():
    resourse = requests.get("https://halykbank.kz/exchange-rates")
    if resourse.status_code == 200:
        soup = BeautifulSoup(resourse.text, features="html.parser")
        soup_list = soup.find_all("div", class_="font-semibold text-2xl")
        res = soup_list[0].find("span")
        return float(res.text)
    else:
        raise Exception("error")

class CurrencyConverter:
    def __init__(self, usd_rate):
        self.usd_rate = usd_rate

    def convert_to_usd(self, local_amount):
        return local_amount / self.usd_rate


usd_rate = get_usd_exchange_rate()

converter = CurrencyConverter(usd_rate)

local_amount = float(input("Введите: "))
usd_amount = converter.convert_to_usd(local_amount)
print(f"США: {usd_amount:.2f}")



