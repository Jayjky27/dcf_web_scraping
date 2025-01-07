from dataScraper import DataScraper
from build.gui import MyGui
from tkinter import Tk

#***************************************************************
# APP
#***************************************************************
def main():
    scraper = DataScraper('MSFT')
    scraper.fetchData()

if __name__ == '__main__':
    root = Tk()
    app = MyGui(root)
    root.mainloop()


