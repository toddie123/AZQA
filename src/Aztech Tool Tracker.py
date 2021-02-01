"""""
Aztech Locknut Company Tool Tracker Program
This program is licensed to Aztech Engineering Inc. and its subsidiaries

Written by Todd Kuebelbeck, 2021 developed at and for Aztech Locknut Company
--------------------------------------------------------------------------------
Main class that contains GUI
"""""

import tkinter
from tkinter import ttk
from tkinter import PhotoImage
from PIL import ImageTk,Image

def main():
    tool_input = input('Input tool ID')




root = tkinter.Tk()

root.title("Aztech Tool Tracker")

main_frame = ttk.Frame(root, padding = 10)
logo_frame = ttk.Frame(root, bg = 'white', width = 196, height = 196)
title_frame = ttk.Frame(root, bg = 'white', width = 300, height = 196)


logo_frame.grid(row=0, col=0)
title_frame.grid(row=0, col=1)
main_frame.grid(row=1, col=0)

logo = Image.open("aztech logo.PNG")
photo = ImageTk.PhotoImage(logo.resize((196, 196), Image.ANTIALIAS))

logo_label = ttk.Label(logo_frame, image=photo, bg='white')
logo_label.image = photo
logo_label.pack()


