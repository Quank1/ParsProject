import requests

from bs4 import BeautifulSoup
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

price_list = []
count = 0


for num in range(1, 5):


    url = f"https://www.olx.ua/uk/nedvizhimost/kvartiry/?page={num}"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find_all("div", class_="css-1sw7q4x")

    for i in data:
        sleep(1)
        try:
            area = i.find("span", class_ = "css-643j0o").text.replace("м²", "")

            if float(area) >= 50 and float(area) <= 60:
                price_find = i.find("p", class_ = "css-tyui9s er34gjf0").text.replace("Договірна", "").replace("грн.", "").replace(" ", "")

                price_list.append(float(price_find))
                count += 1
        except AttributeError:
            print("Нету цены!")


summa = sum(price_list) / count

print(f"Средняя цена квартиры 50-60 м² - {int(summa)} грн")





        


