import tkinter as tk
from tkinter import font as tk_font

"""
('fangsong ti', 'fixed', 'clearlyu alternate glyphs', 'courier 10 pitch', 'open look glyph', 'bitstream charter', 'song ti', 'open look cursor', 'newspaper', 'clearlyu ligature', 'mincho', 'clearlyu devangari extra', 'clearlyu pua', 'clearlyu', 'clean', 'nil', 'clearlyu arabic', 'clearlyu devanagari', 'gothic', 'clearlyu arabic extra')

"""
window = tk.Tk()
ft = tk_font.Font(family="song ti", size=20, weight=tk_font.BOLD)
window.resizable(0, 0)
window.attributes("-topmost", 1)


def on_closing():
    msgList.delete(0, tk.END)
    window.withdraw()


print(tk_font.families())
msgList = tk.Listbox(window, font=ft)
button = tk.Button(window, text="天下大事为我所控gosayimasi", font=ft, command=on_closing)
msgList.pack(fill=tk.BOTH)
button.pack(fill=tk.BOTH)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
