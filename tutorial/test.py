import time
import os
import pandas 

while True:
    if os.path.exists("files/original.csv"):
        data = pandas.read_csv("files/original.csv")
        print(data.mean())
    else:
        print("File does not exist.")
    time.sleep(10)