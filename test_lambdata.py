import pandas as pd
import numpy as np
from random import randint
import pytest
import lambdata as ld
from lambdata import helper_functions as hp
import sklearn.datasets


data = pd.read_csv('/home/afroroboticist/flaskProjectSpace/catalogue_final.csv')

# @pytest.fixture
# def get_data():
# 	data = pd.read_csv('/home/afroroboticist/flaskProjectSpace/catalogue_final.csv')
# 	return data

################################
# Test the randomizer Function #
################################

def test_randomizer():

        my_df = hp.MyDataFrame(data)
        print(my_df)
        randomized_df = my_df.randomize()
        # Test that both dataframes have the same length #
        assert len(my_df) == len(randomized_df)
        # Test that after randomizing both no longer have the same elements #
        assert randomized_df.equals(my_df) == False
        # Test that dataframes are of type MyDataFrame and Pandas #
        assert isinstance(my_df, pd.DataFrame)
        assert isinstance(randomized_df, pd.DataFrame)


######################################
# Test the train_test_split function #
######################################

def test_split():

	my_df = hp.MyDataFrame(data)
	X, y = my_df.train_test_split(0.8)
	assert isinstance(X, pd.DataFrame)
	assert isinstance(y, pd.DataFrame)
	assert round(len(X) / len(my_df)) == round(0.8)


################################
# Test the Null count function #
################################

def test_null():

	my_df = hp.MyDataFrame(data)
	#my_df = hp.MyDataFrame(data)
	result = my_df.null_count()
	assert isinstance(result , np.int64)

