import pandas as pd 
import numpy as np 
from numpy.random import default_rng

def null_count(df):
	return df.isna().sum()


def train_test_split(df, frac):
	df_len = len(df)
	train_len = int(df_len * frac)
	train_split = df.iloc[:train_len]
	test_split = df.iloc[train_len:]
	return (train_split, test_split)




def randomize(df, seed=10):
  rng = default_rng(seed)
  cols = df.shape[1]
  rows = df.shape[0]
  new_df = df.copy()
  #print(cols, rows)
  numbers = rng.choice(rows, size=rows, replace=False)
  numbers2 = rng.choice(cols, size=cols, replace=False)
  print(numbers, numbers2)
  row = 0
  col = 0
  for i in numbers:
    for j in numbers2:
      #print(i,j)
      #print(new_df.iloc[i,j], df.iloc[row, col])
      new_df.iloc[i,j] = df.iloc[row, col]
      if col < cols - 1:
        col += 1
      else:
        col = 0
    if row < rows - 1:
      row += 1
    else:
      row = 0
  return new_df