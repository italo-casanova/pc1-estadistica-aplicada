import os, sys
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import process.unpack as unpack
import process.analyze as analyzer 
import process.visualize as visualize

lista_listas = unpack.unpack("data\data_science.csv")
lista_columnas = list( enumerate(lista_listas[0]))

if __name__ == "__main__":
    print("Desarrollo de la primera hipótesis")
    print(lista_columnas)
    print(visualize.visualize_by_column_floats(lista_listas, 0, "*", 18))
    plt.show()
    