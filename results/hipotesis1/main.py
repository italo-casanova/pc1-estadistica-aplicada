import os, sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# setting the path to the root of the project
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import process.unpack as unpack
import process.analyze as analyzer
import process.visualize as visualize

data_of_ds = unpack.unpack("data\data_science.csv")
data_of_sw = unpack.unpack("data\Software_Professional_Salaries.csv")
columnas_ds = list( enumerate(data_of_ds[0]))
columnas_sw = list( enumerate(data_of_sw[0]))

if __name__ == "__main__":
    print("Desarrollo de la primera hipótesis")
    print(columnas_sw)

    # "*" is as a wildcard
    ds_ingresos = analyzer.filter_by_column_floats(data_of_ds, 0, "*", 18)
    sw_ingresos = analyzer.filter_by_column_floats(data_of_sw, 0, "*", 3)

    # remove the outliers that are 2.5 deviations of the median with numpy
    ds_ingresos = np.array(ds_ingresos)
    ds_ingresos = ds_ingresos[abs(ds_ingresos - np.mean(ds_ingresos)) < 2.5 * np.std(ds_ingresos)]

    sw_ingresos = np.array(sw_ingresos)
    sw_ingresos = sw_ingresos[abs(sw_ingresos - np.mean(sw_ingresos)) < 2.5 * np.std(sw_ingresos)]

    # standardize the data before the tests
    ds_ingresos = (ds_ingresos - np.mean(ds_ingresos)) /np.std(ds_ingresos)
    # plt.hist(ds_ingresos, density=True)
    sw_ingresos = (sw_ingresos - np.mean(sw_ingresos)) /1
    plt.hist(sw_ingresos, density=True)

    #plot a pareto distribution with the same mean and standard deviation
    x = np.linspace(np.min(sw_ingresos), np.max(sw_ingresos), 100)
    
    # # plot a normal distribution with the same mean and standard deviation
    # plt.plot(np.linspace(-3, 3, 100), stats.norm.pdf(np.linspace(-3, 3, 100), 0, 1))
    
    # # plot a t distribution with the same mean and standard deviation and 2 degrees of freedom
    # plt.plot(np.linspace(-3, 3, 100), stats.t.pdf(np.linspace(-3, 3, 100), 2, 0, 1))

    # run normality tests in scipy  
    print(stats.jarque_bera(ds_ingresos))
    print(stats.kstest(ds_ingresos, stats.norm.cdf))

    # generate data from a normal distribution
    print(stats.kstest(np.random.normal(0, 1, 100), stats.norm.cdf))

    # render the histograms
    plt.show()

    # plot a qq plot
    stats.probplot(ds_ingresos, dist="norm", plot=plt)
    plt.show()

