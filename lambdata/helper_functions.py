import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split

def null_count(df):
	return df.isna().value_counts()


def train_test_split(df, frac):
	df_len = len(df)
	train_len = int(df_len * frac)
	test_len = df_len - train_len
	train_split = df.iloc[:train_len]
	test_split = df.iloc[train_len:]
	return (train_split, test_split)
