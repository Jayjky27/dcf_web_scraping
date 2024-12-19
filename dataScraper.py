from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
from bs4 import BeautifulSoup
import numpy as np
from itertools import zip_longest

class DataScraper:
    def __init__(self, ticker):
        self.ticker = ticker
        self.urlCashflow = f"https://finance.yahoo.com/quote/{ticker}/cash-flow"
        self.urlBalanceSheet = f"https://finance.yahoo.com/quote/{ticker}/balance-sheet/"
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}
        
        self.dataFreeCashflows = []
        self.growthOfFreeCashflows = []
        self.averageGrowthRate = 0.0
        self.userGrowthRate = 13 # Zadává user
        self.futureFreeCashflows = [0]*9
        self.perpetualGrowthRate = 2.5 # Zadává user
        self.discountRate = 9 # Zadává user
        self.PVFFCFValues = []
        self.terminalValue = 0.0
        self.terminalPVValue = 0.0
        self.sumFCF = 0

    def fetchData(self):
        try:
            page = requests.get(self.urlCashflow, headers=self.header)
            if page.status_code == 200:
                self.parseDataCashflow(page.text)
            else:
                print('ERROR: Nepodařilo se načíst data')
        except Exception as e:
            print(f'ERROR: Chyba při načítání dat: {e}')

        try:
            page = requests.get(self.urlBalanceSheet, headers=self.header)
            if page.status_code == 200:
                self.parseDataBalanceSheet(page.text)
                pass
            else:
                print('ERROR: Nepodařilo se načíst data')
        except Exception as e:
            print(f'ERROR: Chyba při načítání dat: {e}')


    def parseDataCashflow(self, html):
        soup = BeautifulSoup(html, "html.parser") # Celá stránka

        # PARSE FREE CASHFLOW VALUES
        self.parseFreeCashflowsValues(soup)

        # GROWTH OF FREECASHFLOW VALUES + AVERAGE GROWTH RATE
        self.calculateGrowthRates()

        # CALCULATE FUTURE CASHFLOW VALUES
        self.calculateFutureFreeCashflows()

        self.terminalValue = round(self.futureFreeCashflows[8] * (1 + self.perpetualGrowthRate/100) / (self.discountRate/100 - self.perpetualGrowthRate/100))

        # CALCULATE PV of FFCF VALUES
        self.calculatePVFFCFValues()

        print(self.sumFCF)

    def parseDataBalanceSheet(self, html):
        soup = BeautifulSoup(html, 'html.parser') # Celá HTML stránka


    def parseFreeCashflowsValues(self, soup):
        table = soup.find('div', class_='tableBody yf-9ft13') # Tabulka
        rows = table.find_all('div', class_='row lv-0 yf-t22klz') # Řádky tabulky
        last_row = rows[-1] # Selekce posledního řádku
        
        colums_alt = last_row.find_all('div', class_ = 'column yf-t22klz alt') # Nalezení všech hodnot na řádku s alt
        colums = last_row.find_all('div', class_ = 'column yf-t22klz') # Nalezení všech hodnot na řádku bez alt
        
        colums_alt = [col.text.strip() for col in colums_alt] # Selekce hodnot ze stringu
        colums = [col.text.strip() for col in colums] # Selekce hodnot ze stringu

        colums_alt = [float(value.replace(',',''))/1000 for value in colums_alt] # Přetypování na float
        colums = [float(value.replace(',',''))/1000 for value in colums] # Přetypování na float

        # FREE CASHFLOWS VALUES
        self.dataFreeCashflows = list(zip_longest(colums_alt, colums, fillvalue=None)) # Spojení 2 listů
        self.dataFreeCashflows = [val for pair in self.dataFreeCashflows for val in pair] # Přetypování 2D listu do 1D
        self.dataFreeCashflows.pop() # Odstranění posledního elementu z listu (element None)
        self.dataFreeCashflows = self.dataFreeCashflows[::-1] # Převrácení pořadí elementů v listu
        self.dataFreeCashflows.pop()

    def parseCashAndEquivalents(self, soup):
        table = soup.find

    def calculateGrowthRates(self):
        i = 0
        # Výpočet růstu mezi jednotlivými roky v hodnotách Free Cashflow
        for x in self.dataFreeCashflows:
            if i != 0:
                growth = ((x - temp)/temp) * 100
                self.growthOfFreeCashflows.append(growth)
            temp = x
            i += 1

        self.growthOfFreeCashflows = [round(val, 2) for val in self.growthOfFreeCashflows] # Zaokrouhlení hodnot na 2 desetinná místa

        pom = 0
        for x in self.growthOfFreeCashflows:
            pom += x
        
        self.averageGrowthRate = round((pom / len(self.growthOfFreeCashflows)), 2)
        
    def calculateFutureFreeCashflows(self):
        # Future Cashflows 
        for i in range(0, 9):
            if i == 0:
                self.futureFreeCashflows[i] = self.dataFreeCashflows[-1] * (self.userGrowthRate/100 + 1)
            else:
                self.futureFreeCashflows[i] = self.futureFreeCashflows[i-1] * (self.userGrowthRate/100 + 1)
        
        self.futureFreeCashflows = [round(val) for val in self.futureFreeCashflows]

    def calculatePVFFCFValues(self):
        i = 1
        for value in self.futureFreeCashflows:
            self.PVFFCFValues.append(value / ((self.discountRate/100 + 1)**i))
            i += 1

        self.PVFFCFValues.append(self.terminalValue / ((self.discountRate/100 + 1)**i))

        self.PVFFCFValues = [round(val) for val in self.PVFFCFValues]

        self.sumFCF = 0
        for val in self.PVFFCFValues:
            self.sumFCF += val


    def getData(self):
        # return self.data
        pass

