import requests
from bs4 import BeautifulSoup

class DataScraper:
    def __init__(self, ticker):
        self.ticker = ticker
        self.base_url = f"https://finance.yahoo.com/quote/{ticker}/cash-flow"
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}
        self.dataFreeCashflows = []

    def fetchData(self):
        try:
            page = requests.get(self.base_url, headers=self.header)
            if page.status_code == 200:
                self.parseData(page.text)
            else:
                print('ERROR: Nepodařilo se načíst data')
        except Exception as e:
            print(f'ERROR: Chyba při načítání dat: {e}')

    def parseData(self, html):
        soup = BeautifulSoup(html, "html.parser") # Celá stránka
        table = soup.find('div', class_='tableBody yf-9ft13') # Tabulka
        rows = table.find_all('div', class_='row lv-0 yf-t22klz')
        last_row = rows[-1]
        print(last_row)

    def getData(self):
        # return self.data
        pass
