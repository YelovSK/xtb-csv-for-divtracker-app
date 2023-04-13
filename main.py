import pandas as pd
import os

path_to_csv = input("Path to your csv file (without .csv): ")
path_to_output_csv = input("Path for your output csv file (without .csv): ")

path = f"{path_to_csv}.csv"

if os.path.exists(path):
    data_from_xtb = pd.read_csv("../Movies/xtb.csv", usecols=["Symbol", "Comment", "Time"], sep=";")
    data_to_app = data_from_xtb.copy()

    new_columns = ["Ticker", "Quantity", "Cost Per Share", "Date"]
    data_to_app = data_to_app.reindex(columns=new_columns)

    data_to_app["Ticker"] = data_from_xtb["Symbol"].str.split(".").str[0]
    data_to_app["Quantity"] = data_from_xtb["Comment"].str.split(" ").str[2]
    data_to_app["Cost Per Share"] = data_from_xtb["Comment"].str.split(" ").str[4]
    data_to_app["Date"] = pd.to_datetime(data_from_xtb["Time"].str.split(" ").str[0], dayfirst=True)

    data_to_app.to_csv(f"{path_to_output_csv}.csv", index=False)
else:
    print("File does not exist")
