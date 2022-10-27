import os, sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# setting the path to the root of the project
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import process.unpack as unpack
import process.analyze as analyzer
import process.visualize as visualize

data_of_sw = unpack.unpack("data\Software_Professional_Salaries.csv")
columnas_sw = list( enumerate(data_of_sw[0]))

if __name__ == "__main__":
    print("Desarrollo de la segunda hipótesis")
    print(columnas_sw)

    # "*" is as a wildcard
    sw_ingresos = analyzer.filter_by_column_floats(data_of_sw, 1, "Fresher", 3, exclude= True)
    print(len(sw_ingresos))

    # remove the outliers that are 2.5 deviations of the median with numpy

    sw_ingresos = np.array(sw_ingresos)
    sw_ingresos = sw_ingresos[abs(sw_ingresos - np.median(sw_ingresos)) < 3 * np.std(sw_ingresos)]

    # sw_ingresos = (sw_ingresos - np.mean(sw_ingresos)) /1
    # print("Media: ", np.mean(sw_ingresos))
    # print("Mediana: ", np.median(sw_ingresos))
    # plt.hist(sw_ingresos, density=True, bins = 100 )

    for i in analyzer.find_classes_in_column_qualitative(data_of_sw, 1):
        
        sw_filtered = analyzer.filter_by_column_floats(data_of_sw, 1, i, 3)
        
        if len(sw_filtered) < 100:
            continue

        sw_filtered = np.array(sw_filtered)
        sw_filtered = sw_filtered[abs(sw_filtered - np.median(sw_filtered)) < 3 * np.std(sw_filtered)]

        if(np.median(sw_filtered) > 500000):
            continue

        plt.hist(sw_filtered, label=i, bins = 100)
        plt.legend()
        print(i, "Media: ", np.mean(sw_filtered))
        print("tamaño: ", len(sw_filtered))
        plt.show()

    plt.show()

    #plot a pareto distribution with the same mean and standard deviation of the data
    
    # assuming the data follows a pareto distribution, calculate the parameters of the distribution
    print(stats.pareto.fit(sw_ingresos))
    xm_pareto = stats.pareto.fit(sw_ingresos)[0]
    alpha_pareto = stats.pareto.fit(sw_ingresos)[1]

    # run normality tests in scipy  


    # generate data from a normal distribution
    print(stats.kstest(np.random.normal(0, 1, 100), stats.norm.cdf))

    # render the histograms
    plt.show()

    # plot a qq plot
    plt.show()

