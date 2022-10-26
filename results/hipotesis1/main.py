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
    data_ingresos = np.array(data_ingresos)
    data_ingresos = data_ingresos[abs(data_ingresos - np.mean(data_ingresos)) < 2.5 * np.std(data_ingresos)]
    
    
    # standardize the data before the tests
    data_ingresos = (data_ingresos - np.mean(data_ingresos)) /np.std(data_ingresos) 
    plt.hist(data_ingresos, density=True)
    # plot a normal distribution with the same mean and standard deviation
    plt.plot(np.linspace(-3, 3, 100), stats.norm.pdf(np.linspace(-3, 3, 100), 0, 1))
    # plot a t distribution with the same mean and standard deviation and 2 degrees of freedom
    plt.plot(np.linspace(-3, 3, 100), stats.t.pdf(np.linspace(-3, 3, 100), 2, 0, 1))
    # run normality tests in scipy
    print(stats.jarque_bera(data_ingresos))
    print(stats.kstest(data_ingresos, stats.norm.cdf))


    # render the histograms
    plt.show()  

    # plot a qq plot
    stats.probplot(data_ingresos, dist="norm", plot=plt)
    plt.show()  

    