from PyQt5.QtWidgets import QApplication
import mygui
import requests
from bs4 import BeautifulSoup
import numpy as np
from itertools import zip_longest

# COMMON USER AGENT 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'
}

# CONNECTING
page = requests.get('https://finance.yahoo.com/quote/MSFT/cash-flow/', headers=headers2)
print("Status:" + str(page.status_code))   # vypsaní statusu o připojení ke stránce

# PARSOVÁNÍ STRINGU HTML DAT
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('div', class_='tableBody yf-9ft13')
row = table.find_all('div', class_='row lv-0 yf-t22klz')[9]

columns = row.find_all('div', class_='column yf-t22klz')
columns_alt = row.find_all('div', class_='column yf-t22klz alt') 

# *******************************************************************
# Extrahovat text a uložit do seznamu
# *******************************************************************
# Free Cashflow hodnoty od roku 2021 do 2024
values = [col.text.strip() for col in columns]
values_alt = [col.text.strip() for col in columns_alt]
values_all = list(zip_longest(values_alt, values, fillvalue=None))
values_all = [val for pair in values_all for val in pair]
values_all.pop() # odstranění posledního elementu z listu (hodnota NONE)
freeCashFlow_values = [float(value.replace(',', '')) for value in values_all]
freeCashFlow_values = freeCashFlow_values[::-1]
freeCashFlow_values.pop()
freeCashFlow_values = [value / 1000 for value in freeCashFlow_values]

# Růst Free Cashflow v %
growth_values = []
i = 0

for x in freeCashFlow_values:
    if i != 0:
        growth = ((x - temp)/temp) * 100
        growth_values.append(growth)
    temp = x
    i += 1

growth_values = [round(value, 2) for value in growth_values]

#Average growth rate (%)
pom = 0
for x in growth_values:
    pom += x

averageGrowthRate_value = round((pom / len(growth_values)), 2)

# Growth rate (Zadává user)
growthRate = 13 # pro testing zadano 13 %
futureFreeCashflow_values = [0] * 9

# Future Cashflows 
for i in range(0, 9):
    if i == 0:
        futureFreeCashflow_values[i] = freeCashFlow_values[3] * (growthRate/100 + 1)
    else:
        futureFreeCashflow_values[i] = futureFreeCashflow_values[i-1] * (growthRate/100 + 1)

futureFreeCashflow_values = [round(value) for value in futureFreeCashflow_values]

# Perpetual Growth Rate, Discount Rate (WACC) -> Zadava user
perpetualGrowthRate = 2.5 # [%]
discountRate = 9 # [%] 8 - 12 %

# PV of FFCF
pvffcf_values = []
i = 1
for value in futureFreeCashflow_values:
    pvffcf_values.append(round(value / ((discountRate/100 + 1)**i)))
    i += 1


# Terminal Value
terminalValue = round(futureFreeCashflow_values[8] * (1 + perpetualGrowthRate/100) / (discountRate/100 - perpetualGrowthRate/100))

pvffcf_values.append(terminalValue / ((discountRate/100 + 1)**i))
pvffcf_values = [round(val) for val in pvffcf_values]

sumOfFCF = 0
for val in pvffcf_values:
    sumOfFCF += val

terminalValuePVFFCF = pvffcf_values[9]

# Cash and Cash equivalents, Total Debt - získá se z web stránky (Zatím pouze manuálně)
cashAndEquivalents = 75531 
totalDebt = 67127

# Equity value
equityValue = sumOfFCF + cashAndEquivalents - totalDebt

# Outstanding shares - získá se z web stránky (zatím pouze manuálně)
sharesOutstanding = 7430

# DCF price per share
dcfPricePerShare = round(equityValue / sharesOutstanding, 2)

# Current prize + Difference from DCF prize per share
table = soup.find('div', class_='container yf-aay0dk') 
div_elements = table.find('span')
div_elements = div_elements.text.strip()
div_elements.replace('.','')
currentPrice = float(div_elements)

difference = round(((dcfPricePerShare - currentPrice)/currentPrice) * 100, 2)

# *******************************************************************
# Příprava dat do tabluky
# *******************************************************************
tab1 = [] # Free Cashflows + growth rate tabulka
tab1.append(freeCashFlow_values)
tab1.append(growth_values)

futureFreeCashflow_values.append(terminalValue)
tab3 = [] # Future Cashflows + PV of FFCF
tab3.append(futureFreeCashflow_values)
tab3.append(pvffcf_values)

tab5 = []
tab5.append(sumOfFCF)
tab5.append(cashAndEquivalents)
tab5.append(totalDebt)
tab5.append(equityValue)
tab5.append(sharesOutstanding)
tab5.append(dcfPricePerShare)


# Výpisy do konzole
print('FreeCashflow: '+ str(freeCashFlow_values))
print('Growth rate: '+ str(growth_values))
print('Average Growth Rate: ' + str(averageGrowthRate_value))
print('Future Free Cashflow: ' + str(futureFreeCashflow_values))
print('PV of FFCF values: ' + str(pvffcf_values))
print('Terminal value: ' + str(terminalValue))
print('Terminal PVFFCF value: ' + str(terminalValuePVFFCF))
print('Sum of FCF: ' + str(sumOfFCF))
print('Equity value: ' + str(equityValue))
print('DCF price per share: ' + str(dcfPricePerShare))

'''
element = table.find_next('div', class_='column yf-t22klz alt')
while True:
    element = table.find_next('div', class_='column yf-t22klz alt')
    if element is None:
        break
    values.append(element.text.strip())

span = row.find_all("div", class_='column yf-t22klz alt')[2].text

print('SPAN: ' + str(span))
print(values)
'''

#***************************************************************
# APP
#***************************************************************
def main():
    app = QApplication([])
    window = mygui.MyGUI()
    window.loadDataToTable1(tab1)
    window.loadDataToTable2(growthRate, averageGrowthRate_value)
    window.loadDataToTable3(tab3)
    window.loadDataToTable4(perpetualGrowthRate, discountRate)
    window.loadDataToTable5(tab5)
    window.loadDataToTable6(currentPrice, difference)
    app.exec_()

if __name__ == '__main__':
    main()
