"""""
Aztech Locknut Company Instrument Tracker Program
This program is licensed to Aztech Engineering Inc. and its subsidiaries
Written by Todd Kuebelbeck, 2021 developed at and for Aztech Locknut Company
--------------------------------------------------------------------------------
Main class that contains GUI
"""""

from __future__ import absolute_import  # updated importing tools for python v3.x.x
from azqa_instrument import Tool   # import the Tool helper class
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
import tkinter
from read_log import Log
import os
from write_temp import Temp
from config_class import Config
from PIL import ImageTk, Image
from date_check import Date
import datetime

config_file = Config()
# TODO: Add filepath for spreadsheet
spread_path = config_file.masterlist
def main():

    tool_input = input('Input tool ID')

    # DONE remove below

    # TODO remove below
    #webbrowser.open_new(spread_path)

    new_tool = Tool(tool_input, spread_path)

    try:
        new_tool.find_row()
        new_tool.set_tool_info()
    except Exception:
        messagebox.showerror(title="Aztech Instrument Tracker - Error", message="Instrument ID not found!"
                                                                                " Please try another ID and contact QA Management.")
    """""
    if str(new_tool.ID) != str(tool_input):
        messagebox.showerror(title="Aztech Instrument Tracker - Error", message="Instrument ID not found!"
                                                            " Please try another ID and contact QA Management.")
        quit()
    """


    # DONE remove if necessary


    # DONE uncomment below
    new_date_check = Date(new_tool.cal_exp)
    new_date_check.chop_date()
    new_date_check.chop_today()


    # TODO CHANGE TO TOOL OBJECT PATH VAR
    logged_instrument = Log(str(new_tool.log_path))

    new_tool.use = str(logged_instrument.usecount)

    def cert_button_click():

        os.startfile(new_tool.cert_path)
    # TODO remove below


    root = tkinter.Tk()

    root.title("Aztech Instrument Tracker")

    icon_img = PhotoImage(file = 'aztech logo.PNG')
    root.iconphoto(False, icon_img)

    main_frame = ttk.Frame(root, padding = 10)
    logo_frame = ttk.Frame(root, width = 0, height = 0)
    title_frame = ttk.Frame(root, width = 0, height = 0)

    logo_frame.grid(row=0, column=0)
    title_frame.grid(row=0, column=1)
    main_frame.grid(row=1, column=0)

    logo = Image.open('AZIT_Image1.png')
    photo = ImageTk.PhotoImage(logo)

    logo_label = ttk.Label(logo_frame, image=photo)
    logo_label.grid(row=0, column=0)

    tool_id_label = ttk.Label(main_frame, text="Instrument ID: " + new_tool.ID)
    tool_description_label = ttk.Label(main_frame, text="Instrument Type: " + new_tool.tool_type)
    tool_cal_date_label = ttk.Label(main_frame, text="Date of Calibration: " + new_tool.cal_date)
    tool_cal_exp_label = ttk.Label(main_frame, text="Date of Calibration Expiration: " + new_tool.cal_exp)
    tool_use_no = ttk.Label(main_frame, text="Number of times used: " + str(new_tool.use) + "/" + str(new_tool.use_limit))
    tool_location = ttk.Label(main_frame, text='Location: ' + str(new_tool.location))
    tool_status = ttk.Label(main_frame, text='Instrument Status: ' + str(new_tool.status))
    tool_status.config(font=(44))

    def override_routine():
        override_option = messagebox.askyesno("EXPIRED INSTRUMENT", "The instrument scanned is expired or exceeded its use count!"
                                " Notify QA Management about gage. Would you like to override?")


        if override_option is True:
            new_tool.status = 'OVERRIDE'
            Temp(new_tool.status, new_tool.log_path,new_tool.ID, config_file.temp_location)
        else:
            new_tool.status = 'NOT GOOD FOR USE'
            Temp(new_tool.status, new_tool.log_path, new_tool.ID, config_file.temp_location)

    if new_tool.exp_type == 'COUNT' and int(new_tool.use) < new_tool.use_limit:
        new_tool.status = 'GOOD FOR USE'
        tool_status = ttk.Label(main_frame, text='Instrument Status: ' + str(new_tool.status))
        tool_status.config(font=(44))
        tool_status.configure(foreground="green")

        good_button = ttk.Button(main_frame, text="USE INSTRUMENT")
        good_button.grid(row=5, column=1)
        good_button['command'] = lambda: Temp(new_tool.status, new_tool.log_path,new_tool.ID, config_file.temp_location)

    elif new_tool.exp_type == 'DATE' and (str(new_date_check.check()) == 'False'):
        new_tool.status = 'GOOD FOR USE'
        tool_status = ttk.Label(main_frame, text='Instrument Status: ' + str(new_tool.status))
        tool_status.config(font=(44))
        tool_status.configure(foreground="green")

        good_button = ttk.Button(main_frame, text="USE INSTRUMENT")
        good_button.grid(row=5, column=1)
        good_button['command'] = lambda: Temp(new_tool.status, new_tool.log_path, new_tool.ID, config_file.temp_location)

    else:
        override_routine()
        tool_status = ttk.Label(main_frame, text='Instrument Status: ' + str(new_tool.status))
        tool_status.configure(foreground="red")
        tool_status.config(font=(44))


    tool_status.grid(row=1, column=0)
    tool_id_label.grid(row=2, column=0)
    #tool_id_label.pack()
    tool_description_label.grid(row=2, column=1)
    #tool_description_label.pack()
    tool_cal_date_label.grid(row=3, column=0)
    #tool_cal_date_label.pack()
    tool_cal_exp_label.grid(row=3, column=1)
    #tool_cal_exp_label.pack()
    tool_use_no.grid(row=4, column=0)
    #tool_use_no.pack()
    tool_location.grid(row=4, column=1)

    # TODO REMOVE BELOW

    cert_button = ttk.Button(main_frame, text="Open " + new_tool.ID + " Calibration Certificate")
    cert_button.grid(row=5, column=0)
    cert_button['command'] = lambda: cert_button_click()

    root.mainloop()


main()
