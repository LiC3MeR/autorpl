import pandas as pd
import os

#Путь к папке с доком
os.chdir(r'C:\Users\010011010\Downloads')
os.getcwd()


#Путь к доку

#Пример
#pd.read_excel('doc1.xlsx',
#                       sheet_name = 'Лист1')

dataset = pd.read_excel('',
                        sheet_name = '')
dataset



#Выбераем Лист в котором вся информация про замену

#Пример
#pd.read_excel('doc1.xlsx', 
#                       sheet_name = 'Замены')

rpl = pd.read_excel('', 
                        sheet_name = '')
rpl



# Выполняем замену
rng = len(rpl)
rng

for i in range(rng):
    dataset['Столбец который надо заменить'] = dataset['Столбец который надо заменить'].str.replace(rpl['Столбец с которого надо поменять'][i], rpl['Столбец на который надо поменять'][i], case = False)


# Сохраняем документ

dataset.to_excel('Название готового дока!')