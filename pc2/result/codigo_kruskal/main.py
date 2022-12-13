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

data_kruskall = unpack.unpack("data//data_kruskal//06-01-2020.csv")

print("Kruskal-Wallis Test")
print("=====================================")
grupo_los_olivos = analyzer.select_by_column_qualitative(data_kruskall, 2, "Los Olivos Academia")
grupo_comas = analyzer.select_by_column_qualitative(data_kruskall, 2, "Comas Academia")
grupo_santa_beatriz = analyzer.select_by_column_qualitative(data_kruskall, 2, "Santa Beatriz Academia")
grupo_villa_el_salvador = analyzer.select_by_column_qualitative(data_kruskall, 2, "Villa el Salvador Academia")

notas_los_olivos = analyzer.select_column_floats(grupo_los_olivos, 4)
notas_comas = analyzer.select_column_floats(grupo_comas, 4)
notas_santa_beatriz = analyzer.select_column_floats(grupo_santa_beatriz, 4)
notas_villa_el_salvador = analyzer.select_column_floats(grupo_villa_el_salvador, 4)


# visualize the data with plt
print("Todos:")
print(stats.kruskal(notas_comas, notas_santa_beatriz, notas_villa_el_salvador, notas_los_olivos))
print("Comas, Santa Beatriz, Los Olivos: ")
print(stats.kruskal(notas_comas, notas_santa_beatriz, notas_los_olivos)) # p = 0.0186
print("Comas, Santa Beatriz, Villa el Salvador: ")
print(stats.kruskal(notas_comas, notas_santa_beatriz, notas_villa_el_salvador))

# plot the graphs in the same figure with subplots
fig, axs = plt.subplots(2, 2)
fig.suptitle('Kruskal-Wallis Test')
axs[0, 0].hist(notas_comas,bins = 5, density = True)
axs[0, 0].set_title('Comas')
axs[0, 1].hist(notas_santa_beatriz, bins = 5, density = True)
axs[0, 1].set_title('Santa Beatriz')
axs[1, 0].hist(notas_los_olivos, bins = 5, density = True)
axs[1, 0].set_title('Los Olivos')
axs[1, 1].hist(notas_villa_el_salvador, bins = 5, density = True)
axs[1, 1].set_title('Villa el Salvador')

# plot the graphs as boxplots int he same figure with the same scale
fig, axs = plt.subplots(2, 2)
fig.suptitle('Kruskal-Wallis Test')
axs[0, 0].boxplot(notas_comas)
axs[0, 0].set_title('Comas')
axs[0, 1].boxplot(notas_santa_beatriz)
axs[0, 1].set_title('Santa Beatriz')
axs[1, 0].boxplot(notas_los_olivos)
axs[1, 0].set_title('Los Olivos')
axs[1, 1].boxplot(notas_villa_el_salvador)
axs[1, 1].set_title('Villa el Salvador')
axs[0,0].set_ylim([0, 500])
axs[0,1].set_ylim([0, 500])
axs[1,0].set_ylim([0, 500])
axs[1,1].set_ylim([0, 500])
plt.show()