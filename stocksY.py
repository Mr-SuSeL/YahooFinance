import tkinter as tk
import yfinance as yf
import pandas as pd

window = tk.Tk()
window.title("Stock info")

# Kontener interfejsu
topWidget = tk.Frame(window)
label = tk.Label(topWidget, text="Stock ticker:")
label.pack(side=tk.LEFT)
entry = tk.Entry(topWidget)
entry.pack(side=tk.RIGHT)
topWidget.pack() # dodane na samej górze


scrollbar = tk.Scrollbar(window)
textBox = tk.Text(window, height=35, width=80, padx=5, pady=5, font="Helvetica 12")
scrollbar.pack(side=tk.RIGHT, fill = tk.Y)
textBox.pack(expand=True, fill=tk.BOTH)

scrollbar.config(command=textBox.yview)
textBox.config(yscrollcommand=scrollbar.set)

# Pobieramy dane z serwera za pomocą Yahoo Finance
def download_data(e):
    textBox.delete("1.0", tk.END)
    stock = str(e.widget.get())
    
    if not stock:
        print("No stock choosen")
        return
    
    stock = stock.upper().strip()
    # stock = str(stock)
    print("Data downloaded for stock:", stock)

    stockData = yf.Ticker(stock)
    # Zmiany w API z .info na .fast_info
    print(stockData.fast_info)

    stockKeys = ['currency', 'dayHigh', 'dayLow', 'exchange', 'fiftyDayAverage', 
    'lastPrice', 'lastVolume', 'marketCap', 'open', 'previousClose', 'quoteType', 
    'regularMarketPreviousClose', 'shares', 'tenDayAverageVolume', 'threeMonthAverageVolume', 
    'timezone', 'twoHundredDayAverage', 'yearChange', 'yearHigh', 'yearLow']

    textBox.insert(tk.END, "Ticker: " + stock + " \n\n")

    for key in stockKeys:
        try:
            v = str(key) + " : " + stockData.fast_info[str(key)] + " \n\n"
            textBox.insert(tk.END, v)
        except:
            pass
    history = stockData.history(period="1mo", interval="1d")
    textBox.insert(tk.END, history)

entry.bind("<Return>", download_data)

window.mainloop()