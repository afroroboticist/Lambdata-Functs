import pandas as pd
import numpy as np
from random import randint
import pytest
import lambdata as ld
from lambdata import helper_functions as hp
import sklearn.datasets


@pytest.fixture
def get_data():
	data = pd.read_csv('/home/afroroboticist/flaskProjectSpace/catalogue_final.csv')
	my_df = hp.MyDataFrame(data)
	return my_df

################################
# Test the randomizer Function #
################################


def test_randomizer(get_data):

        randomized_df = get_data.randomize()
        # Test that both dataframes have the same length #
        assert len(get_data) == len(randomized_df)
        # Test that after randomizing both no longer have the same elements #
        assert randomized_df.equals(get_data) == False
        # Test that dataframes are of type MyDataFrame and Pandas #
        assert isinstance(get_data, pd.DataFrame)
        assert isinstance(randomized_df, pd.DataFrame)


######################################
# Test the train_test_split function #
######################################

def test_split(get_data):

	X, y = get_data.train_test_split(0.8)
	assert isinstance(X, pd.DataFrame)
	assert isinstance(y, pd.DataFrame)
	assert round(len(X) / len(get_data)) == round(0.8)


################################
# Test the Null count function #
################################

def test_null(get_data):
	
	result = get_data.null_count()
	assert isinstance(result , np.int64)

