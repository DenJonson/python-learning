import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

width = 0.4

def graf(path):
  data = pd.read_excel(path)
  data = np.array(data)
  x_list = data[1:, 0]
  y_list2 = data[1:, 1]
  y_list3 = data[1:, 2]
  for i in range(3,9):
    y_list = data[1:, i]
    plt.title('Плотность от длины волны образца 2+ Концентрация:' + str(data[0, i]))
    plt.plot(x_list, y_list,   label = '.', marker='2')
    plt.plot(x_list, y_list2,  label = '.', marker='*')
    plt.show()
  for i in range(9, 16):
    y_list = data[1:, i]
    plt.title('Плотность от длины волны образца 3+ Концентрация:' + str(data[0, i]))
    plt.plot(x_list, y_list, label = '.', marker='2')
    plt.plot( x_list, y_list3,  label = '.', marker='H')
    plt.show()

graf("2.xlsx")
