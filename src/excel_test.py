import pandas
import csv


def main():
    spreadsheet_path = r'C:\Users\kuebeltm\OneDrive\Documents\Aztech_work\Copy of QA EQUIPMENT LIST 8-21-2020 (WIP)x(2).csv'

    df = pandas.read_csv(spreadsheet_path, encoding='unicode_escape')

    column = df['NEW ID NUMBER']

    id_input = input("Enter ID")

    for i in range(len(column)):
        if str(df.iloc[i,2]) == str(id_input):
            print("ID " + id_input + " found and expires on: " + str(df.iloc[i,12]))
            break

main()


