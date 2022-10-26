import os, sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# setting the path to the root of the project
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import process.unpack as unpack
import process.analyze as analyzer 
import process.visualize as visualize

data = unpack.unpack("data\data_science.csv")
columnas = list( enumerate(data[0]))

if __name__ == "__main__":
    print("Desarrollo de la primera hipótesis")
    print(columnas)

    # "*" is as a wildcard
    data_ingresos = analyzer.filter_by_column_floats(data, 0, "*", 18)

    # remove the outliers that are 2.5 deviations of the median with numpy
    # data_ingresos = np.array(data_ingresos)
    # data_ingresos = data_ingresos[abs(data_ingresos - np.median(data_ingresos)) < 2.5 * np.std(data_ingresos)]
    
    # show in a histogram as probability density
    plt.hist(data_ingresos, density=True)
    
    # display a normal distributions with the same mean and standard deviation of the data
    plt.plot(np.linspace(np.min(data_ingresos), np.max(data_ingresos), 100), stats.norm.pdf(np.linspace(np.min(data_ingresos), np.max(data_ingresos), 100), np.mean(data_ingresos), np.std(data_ingresos)))
    
    # jarque-bera test
    print("cantidad de datos:", len(data_ingresos))

    # print(stats.jarque_bera(data_ingresos))
    # run normality tests in scipy
    print(stats.normaltest(data_ingresos*2))
    print(stats.shapiro(data_ingresos))
    # print(stats.anderson(data_ingresos))
    print(stats.kstest(np.random.normal(0, 1, 00), stats.norm.cdf))

    # generate array with values of a normal distribution with mean 1 and starndard deviation 1
    print(np.random.normal(1, 1, 100))

    # render the histograms
    # plt.show()  
    