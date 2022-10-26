import os, sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# setting the path to the root of the project
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import process.unpack as unpack
import process.analyze as analyzer
import process.visualize as visualize

data_sw = unpack.unpack("data/Software_Professional_Salaries.csv")
data_ds = unpack.unpack("data/data_science")
sw_cols = list( enumerate(data_sw[0]))
ds_cols = list( enumerate(data_ds[0]))

if __name__ == "__main__":
    print(sw_cols)
    print(ds_cols)

    # "*" is as a wildcard
    data_ingresos = analyzer.filter_by_column_floats(data, 0, "*", 18)

    plt.hist(sw_data_income, density=True)
    plt.hist(ds_data_income, density=True)
    plt.show()

    # remove the outliers that are 2.5 deviations of the median with numpy
    sw_data_income = np.array(data_ingresos)
    ds_data_income = data_ingresos[abs(data_ingresos - np.median(data_ingresos)) < 2.5 * np.std(data_ingresos)]

    # show in a histogram as probability density
    plt.hist(sw_data_income, density=True)
    plt.hist(ds_data_income, density=True)
    plt.show()

    # show boxplot

    plt.title("Distribucion de ingresos segun especialidad")
    plt.boxplot(sw_data_income)
    plt.boxplot(ds_data_income)

    # render the histograms
    plt.show()


