import csv
import numpy as np
import pandas as pd

# import nyc_taxi.csv as a list of lists
f = open("CSVandPandas\\taxi_zone_lookup.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_col = taxi_list[:-1]
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(item)
    converted_taxi_list.append(converted_row)

# Превращаем лист из питона в массив из numpy
taxi = np.array(converted_taxi_list)
# Так как вся таблица не может в ширину уместиться в терминале,
# Записываем параметры получившегося массива в отдельную переменную, используя метод ndarray.shape
taxi_shape = taxi.shape

# для выбора строки 12 в ndarray используется
taxi[12]

#Для выбора строк 5 - 87 используется
taxi[5:88]

#Для выбора столбцов используется
taxi[:, 1:3]

#Для выбора элемента
taxi[3, 3]

#Для выбора нескольких строк или столбцов можно использовать массив значений
taxi[[4, 55, 80], 3]

# Создание файла из таблицы с помощью PANDAS
df = pd.DataFrame(taxi, columns=taxi_col)
df.to_csv(r'CSVandPandas/cartridge_accounting.csv')