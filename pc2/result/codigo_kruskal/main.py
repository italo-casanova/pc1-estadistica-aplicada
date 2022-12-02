import os, sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy.stats import wilcoxon

# setting the path to the root of the project
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import process.unpack as unpack
import process.analyze as analyzer
import process.visualize as visualize

data_sim1 = unpack.unpack("data//data_kruskal//06-01-2020.csv")

print("Wilcoxon test for the first simulation")
print("=====================================")
print(data_sim1[0])


