from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import sys
import os

# Přidání kořenové složky projektu do sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataScraper import DataScraper

class MyGui:
    def __init__(self, root):
        self.root = root
        self.scraper = DataScraper()  # Inicializace instance DataScraper

        # Nastavení okna
        self.root.geometry("710x490")
        self.root.configure(bg="#FFFFFF")
        self.root.resizable(False, False)

        # Cesta k assets
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\ferrit_electric\python\dcf_project\build\assets\frame0")

        # Canvas
        self.canvas = Canvas(
            self.root,
            bg="#f7f7f7",
            height=490,
            width=710,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # GUI komponenty
        self.create_widgets()

    def relative_to_assets(self, path: str) -> Path:
        """Pomocná metoda pro práci s cestami k assets."""
        return self.ASSETS_PATH / Path(path)

    def create_widgets(self):

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            197.0,
            60.0,
            514.0,
            136.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_text(
            166.0,
            15.0,
            anchor="nw",
            text="DCF Model Calculation",
            fill="#080808",
            font=("Inter Bold", 36 * -1)
        )

        self.canvas.create_text(
            208.0,
            65.0,
            anchor="nw",
            text="Previous years:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            12.0,
            65.0,
            anchor="nw",
            text="Ticker:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            203.0,
            88.0,
            anchor="nw",
            text="Free Cashflows:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            258.0,
            111.0,
            anchor="nw",
            text="Growth:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            322.0,
            65.0,
            anchor="nw",
            text="2021",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            370.0,
            65.0,
            anchor="nw",
            text="2022",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            420.0,
            65.0,
            anchor="nw",
            text="2023",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            470.0,
            65.0,
            anchor="nw",
            text="2024",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_rectangle(
            11.0,
            159.0,
            699.0,
            235.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            11.0,
            256.0,
            249.0,
            365.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_text(
            38.0,
            164.0,
            anchor="nw",
            text="Future years:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            93.0,
            263.0,
            anchor="nw",
            text="Growth Rate:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            52.0,
            289.0,
            anchor="nw",
            text="Growth Rate (Avg):",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            23.0,
            315.0,
            anchor="nw",
            text="Perpetual Growth Rate:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            22.0,
            341.0,
            anchor="nw",
            text="Discount Rate (WACC):",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            17.0,
            187.0,
            anchor="nw",
            text="Free Cashflows:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            48.0,
            210.0,
            anchor="nw",
            text="PV of FFCF:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            136.0,
            164.0,
            anchor="nw",
            text="2025",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            186.0,
            164.0,
            anchor="nw",
            text="2026",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            236.0,
            164.0,
            anchor="nw",
            text="2027",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            285.0,
            164.0,
            anchor="nw",
            text="2028",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            335.0,
            164.0,
            anchor="nw",
            text="2029",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            385.0,
            164.0,
            anchor="nw",
            text="2030",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            436.0,
            164.0,
            anchor="nw",
            text="2031",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            484.0,
            164.0,
            anchor="nw",
            text="2032",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            534.0,
            164.0,
            anchor="nw",
            text="2033",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            585.0,
            164.0,
            anchor="nw",
            text="Terminal Value",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            340.0,
            93.5,
            image=self.entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=322.0,
            y=85.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            489.0,
            93.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=471.0,
            y=85.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            439.0,
            93.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=421.0,
            y=85.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            389.0,
            93.5,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=371.0,
            y=85.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            155.0,
            195.5,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=137.0,
            y=187.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_6 = PhotoImage(
            file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            304.0,
            195.5,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=286.0,
            y=187.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_7 = PhotoImage(
            file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            354.0,
            195.5,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_7.place(
            x=336.0,
            y=187.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_8 = PhotoImage(
            file=self.relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(
            405.0,
            195.5,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_8.place(
            x=387.0,
            y=187.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_9 = PhotoImage(
            file=self.relative_to_assets("entry_9.png"))
        self.entry_bg_9 = self.canvas.create_image(
            454.0,
            195.5,
            image=self.entry_image_9
        )
        self.entry_9 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_9.place(
            x=436.0,
            y=187.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_10 = PhotoImage(
            file=self.relative_to_assets("entry_10.png"))
        self.entry_bg_10 = self.canvas.create_image(
            503.0,
            195.5,
            image=self.entry_image_10
        )
        self.entry_10 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_10.place(
            x=485.0,
            y=187.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_11 = PhotoImage(
            file=self.relative_to_assets("entry_11.png"))
        self.entry_bg_11 = self.canvas.create_image(
            554.0,
            195.5,
            image=self.entry_image_11
        )
        self.entry_11 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_11.place(
            x=536.0,
            y=187.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_12 = PhotoImage(
            file=self.relative_to_assets("entry_12.png"))
        self.entry_bg_12 = self.canvas.create_image(
            254.0,
            195.5,
            image=self.entry_image_12
        )
        self.entry_12 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_12.place(
            x=236.0,
            y=187.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_13 = PhotoImage(
            file=self.relative_to_assets("entry_13.png"))
        self.entry_bg_13 = self.canvas.create_image(
            205.0,
            195.5,
            image=self.entry_image_13
        )
        self.entry_13 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_13.place(
            x=187.0,
            y=187.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_14 = PhotoImage(
            file=self.relative_to_assets("entry_14.png"))
        self.entry_bg_14 = self.canvas.create_image(
            155.0,
            217.5,
            image=self.entry_image_14
        )
        self.entry_14 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_14.place(
            x=137.0,
            y=209.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_15 = PhotoImage(
            file=self.relative_to_assets("entry_15.png"))
        self.entry_bg_15 = self.canvas.create_image(
            304.0,
            217.5,
            image=self.entry_image_15
        )
        self.entry_15 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_15.place(
            x=286.0,
            y=209.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_16 = PhotoImage(
            file=self.relative_to_assets("entry_16.png"))
        self.entry_bg_16 = self.canvas.create_image(
            354.0,
            217.5,
            image=self.entry_image_16
        )
        self.entry_16 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_16.place(
            x=336.0,
            y=209.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_17 = PhotoImage(
            file=self.relative_to_assets("entry_17.png"))
        self.entry_bg_17 = self.canvas.create_image(
            405.0,
            217.5,
            image=self.entry_image_17
        )
        self.entry_17 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_17.place(
            x=387.0,
            y=209.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_18 = PhotoImage(
            file=self.relative_to_assets("entry_18.png"))
        self.entry_bg_18 = self.canvas.create_image(
            454.0,
            217.5,
            image=self.entry_image_18
        )
        self.entry_18 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_18.place(
            x=436.0,
            y=209.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_19 = PhotoImage(
            file=self.relative_to_assets("entry_19.png"))
        self.entry_bg_19 = self.canvas.create_image(
            503.0,
            217.5,
            image=self.entry_image_19
        )
        self.entry_19 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_19.place(
            x=485.0,
            y=209.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_20 = PhotoImage(
            file=self.relative_to_assets("entry_20.png"))
        self.entry_bg_20 = self.canvas.create_image(
            554.0,
            217.5,
            image=self.entry_image_20
        )
        self.entry_20 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_20.place(
            x=536.0,
            y=209.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_21 = PhotoImage(
            file=self.relative_to_assets("entry_21.png"))
        self.entry_bg_21 = self.canvas.create_image(
            637.0,
            195.5,
            image=self.entry_image_21
        )
        self.entry_21 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_21.place(
            x=619.0,
            y=187.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_22 = PhotoImage(
            file=self.relative_to_assets("entry_22.png"))
        self.entry_bg_22 = self.canvas.create_image(
            637.0,
            217.5,
            image=self.entry_image_22
        )
        self.entry_22 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_22.place(
            x=619.0,
            y=209.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_23 = PhotoImage(
            file=self.relative_to_assets("entry_23.png"))
        self.entry_bg_23 = self.canvas.create_image(
            215.0,
            271.5,
            image=self.entry_image_23
        )
        self.entry_23 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_23.place(
            x=190.0,
            y=263.0,
            width=50.0,
            height=15.0
        )

        self.entry_image_24 = PhotoImage(
            file=self.relative_to_assets("entry_24.png"))
        entry_bg_24 = self.canvas.create_image(
            215.0,
            297.5,
            image=self.entry_image_24
        )
        self.entry_24 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_24.place(
            x=190.0,
            y=289.0,
            width=50.0,
            height=15.0
        )

        self.entry_image_25 = PhotoImage(
            file=self.relative_to_assets("entry_25.png"))
        entry_bg_25 = self.canvas.create_image(
            215.0,
            323.5,
            image=self.entry_image_25
        )
        self.entry_25 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_25.place(
            x=190.0,
            y=315.0,
            width=50.0,
            height=15.0
        )

        self.entry_image_26 = PhotoImage(
            file=self.relative_to_assets("entry_26.png"))
        self.entry_bg_26 = self.canvas.create_image(
            215.0,
            349.5,
            image=self.entry_image_26
        )
        self.entry_26 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_26.place(
            x=190.0,
            y=341.0,
            width=50.0,
            height=15.0
        )

        self.canvas.create_rectangle(
            261.0,
            256.0,
            472.0,
            391.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_text(
            323.0,
            263.0,
            anchor="nw",
            text="Sum of FCF:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            269.0,
            289.0,
            anchor="nw",
            text="Cash & Equivalents:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            331.0,
            315.0,
            anchor="nw",
            text="Total Debt:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            316.0,
            341.0,
            anchor="nw",
            text="Equity Value:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.entry_image_27 = PhotoImage(
            file=self.relative_to_assets("entry_27.png"))
        self.entry_bg_27 = self.canvas.create_image(
            438.0,
            271.5,
            image=self.entry_image_27
        )
        self.entry_27 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_27.place(
            x=413.0,
            y=263.0,
            width=50.0,
            height=15.0
        )

        self.entry_image_28 = PhotoImage(
            file=self.relative_to_assets("entry_28.png"))
        self.entry_bg_28 = self.canvas.create_image(
            438.0,
            297.5,
            image=self.entry_image_28
        )
        self.entry_28 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_28.place(
            x=413.0,
            y=289.0,
            width=50.0,
            height=15.0
        )

        self.entry_image_29 = PhotoImage(
            file=self.relative_to_assets("entry_29.png"))
        self.entry_bg_29 = self.canvas.create_image(
            438.0,
            323.5,
            image=self.entry_image_29
        )
        self.entry_29 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_29.place(
            x=413.0,
            y=315.0,
            width=50.0,
            height=15.0
        )

        self.entry_image_30 = PhotoImage(
            file=self.relative_to_assets("entry_30.png"))
        self.entry_bg_30 = self.canvas.create_image(
            438.0,
            349.5,
            image=self.entry_image_30
        )
        self.entry_30 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_30.place(
            x=413.0,
            y=341.0,
            width=50.0,
            height=15.0
        )

        self.canvas.create_text(
            264.0,
            367.0,
            anchor="nw",
            text="Shares Outstanding:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.entry_image_31 = PhotoImage(
            file=self.relative_to_assets("entry_31.png"))
        self.entry_bg_31 = self.canvas.create_image(
            438.0,
            375.5,
            image=self.entry_image_31
        )
        self.entry_31 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_31.place(
            x=413.0,
            y=367.0,
            width=50.0,
            height=15.0
        )

        self.canvas.create_rectangle(
            485.0,
            256.0,
            696.0,
            367.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_text(
            490.0,
            263.0,
            anchor="nw",
            text="DCF price per share:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            534.0,
            289.0,
            anchor="nw",
            text="Current price:",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            530.0,
            315.0,
            anchor="nw",
            text="Difference ($):",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            527.0,
            341.0,
            anchor="nw",
            text="Difference (%):",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.entry_image_32 = PhotoImage(
            file=self.relative_to_assets("entry_32.png"))
        self.entry_bg_32 = self.canvas.create_image(
            662.0,
            271.5,
            image=self.entry_image_32
        )
        self.entry_32 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_32.place(
            x=637.0,
            y=263.0,
            width=50.0,
            height=15.0
        )

        self.entry_image_33 = PhotoImage(
            file=self.relative_to_assets("entry_33.png"))
        self.entry_bg_33 = self.canvas.create_image(
            662.0,
            297.5,
            image=self.entry_image_33
        )
        self.entry_33 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_33.place(
            x=637.0,
            y=289.0,
            width=50.0,
            height=15.0
        )

        self.entry_image_34 = PhotoImage(
            file=self.relative_to_assets("entry_34.png"))
        self.entry_bg_34 = self.canvas.create_image(
            662.0,
            323.5,
            image=self.entry_image_34
        )
        self.entry_34 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_34.place(
            x=637.0,
            y=315.0,
            width=50.0,
            height=15.0
        )

        self.entry_image_35 = PhotoImage(
            file=self.relative_to_assets("entry_35.png"))
        self.entry_bg_35 = self.canvas.create_image(
            662.0,
            349.5,
            image=self.entry_image_35
        )
        self.entry_35 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_35.place(
            x=637.0,
            y=341.0,
            width=50.0,
            height=15.0
        )

        self.entry_image_36 = PhotoImage(
            file=self.relative_to_assets("entry_36.png"))
        self.entry_bg_36 = self.canvas.create_image(
            254.0,
            217.5,
            image=self.entry_image_36
        )
        self.entry_36 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_36.place(
            x=236.0,
            y=209.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_37 = PhotoImage(
            file=self.relative_to_assets("entry_37.png"))
        self.entry_bg_37 = self.canvas.create_image(
            205.0,
            217.5,
            image=self.entry_image_37
        )
        self.entry_37 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_37.place(
            x=187.0,
            y=209.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_38 = PhotoImage(
            file=self.relative_to_assets("entry_38.png"))
        self.entry_bg_38 = self.canvas.create_image(
            489.0,
            120.5,
            image=self.entry_image_38
        )
        self.entry_38 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_38.place(
            x=471.0,
            y=112.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_39 = PhotoImage(
            file=self.relative_to_assets("entry_39.png"))
        self.entry_bg_39 = self.canvas.create_image(
            439.0,
            120.5,
            image=self.entry_image_39
        )
        self.entry_39 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_39.place(
            x=421.0,
            y=112.0,
            width=36.0,
            height=15.0
        )

        self.entry_image_40 = PhotoImage(
            file=self.relative_to_assets("entry_40.png"))
        self.entry_bg_40 = self.canvas.create_image(
            389.0,
            120.5,
            image=self.entry_image_40
        )
        self.entry_40 = Entry(
            bd=0,
            bg="#4D4646",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_40.place(
            x=371.0,
            y=112.0,
            width=36.0,
            height=15.0
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_1_click,
            #command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=485.0,
            y=424.0,
            width=104.0,
            height=32.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_2_click,
            relief="flat"
        )
        self.button_2.place(
            x=592.0,
            y=424.0,
            width=107.0,
            height=32.0
        )

        self.entry_image_41 = PhotoImage(
            file=self.relative_to_assets("entry_41.png"))
        self.entry_bg_41 = self.canvas.create_image(
            101.5,
            74.0,
            image=self.entry_image_41
        )
        self.entry_41 = Entry(
            bd=0,
            bg="#4E4747",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_41.place(
            x=65.0,
            y=65.0,
            width=73.0,
            height=16.0
        )

    def on_button_1_click(self):
        print('Button 1 clicked')
        self.scraper.ticker = self.entry_41.get()
        print(self.scraper.ticker)
        
        try:
            self.scraper.fetchData()
            print(self.scraper.dataFreeCashflows)
        except Exception as e:
            print('Chyba při načítání dat: ', e)

        self.entry_2.insert(0, self.scraper.dataFreeCashflows[0])
    
    def on_button_2_click(self):
        print('Button 2 clicked')

