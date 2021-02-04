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

from PIL import ImageTk, Image

# TODO: Add filepath for spreadsheet
spread_path = r'C:/Users/kuebeltm/OneDrive/Documents/Aztech_work/Copy of QA EQUIPMENT LIST 8-21-2020 (WIP)x(2)UTF.csv'
print(spread_path)
def main():

    tool_input = input('Input tool ID')

    # DONE remove below

    # TODO remove below
    #webbrowser.open_new(spread_path)

    new_tool = Tool(tool_input, spread_path)
    print('made to 33')

    try:
        new_tool.find_row()
        new_tool.set_tool_info()
        # DONE remove if necessary
        print("does das PATH work?: " + new_tool.cert_path)
        if new_tool.ID == 'nan':
            messagebox.showerror(title="Aztech Instrument Tracker - Error", message="Instrument ID not found!"
                                                                " Please try another ID and contact QA Management.")
            quit()
    except Exception:
        messagebox.showerror(title="Aztech Instrument Tracker - Error", message="Instrument ID not found!"
                                                   " Please try another ID and contact QA Management.")

    # DONE uncomment below


    print("confirming expiration is: " + new_tool.cal_exp)

    # TODO CHANGE TO TOOL OBJECT PATH VAR
    logged_instrument = Log(r'C:\Users\kuebeltm\OneDrive\Documents\Aztech_work\20266120.csv')

    new_tool.use = str(logged_instrument.usecount)

    def cert_button_click():
        print(str(new_tool.cert_path))
        os.startfile(new_tool.cert_path)
    # TODO remove below

    print("tool use count is: " + new_tool.use)


    root = tkinter.Tk()

    root.title("Aztech Instrument Tracker")

    icon_img = PhotoImage(file = 'aztech logo.PNG')
    root.iconphoto(False, icon_img)

    main_frame = ttk.Frame(root, padding = 10)
    logo_frame = ttk.Frame(root, width = 50, height = 50)
    title_frame = ttk.Frame(root, width = 300, height = 196)

    logo_frame.grid(row=0, column=0)
    title_frame.grid(row=0, column=1)
    main_frame.grid(row=1, column=0)

    logo = Image.open('AZIT_Image1.png')
    photo = ImageTk.PhotoImage(logo)

    logo_label = ttk.Label(logo_frame, image=photo)
    logo_label.grid(row=0,column=0)

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

        print(override_option)
        if override_option is True:
            new_tool.status = 'OVERRIDE'
            Temp(new_tool.status, new_tool.log_path)
        else:
            new_tool.status = 'NOT GOOD FOR USE'
            Temp(new_tool.status, new_tool.log_path)


    if new_tool.status == "GAGE READY FOR USE":
        tool_status.configure(foreground="green")

        good_button = ttk.Button(main_frame, text="USE INSTRUMENT")
        good_button.grid(row=5, column=1)
        good_button['command'] = lambda: Temp(new_tool.status, new_tool.log_path)
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

    cert_button = ttk.Button(main_frame, text="Open " + new_tool.ID + " Calibration Certificate")
    cert_button.grid(row=5, column=0)
    cert_button['command'] = lambda: cert_button_click()


    root.mainloop()


main()
