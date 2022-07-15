import time
import csv
import os

data = ['ID', 'Type', 'Keywords (ILJ)', 'Title', 'Url']


def str_time(): #название файла м-д-ч-м-с
    named_tuple = time.localtime() # получить struct_time
    time_string = time.strftime("%m-%d-%H-%M-%S", named_tuple)
    return time_string

def csv_writer():
    global data
    if not os.path.isdir("result"):
        os.mkdir("result")
    with open(f"result\\{str(str_time())}.csv", 'w', newline='', encoding="utf_8") as csvfile:
        writer = csv.writer(csvfile, quotechar='"', delimiter = ";", dialect='unix')
        for row in data:
            writer.writerow(row)

csv_writer()
print(str_time())