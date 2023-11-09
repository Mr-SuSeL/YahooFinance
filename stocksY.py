import tkinter as tk
import yfinance as yf

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
textBox = tk.Text(window, height=10, width=70, padx=5, pady=5, font="Helvetica 12")
scrollbar.pack(side=tk.RIGHT, fill = tk.Y)
textBox.pack(expand=True, fill=tk.BOTH)

scrollbar.config(command=textBox.yview)
textBox.config(yscrollcommand=scrollbar.set)

# Pobieramy dane z serwera za pomocą Yahoo Finance


window.mainloop()