import requests
from bs4 import BeautifulSoup as bs

if __name__ == "__main__":
    url = "https://www.esportsearnings.com/history/2022/countries"
    page = requests.get(url)
    soup = bs(page.text, "html.parser")

    countryObjects = soup.select('tr.format_row')

    with open('res.csv', 'w', encoding='UTF-8') as f:
        f.write("순위,국가,상금,선수 수" + '\n') # header
        for obj in countryObjects:
            rankNum = obj.select_one('td.detail_list_order').text[:-1]
            countryName = obj.select_one('td.detail_list_player').text.replace(',', '')

            # 상금이랑 선수 수가 같은 클래스로 되어있으므로 배열로 받고 쪼갠다.
            prizeObjects = obj.select('td.detail_list_prize')
            prize = prizeObjects[0].text[1:].replace(',', '')
            numOfPlayers = prizeObjects[1].text[:-8]

            print(rankNum, countryName, prize, numOfPlayers)
            f.write(rankNum + "," + countryName + "," + prize + "," + numOfPlayers + '\n')