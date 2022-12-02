from calendar import c
from math import dist
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



x_m = 1
alpha = 0.7
size = 10
divisions = size * 100
gamma = stats.gamma(1, 1, 1/alpha)
rv = stats.pareto(alpha, 0, x_m)

if __name__ == "__main__":
    print("Desarrollo de la segunda hipótesis")
    print(columnas_sw)

    # "*" is as a wildcard
    sw_ingresos = analyzer.filter_by_column_floats(data_of_sw, 1, "*", 3)
    print(len(sw_ingresos))


    sw_ingresos = np.array(sw_ingresos)
    sw_ingresos = sw_ingresos[abs(sw_ingresos - np.median(sw_ingresos)) < 3 * np.std(sw_ingresos)]
    
    plt.hist(sw_ingresos, density=True, bins=100, label="Software Professional Salaries")
    plt.show()
    sw_ingresos, min, sum_group = filter_group(list(sw_ingresos))

    plt.hist(sw_ingresos, density=True, bins=100, label="Software Professional Salaries")
    plt.show()


    sw_ingresos = np.array(sw_ingresos)
    sw_ingresos = sw_ingresos - min -200000 - 100000 
    sw_ingresos = 2.5*sw_ingresos / 1e6 + 1

    plt.hist(sw_ingresos, bins=15, density=True)
    count, bins = np.histogram(sw_ingresos, bins=1000, density=True)
    pdf = count / sum(count)
    plt.plot(np.linspace(0, size, divisions), gamma.pdf(np.linspace(0, size, divisions)))
    plt.show()

    cumulative = np.cumsum(pdf)
    plt.plot(bins[:-1], cumulative, c='blue')

    # plt.show()
    # draw bins and pdf as x,y points
    # plt.plot(np.linspace(0, size, divisions), stats.pareto.pdf(np.linspace(0, size, divisions),alpha, 0, x_m))
    plt.plot(np.linspace(0, size, divisions), gamma.cdf(np.linspace(0, size, divisions)))
    # plt.plot(np.linspace(0, size, divisions), rv.cdf(np.linspace(0, size, divisions)), color = "red")

    # render the histograms
    plt.show()

    # draw a qq plot
    stats.probplot(sw_ingresos, dist=gamma, plot=plt)

    # kolmogorov-smirnov test
    print(stats.kstest(sw_ingresos, cdf=gamma.cdf))

    # calculate the p-value of a kolmogorov-smirnov test given the statistic
    print(stats.kstwobign.sf(0.1))

    # plot a qq plot
    plt.show()

