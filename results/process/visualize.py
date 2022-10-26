import matplotlib.pyplot as plt
import numpy as np
from .analyze import *

def visualize_by_column_qualitative(data: list, filter_column: int,  class_name: str, column: int) -> tuple[list,list]:
    """visualize the frequency of the data in a column"""
    (classes, counts) = filter_by_column_qualitative (data, filter_column,  class_name, column)
    plt.bar(classes, counts)
    return (classes, counts)

def visualize_by_column_floats(data: list, filter_column: int,  class_name: str, column: int) -> list:
    """visualize the frequency of the data in a column of real numbers
    Outputs the list of numbers in the column filtered by the class name"""
    numbers = filter_by_column_floats (data , filter_column,  class_name, column)
    plt.hist(numbers)
    return numbers