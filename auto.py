import pandas as pd
import os

os.chdir(r'C:\Users\010011010\Downloads')
os.getcwd()
dataset = pd.read_excel('',
                        sheet_name = '')
dataset

rpl = pd.read_excel('', 
                        sheet_name = '')
rpl

rng = len(replace)
rng

for i in range(rng):
    dataset['Столбец который надо заменить'] = dataset['Столбец который надо заменить'].str.replace(rpl['Столбец с которого надо поменять'][i], rpl['Столбец на который надо поменять'][i], case = False)



dataset.to_excel('Название готового дока!')