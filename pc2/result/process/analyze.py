from csv import list_dialects
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

def find_classes_in_column_qualitative(list_of_lists: list,
                                       column: int) -> list:
    """find the classes in a column"""
    classes = []
    # delete the first row
    for row in list_of_lists[1:]:
        if row[column] not in classes:
            class_name = row[column]
            classes.append(class_name)
    # print(classes)
    return classes


def filter_by_column_qualitative(data: list, filter_column: int,  class_name: str, column: int) -> tuple[list,list]:
    """visualize the frequency of the data in a column. Returns a tuple containing class_names and its
    frequencies"""

    classes = find_classes_in_column_qualitative(data, column)
    counts = []
    for c in classes:
        count = 0
        for row in data:
            if c == row[column] and (class_name == "*" or class_name in row[filter_column]):
                count += 1
        counts.append(count)

    # truncating the string to 10 characters
    classes = [c[:10] for c in classes]
    return (classes, counts)

def filter_by_column_floats(data: list, filter_column: int,  class_name: str, column: int, **kwargs) -> list:
    """visualize the frequency of the data in a column of real numbers
    Outputs the list of numbers in the column filtered by the class name"""

    if "exclude" in kwargs:
        exclude = kwargs["exclude"]
        if exclude == True:
            return [float(row[column]) for row in data[1:] if class_name not in  row[filter_column]]

    # numbers = []
    # for row in data[1:]:
    #     if class_name == "*" or class_name in row[filter_column]:
    #         numbers.append(float(row[column]))
    return [float(row[column]) for row in data[1:]
    if class_name in  row[filter_column] or class_name == "*"]

def select_by_column_qualitative(data: list, filter_column: int,  filter: str) -> list:
    """select the data in a column. Returns a list containing the data that matches the filter"""
    selected = []
    for row in data:
        filter_name = row[filter_column]
        if filter_name == filter:
            selected.append(row)

    return selected

def select_column_floats(data: list, column: int) -> list:
    """select the data of floats in a column. """
    selected = []
    for row in data:
        selected.append(float(row[column]))

    return selected