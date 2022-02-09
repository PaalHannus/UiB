
import pandas as pd 
import numpy as np

#https://www.kaggle.com/budnyak/wine-rating-and-price

df = pd.read_csv('Red.csv')

data = df[['Price', 'Rating']]

data.to_csv(r'C:\Users\paal_\OneDrive\Desktop\SkolearbeidV21\INF250\CA03\data.txt', header=None, index=None, sep=' ', mode='a')

data100 = data[:100]

data100.to_csv(r'C:\Users\paal_\OneDrive\Desktop\SkolearbeidV21\INF250\CA03\data100.txt', header=None, index=None, sep=' ', mode='a')

dataCheap = data.loc[data['Price'] < 150]

dataCheap.to_csv(r'C:\Users\paal_\OneDrive\Desktop\SkolearbeidV21\INF250\CA03\dataCheap.txt', header=None, index=None, sep=' ', mode='a')