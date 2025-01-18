#Martin lumpickas
import pandas as pd
from ex1 import ex1
from ex2 import ex2
from ex3 import ex3
from ex4 import ex4
from ex5 import ex5

df = pd.read_csv('data/dataset.csv', encoding='latin-1', sep=';') #importo el dataset

ex1(df)
df = ex2(df)
df = ex3(df, False)
df = ex4(df)
df = ex5(df)
