# -*- coding: utf-8 -*-

import tkinter as tk

root = tk.Tk()
root.geometry('600x600')

launch_browser = tk.Button(root, text='Launch Browser')
quit_app = tk.Button(root, text='Quit App')
blitz_app = tk.Button(root, text='Blitz (5+5)')
play_cpu = tk.Button(root, text='Play vs stockfish')
show_prev_moves = tk.Button(root, text='Previous moves')

# Canvases
previous_moves_canvas = tk.Canvas(root, height=200, width=200, bg='blue')

launch_browser.grid(row=2, column=5)
quit_app.grid(row=0, column=0, rowspan=2, columnspan=1)
blitz_app.grid(row=3, column=, columnspan=1)
play_cpu.grid(row=3, column=6, columnspan=1)
show_prev_moves.grid(row=1, column=6)
previous_moves_canvas.grid(row=2, column=6)

root.mainloop()