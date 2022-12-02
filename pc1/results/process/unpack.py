# read PC1.csv
# unpack the data into a list of lists
# print the data

import csv
def unpack(path_name: str) -> list:
    """unpack the data into a list of lists"""
    with open(path_name, newline='', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = []
        for row in reader:
            data.append(row)
    # close the file
    csvfile.close()
    return data

