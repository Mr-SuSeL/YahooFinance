import tkinter as tk
import yfinance as yf

window = tk.Tk()
window.title("Stock info")

scrollbar = tk.Scrollbar(window)
textBox = tk.Text(window, height=10, width=70, padx=5, pady=5, font="Helvetica 12")
scrollbar.pack(side=tk.RIGHT, fill = tk.Y)
textBox.pack(expand=True, fill=tk.BOTH)

scrollbar.config(command=textBox.yview)
textBox.config(yscrollcommand=scrollbar.set)



window.mainloop()