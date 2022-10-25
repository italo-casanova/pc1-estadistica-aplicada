import matplotlib.pyplot as plt
import numpy as np

def find_classes(list_of_lists: list) -> list:
    """find the classes in the data"""
    classes = []
    for row in list_of_lists:
        if row[0] not in classes:
            print(row[0])
            classes.append(row[0])
    return classes

def find_classes_in_column_qualitative(list_of_lists: list, column: int) -> list:
    """find the classes in a column"""
    classes = []
    # delete the first row
    for row in list_of_lists[1:]:
        if row[column] not in classes:
            class_name = row[column]
            classes.append(class_name)
    # print(classes)
    return classes


def visualize_by_column_qualitative(data: list, column: int) -> None:
    """visualize the frequency of the data in a column"""
    classes = find_classes_in_column_qualitative(data, column)
    counts = []
    for c in classes:
        count = 0
        for row in data:
            if c == row[column]:
                count += 1
        counts.append(count)
    classes = [c[:10] for c in classes]
    plt.bar(classes, counts)
    # plt.show()

def visualize_by_column_floats(data: list, class_name: str, column: int) -> list:
    """visualize the frequency of the data in a column of real numbers
    Outputs the list of numbers in the column filtered by the class name"""
    numbers = []
    for row in data[1:]:
        if class_name == row[0]:
            numbers.append(float(row[column]))
    plt.hist(numbers)
    return numbers
