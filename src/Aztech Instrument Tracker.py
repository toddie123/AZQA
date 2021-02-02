"""""
Aztech Locknut Company Instrument Tracker Program
This program is licensed to Aztech Engineering Inc. and its subsidiaries

Written by Todd Kuebelbeck, 2021 developed at and for Aztech Locknut Company
--------------------------------------------------------------------------------
Main class that contains GUI
"""""

from __future__ import absolute_import  # updated importing tools for python v3.x.x
from azqa_instrument import Tool   # import the Tool helper class
import tkinter
from tkinter import ttk

import webbrowser

from PIL import ImageTk, Image

# TODO: Add filepath for spreadsheet
spread_path = r'C:\Users\kuebeltm\OneDrive\Documents\Aztech_work\Copy of QA EQUIPMENT LIST 8-21-2020 (WIP)x(2).csv'


def main():

    tool_input = input('Input tool ID')

    # TODO remove below
    print(tool_input)


    # TODO remove below
    #webbrowser.open_new(spread_path)

    new_tool = Tool(tool_input, spread_path)

    # DONE uncommment below
    new_tool.find_row()
    new_tool.set_tool_info()

    print("confirming expiration is: " + new_tool.cal_exp)

    root = tkinter.Tk()

    root.title("Aztech Tool Tracker")

    main_frame = ttk.Frame(root, padding = 10)
    logo_frame = ttk.Frame(root, width = 50, height = 50)
    title_frame = ttk.Frame(root, width = 300, height = 196)

    logo_frame.grid(row=0, column=0)
    title_frame.grid(row=0, column=1)
    main_frame.grid(row=1, column=0)

    logo = Image.open('aztech logo.png')
    photo = ImageTk.PhotoImage(logo)
    title = ttk.Label(title_frame, text="Aztech Instrument Tracker")

    title.grid(row=0, column=0)
    logo_label = ttk.Label(logo_frame, image=photo)
    logo_label.grid(row=0,column=0)

    tool_id_label = ttk.Label(main_frame, text="Tool ID: " + new_tool.ID)
    tool_description_label = ttk.Label(main_frame, text="Tool Type: " + new_tool.tool_type)
    tool_cal_date_label = ttk.Label(main_frame, text="Date of Calibration: " + new_tool.cal_date)
    tool_cal_exp_label = ttk.Label(main_frame, text="Date of Calibration Expiration: " + new_tool.cal_exp)
    tool_use_no = ttk.Label(main_frame, text="Number of times used: " + str(new_tool.use) + "/" + str(new_tool.use_limit))

    tool_id_label.grid(row=0, column=0)
    #tool_id_label.pack()
    tool_description_label.grid(row=0, column=1)
    #tool_description_label.pack()
    tool_cal_date_label.grid(row=1, column=0)
    #tool_cal_date_label.pack()
    tool_cal_exp_label.grid(row=1, column=1)
    #tool_cal_exp_label.pack()
    tool_use_no.grid(row=2, column=0)
    #tool_use_no.pack()

    cert_button = ttk.Button(main_frame, text="Open " + new_tool.ID + " Calibration Certificate")
    cert_button.grid(row=3, column=0)
    cert_button['command'] = lambda: webbrowser.open_new(new_tool.cert_path)

    print(new_tool.cert_path)

    root.mainloop()

main()


