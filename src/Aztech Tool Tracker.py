"""""
Aztech Locknut Company Tool Tracker Program
This program is licensed to Aztech Engineering Inc. and its subsidiaries

Written by Todd Kuebelbeck, 2021 developed at and for Aztech Locknut Company
--------------------------------------------------------------------------------
Main class that contains GUI
"""""

from __future__ import absolute_import  # updated importing tools for python v3.x.x
from .azqa_toolhelper import Tool   # import the Tool helper class
import tkinter
from tkinter import ttk

import webbrowser

from PIL import ImageTk, Image

# TODO: Add filepath for spreadsheet
spread_path = ''


def main():

    tool_input = input('Input tool ID')

    new_tool = Tool(tool_input, spread_path)

    new_tool.find_row()
    new_tool.set_tool_info()

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
    title = ttk.Label(title_frame, text="Aztech Tool Tracker", size='65')

    title.pack()
    logo_label = ttk.Label(logo_frame, image=photo, bg='white')
    logo_label.image = photo
    logo_label.pack()

    tool_id_label = ttk.Label(main_frame, text="Tool ID: " + new_tool.ID)
    tool_description_label = ttk.Label(main_frame, text="Tool Type: " + new_tool.tool_type)
    tool_cal_date_label = ttk.Label(main_frame, text="Date of Calibration: " + new_tool.cal_date)
    tool_cal_exp_label = ttk.Label(main_frame, text="Date of Calibration Expiration: " + new_tool.cal_exp)
    tool_use_no = ttk.Label(main_frame, text="Number of times used: " + new_tool.use + "/" + new_tool.use_limit)

    tool_id_label.grid(row=0, col=0)
    tool_id_label.pack()
    tool_description_label.grid(row=0, col=1)
    tool_description_label.pack()
    tool_cal_date_label.grid(row=1, col=0)
    tool_cal_date_label.pack()
    tool_cal_exp_label.grid(row=1, col=1)
    tool_cal_exp_label.pack()
    tool_use_no.grid(row=2, col=0)
    tool_use_no.pack()

    cert_button = ttk.Button(main_frame, text="Open " + new_tool.ID + " Calibration Certificate")
    cert_button.grid(row=3, col=0)
    cert_button['command'] = lambda: webbrowser.open_new(new_tool.cert_path)


