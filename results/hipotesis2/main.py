from calendar import c
import os, sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# setting the path to the root of the project
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import process.unpack as unpack
import process.analyze as analyzer
import process.visualize as visualize

data_of_sw = unpack.unpack("data//Software_Professional_Salaries.csv")
columnas_sw = list( enumerate(data_of_sw[0]))


def filter_group(data_list):
    # slice the data of floats in 1000 bins of equal size and return the frequency/density of each bin 
    # create a new list including only the data of the bins that contain a density > 0.3

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
    for i in range(1000):
        current_list = []
        print("aqui")
        while current_bound < data_list[0]+width*(i+1):
            current_bound = data_list[i_list]
            density[i] += data_list[i_list]/sum
            current_list.append(float(data_list[i_list]))
            i_list += 1
        # print(density[i], current_list)
        if density[i] > 5e-6 and i < 200:
            list_res += (current_list)
        if i >= 200:
            print("confirmacion")
            print(list_res)
            return list_res + data_list[i_list:]

    return list_res




if __name__ == "__main__":
    print("Desarrollo de la segunda hipótesis")
    print(columnas_sw)

    # "*" is as a wildcard
    sw_ingresos = analyzer.filter_by_column_floats(data_of_sw, 1, "*", 3)
    print(len(sw_ingresos))

    sw_ingresos = np.array(sw_ingresos)
    sw_ingresos = sw_ingresos[abs(sw_ingresos - np.median(sw_ingresos)) < 3 * np.std(sw_ingresos)]
    
    plt.hist(filter_group(list(sw_ingresos)), bins = 1000, density = True)
    plt.show()

    # remove the outliers that are 2.5 deviations of the median with numpy


    # sw_ingresos = (sw_ingresos - np.mean(sw_ingresos)) /1
    # print("Media: ", np.mean(sw_ingresos))
    # print("Mediana: ", np.median(sw_ingresos))
    # plt.hist(sw_ingresos, density=True, bins = 100 )

    # for i in analyzer.find_classes_in_column_qualitative(data_of_sw, 1):
        
    #     sw_filtered = analyzer.filter_by_column_floats(data_of_sw, 1, i, 3)
        
    #     if len(sw_filtered) < 100:
    #         continue

    #     sw_filtered = np.array(sw_filtered)
    #     sw_filtered = sw_filtered[abs(sw_filtered - np.median(sw_filtered)) < 3 * np.std(sw_filtered)]

    #     if(np.median(sw_filtered) > 500000):
    #         continue

    #     plt.hist(sw_filtered, label=i, bins = 100)
    #     plt.legend()
    #     print(i, "Media: ", np.mean(sw_filtered))
    #     print("tamaño: ", len(sw_filtered))
    #     plt.show()

    # do something

    plt.show()

    #plot a pareto distribution with the same mean and standard deviation of the data

    # assuming the data follows a pareto distribution, calculate the parameters of the distribution
    print(stats.pareto.fit(sw_ingresos))
    xm_pareto = stats.pareto.fit(sw_ingresos)[0]
    alpha_pareto = stats.pareto.fit(sw_ingresos)[1]


    # render the histograms
    plt.show()

    # plot a qq plot
    plt.show()

