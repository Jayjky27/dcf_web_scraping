from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtGui import QColor, QBrush, QFont

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("gui_design.ui", self)
        self.show()

    def loadDataToTable1(self, data):
        # Nastavení počtu řádků a sloupců podle vstupních dat
        self.freeCashflow_table.setRowCount(len(data))
        self.freeCashflow_table.setColumnCount(len(data[0]))

        # *************************************************************
        # Nastavení fontu hlavičky 1. tabulky Free Cashflows
        # *************************************************************
        # Nastavení fontu
        fnt = QFont()
        fnt.setBold(True)
        fnt.setPointSize(11)

        # Nastavení barvy
        color_tableHeader = QColor()
        color_tableHeader.setRed(255)
        color_tableHeader.setGreen(189)
        color_tableHeader.setBlue(90)

        year = 2021
        for i in range(0, 4):
            item = QtWidgets.QTableWidgetItem(str(year))
            item.setForeground(QtGui.QColor(color_tableHeader))
            item.setFont(fnt)
            self.freeCashflow_table.setHorizontalHeaderItem(i, item)
            year += 1
        
        # Naplnění tabulky daty
        for row in range(len(data)):
            for col in range(len(data[row])):
                if row == 1:
                    item = QTableWidgetItem(str(data[row][col]))  # Převod na řetězec
                    self.freeCashflow_table.setItem(row, col+1, item)
                else:
                    item = QTableWidgetItem(str(data[row][col]))  # Převod na řetězec
                    self.freeCashflow_table.setItem(row, col, item)

    def loadDataToTable2(self, val1, val2):
        # Nastavení řádků a sloupců
        self.growthRate_table.setRowCount(2)
        self.growthRate_table.setColumnCount(1)

        item = QTableWidgetItem(str(val1))
        self.growthRate_table.setItem(0, 0, item)

        item = QTableWidgetItem(str(val2))
        self.growthRate_table.setItem(1,0,item)

    def loadDataToTable3(self, data):
    # Nastavení počtu řádků a sloupců podle vstupních dat
        self.futureCashflow_table.setRowCount(len(data))
        self.futureCashflow_table.setColumnCount(len(data[0]))

        # *************************************************************
        # Nastavení fontu hlavičky 3. tabulky Future Free Cashflows
        # *************************************************************
        # Nastavení fontu
        fnt = QFont()
        fnt.setBold(True)
        fnt.setPointSize(11)

        # Nastavení barvy
        color_tableHeader = QColor()
        color_tableHeader.setRed(255)
        color_tableHeader.setGreen(189)
        color_tableHeader.setBlue(90)

        # Vypsání hlavičky do tabulky
        year = 2025
        for i in range(0, 9):
            item = QtWidgets.QTableWidgetItem(str(year))
            item.setForeground(QtGui.QColor(color_tableHeader))
            item.setFont(fnt)
            self.futureCashflow_table.setHorizontalHeaderItem(i,item)
            year += 1    


        # Naplnění tabulky daty
        for row in range(len(data)):
            for col in range(len(data[row])):
                if row == 1:
                    item = QTableWidgetItem(str(data[row][col]))  # Převod na řetězec
                    self.futureCashflow_table.setItem(row, col, item)
                else:
                    item = QTableWidgetItem(str(data[row][col]))  # Převod na řetězec
                    self.futureCashflow_table.setItem(row, col, item)

    def loadDataToTable4(self, val1, val2):
        self.growthRate_table2.setRowCount(2)
        self.growthRate_table2.setColumnCount(1)

        item = QTableWidgetItem(str(val1))
        self.growthRate_table2.setItem(0, 0, item)

        item = QTableWidgetItem(str(val2))
        self.growthRate_table2.setItem(1, 0, item)

    def loadDataToTable5(self, data):
        self.dcfValue_table.setRowCount(6)
        self.dcfValue_table.setColumnCount(1)

        for row in range(len(data)):
            item = QTableWidgetItem(str(data[row]))
            self.dcfValue_table.setItem(row, 0, item)

    def loadDataToTable6(self, val1, val2):
        self.currentPrice_table.setRowCount(2)
        self.currentPrice_table.setColumnCount(1)

        item = QTableWidgetItem(str(val1))
        self.currentPrice_table.setItem(0, 0, item)

        item = QTableWidgetItem(str(val2))
        self.currentPrice_table.setItem(1, 0, item)

