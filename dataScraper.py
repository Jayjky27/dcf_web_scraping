from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import requests
from bs4 import BeautifulSoup
import numpy as np
from itertools import zip_longest

class DataScraper:
    def __init__(self):
        self.ticker = ""
        self.urlCashflow = ""
        self.urlBalanceSheet = ""
        self.urlKeyStatistics = ""
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
        self.cashAndEquivalents = 0
        self.totalDebt = 0
        self.equityValue = 0
        self.sharesOutstanding = 0

    def set_Ticker(self, ticker):
        self.ticker = ticker

    def get_Ticker(self):
        return self.ticker

    def fetchData(self):
        # *******************************************
        # Scrap data from CashFlow statement
        # *******************************************
        self.urlCashflow = f"https://finance.yahoo.com/quote/{self.ticker}/cash-flow"
        self.urlBalanceSheet = f"https://finance.yahoo.com/quote/{self.ticker}/balance-sheet/"
        self.urlKeyStatistics = f"https://finance.yahoo.com/quote/{self.ticker}/key-statistics/"
        try:
            page = requests.get(self.urlCashflow, headers=self.header)
            if page.status_code == 200:
                self.parseDataCashflow(page.text)
            else:
                print('ERROR: Nepodařilo se načíst data')
        except Exception as e:
            print(f'ERROR: Chyba při načítání dat: {e}')

        # *******************************************
        # Scrap data from CashFlow statement
        # *******************************************
        self.parseDataBalanceSheet()

        # *******************************************
        # Scrap data from Key statistic
        # *******************************************
        try:
            page = requests.get(self.urlKeyStatistics, headers=self.header)
            if page.status_code == 200:
                self._parseSharesOutstanding(page.text)
            else:
                print('ERROR: Nepodařilo se načíst data')
        except Exception as e:
            print(f'ERROR: Chyba při načítání dat: {e}')

    def parseDataCashflow(self, html):
        soup = BeautifulSoup(html, "html.parser") # Celá stránka

        # PARSE FREE CASHFLOW VALUES
        self._parseFreeCashflowsValues(soup)

        # GROWTH OF FREECASHFLOW VALUES + AVERAGE GROWTH RATE
        self.calculateGrowthRates()

        # CALCULATE FUTURE CASHFLOW VALUES
        self.calculateFutureFreeCashflows()

        self.terminalValue = round(self.futureFreeCashflows[8] * (1 + self.perpetualGrowthRate/100) / (self.discountRate/100 - self.perpetualGrowthRate/100))

        # CALCULATE PV of FFCF VALUES
        self.calculatePVFFCFValues()

        print(self.sumFCF)

    def parseDataBalanceSheet(self):
        # **************************************************
        # Cash and Cash Equivalents
        # **************************************************
        service = Service(executable_path='chromedriver.exe')
        driver = webdriver.Chrome(service=service)

        driver.get(self.urlBalanceSheet)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME,'reject'))).click() # Reject cookies button

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Total Assets']"))).click() # Expand button Total assets

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Current Assets']"))).click() # Expand button Current assets

        html = driver.page_source # Získání HTM kódu stránky pro beautiful soup

        # Parse Cash and Cash Equivalents
        table = self._parseCashAndEquivalents(html)

        # Parse Total Debt
        self._parseTotalDebt(table)

        # **************************************************
        # Equity value
        # **************************************************
        self.equityValue = self.sumFCF + self.cashAndEquivalents - self.totalDebt

        print(self.totalDebt)

        driver.quit()

    def _parseSharesOutstanding(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        column = soup.find_all('div', class_='column yf-14j5zka')[-1]
        rows = column.find_all('td', class_='label yf-vaowmx')

        for current_row in rows:
            if 'Shares Outstanding' in current_row.text:
               row = current_row
        
        row_parent = row.parent

        self.sharesOutstanding = row_parent.find('td', class_='value yf-vaowmx')
        
        print(self.sharesOutstanding)



    def _parseCashAndEquivalents(self, html):
        soup = BeautifulSoup(html, 'html.parser') # Parsování

        table = soup.find('div',class_='table yf-9ft13') # Tabulka

        row = table.find('div',class_='row lv-2 yf-t22klz') # Řádek

        self.cashAndEquivalents = row.find('div', class_='column yf-t22klz alt') # získání hodnoty
        self.cashAndEquivalents = self.cashAndEquivalents.text.strip() 
        self.cashAndEquivalents = round(float(self.cashAndEquivalents.replace(',','')))/1000

        return table

    def _parseTotalDebt(self, table):
        rows = table.find_all('div', class_='rowTitle yf-t22klz') # Získání všech DIV elementů

        # Nalezení konkrétního DIV (Total Debt DIV)
        for row in rows:
            if 'Total Debt' in row.text:
                row1 = row

        row = row1.parent # Získání DIV elementu o úroveň výše
        row = row.parent # Získání DIV elementu o úroveň výše (Celý řádek tabulky)
                
        self.totalDebt = row.find('div', class_='column yf-t22klz alt')
        self.totalDebt = self.totalDebt.text.strip()
        self.totalDebt = float(self.totalDebt.replace(',',''))/1000

    def _parseFreeCashflowsValues(self, soup):
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

