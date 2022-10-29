import os, sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# setting the path to the root of the project
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import process.unpack as unpack
import process.analyze as analyzer
import process.visualize as visualize

data_sw = unpack.unpack("data//Software_Professional_Salaries.csv")
sw_cols = list( enumerate(data_sw[0]))

def filter_group(data_list) -> tuple[list, min, sum]:
    # slice the data of floats in 1000 bins of equal size and return the frequency/density of each bin 
    # create a new list including only the data of the bins that contain a density > 0.3

    FILTER_NUMBER = 400 # number of bins to be filtered

    data_list.sort()
    data_range = data_list[-1] - data_list[0]
    print(data_list[-1], data_list[0])
    width = data_range / 1000.0
    sum = 0
    for num in data_list:
        sum += num*width
    list_res = []
    density = [0]*1000

    i_list = 0
    current_bound = 0
    min = 0
    for i in range(FILTER_NUMBER):
        
        current_list = []
        while current_bound < data_list[0]+width*(i+1):
            current_bound = data_list[i_list]
            density[i] += data_list[i_list]/sum
            current_list.append(float(data_list[i_list]))
            i_list += 1
            
        if density[i] > 4.1e-5:
            min = data_list[0]+width*(i+1)
        if density[i] > 5e-6 :
            list_res += current_list

    print("ilist", i_list)
    print("Length of list: ", len(list_res))
    return (list_res + data_list[i_list:],
            min,
            sum)


def remove_outliers(list_data):
    list_data = np.array(list_data)
    list_data = list_data[abs(list_data - np.mean(list_data)) < 3 * np.std(list_data)]

def transform_to_same_scale(list_data):
    list_data = np.array(list_data)
    print(np.min(list_data))
    list_data = list_data - np.min(list_data)
    
if __name__ == "__main__":
    
    print(sw_cols)

    # "*" is as a wildcard
    sw_data_income_bangalore = analyzer.filter_by_column_floats(data_sw, 5, "Bangalore", 3, exclude=False)
    sw_data_income_delhi = analyzer.filter_by_column_floats(data_sw, 5, "New Delhi", 3, exclude=False)
    print("Bangalore: ", len(sw_data_income_bangalore))
    print("Delhi: ", len(sw_data_income_delhi))
    # remove the outliers that are 2.5 deviations of the median with numpy
    remove_outliers(sw_data_income_bangalore)
    remove_outliers(sw_data_income_delhi)
    transform_to_same_scale(sw_data_income_bangalore)
    transform_to_same_scale(sw_data_income_delhi)

    plt.hist(sw_data_income_bangalore, bins=1000, density=True, alpha=0.5, label="Bangalore")
    plt.show()

    plt.hist(sw_data_income_delhi, bins=1000, density=True, alpha=0.5, label="Delhi")
    plt.show()
    
    # generate a frame for the plot in 2 rows and 1 column
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    
    # plot the data
    ax1.hist(sw_data_income_bangalore, bins=20, color="blue")
    ax2.hist(sw_data_income_delhi, bins=100, color="red")
    
    # set the title
    ax1.set_title("Bangalore")
    ax2.set_title("Delhi")
    plt.show()
    
    # kuskal wallis test
    print("Kuskal Wallis Test")
    print(stats.kruskal(sw_data_income_bangalore, sw_data_income_delhi))
    


