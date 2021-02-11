import pandas as pd
import numpy as np
from numpy.random import default_rng


class MyDataFrame(pd.DataFrame):
    def null_count(self):
        return self.isna().sum().sum()

    def train_test_split(self, frac):
        df_len = self.shape[0]
        train_len = int(df_len * frac)
        train_split = self.iloc[:train_len]
        test_split = self.iloc[train_len:]
        return train_split, test_split

    def randomize(self, seed=10):
        rng = default_rng(seed)
        cols = self.shape[1]
        rows = self.shape[0]
        new_df = self.copy()
        numbers = rng.choice(rows, size=rows, replace=False)
        numbers2 = rng.choice(cols, size=cols, replace=False)
        print(numbers, numbers2)
        row = 0
        col = 0
        for i in numbers:
            for j in numbers2:
                new_df.iloc[i, j] = self.iloc[row, col]
                if col < cols - 1:
                    col += 1
                else:
                    col = 0
            if row < rows - 1:
                row += 1
            else:
                row = 0
        return new_df


if __name__ == "__main__":
    ODI_runs = {'name': ['Tendulkar', 'Sangakkara', 'Ponting',
                         'Jayasurya', 'Jayawardene', 'Kohli',
                         'Haq', 'Kallis', 'Ganguly', 'Dravid'],
                'runs': [18426, 14234, 13704, 13430, 12650,
                         11867, 11739, 11579, 11363, 10889]}
    my_df = MyDataFrame(ODI_runs)
    train_test = my_df.train_test_split(0.8)
    print(train_test)