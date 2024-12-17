from PyQt5 import QtWidgets
import requests
from bs4 import BeautifulSoup
import numpy as np
from itertools import zip_longest

# COMMON USER AGENT 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# CONNECTING
page = requests.get('https://finance.yahoo.com/quote/MSFT/cash-flow/', headers=headers)
print("Status:" + str(page.status_code))   # vypsaní statusu o připojení ke stránce

# PARSOVÁNÍ STRINGU HTML DAT
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('div', class_='tableBody yf-9ft13')
row = table.find_all('div', class_='row lv-0 yf-t22klz')[9]

columns = row.find_all('div', class_='column yf-t22klz')
columns_alt = row.find_all('div', class_='column yf-t22klz alt') 

# Extrahovat text a uložit do seznamu
values = [col.text.strip() for col in columns]
values_alt = [col.text.strip() for col in columns_alt]
values_all = list(zip_longest(values_alt, values, fillvalue=None))
values_all = [val for pair in values_all for val in pair]
values_all.pop() # odstranění posledního elementu z listu (hodnota NONE)
freeCashFlow_values = values_all

print(freeCashFlow_values)


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
'''
app = QtWidgets.QApplication([])

button = QtWidgets.QPushButton("Click to Exit")
button.setWindowTitle("Goodbye World")
button.clicked.connect(app.quit)

button.show()

app.exec()
'''