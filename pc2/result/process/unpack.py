import csv
def unpack(path_name: str) -> list:
    """unpack the data into a list of lists"""
    with open(path_name, newline='', encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = []
        for row in reader:
            data.append(row)
    # close the file
    csvfile.close()
    return data

