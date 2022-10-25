# read PC1.csv
# unpack the data into a list of lists
# print the data

import csv
def unpack(path_name: str) -> list:
    """unpack the data into a list of lists"""
    with open(path_name, newline='') as csvfile:

        reader = csv.reader(csvfile, delimiter=',')
        data = [row for row in reader]
    csvfile.close()
    return data



with open("../../data/Software_Professional_Salaries.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = [row for row in reader]

    print(data)
