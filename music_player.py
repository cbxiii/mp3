from tkinter import *
from tkinter import ttk
import pygame
import os

root = Tk()
root.title("music player")
root.geometry("400x600")
root.resizable(False, False)

pygame.init()
pygame.mixer.init()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, padx=10, pady=10)

playlist = Listbox(mainframe, width=40, height=20)
playlist.pack(fill=BOTH, expand=True)
playlist.bind("<<ListboxSelect>>", play_selected)

controls = ttk.Frame(root)
controls.grid(column=0, row=1, padx=10, pady=10)
controls.configure(border=1, relief="groove", borderwidth=2)

# play/pause button
play_var = StringVar()
play_var.set("Play")
play_pause_button = ttk.Button(controls, textvariable=play_var, command=play_pause)
play_pause_button.grid(column=0, row=1, padx=10, pady=10)

# rewind button
rewind_button = ttk.Button(controls, text="<<", command=rewind)
rewind_button.grid(column=0, row=2, padx=10, pady=10)

# fast forward button
fast_forward_button = ttk.Button(controls, text=">>", command=fast_forward)

# volume control
status_var = StringVar()
status_var.set("Volume Control")
status_label = ttk.Label(controls, textvariable=status_var)

volume_var = DoubleVar()
volume_scale = ttk.Scale(controls, orient="horizontal", from_=0, to=1, variable=volume_var, command=set_volume)
volume_scale.grid(column=0, row=5, padx=10, pady=10)

# import music button
import_button = ttk.Button(controls, text="Import", command=import_music)
import_button.grid(column=0, row=6, padx=10, pady=10)


"""
TODO: 
add functionality to:
- play/pause button
- rewind button
- fast forward button
- volume control
- import music button
"""

root.mainloop()