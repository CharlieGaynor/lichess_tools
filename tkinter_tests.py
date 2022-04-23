# -*- coding: utf-8 -*-

import tkinter as tk

root = tk.Tk()
root.geometry('600x600')

canvas = tk.Canvas(root, height=600, width=600, bg='lightblue')


bottom_left = tk.Frame(canvas, height=300, width=300)


bottom_right = tk.Frame(canvas, height=300, width=300)


top_left = tk.Frame(canvas, height=300, width=300)


top_right = tk.Frame(canvas, height=300, width=300)

canvas.grid(column=0, row=0)
bottom_left.grid(column=0, row=1)
bottom_right.grid(column=1, row=1)
top_left.grid(column=0, row=0)
top_right.grid(column=1, row=0)

launch_browser = tk.Button(top_left, text='Launch Browser')
quit_app = tk.Button(top_left, text='Quit App')
blitz_app = tk.Button(top_left, text='Blitz (5+5)')

launch_browser.grid(row=2, column=3)
quit_app.grid(row=0, column=0)
blitz_app.grid(row=5, column=2)

root.mainloop()