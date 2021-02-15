import numpy as np


class Description:
    def __init__(self, df):
        self.df = df

    def summary(self):
        a = self.df.columns
        for i in range(len(self.df.columns)):
            if np.issubdtype(self.df[a[i]].dtype, np.number):
                keys = ["Count", "Min", "1st Q", "Median", "3rd Q", "Max", "Mean", "St. dev"]
                values = [self.df[a[i]].count(), self.df[a[i]].min(), np.quantile(self.df[a[i]], 0.25),
                          self.df[a[i]].median(),
                          np.quantile(self.df[a[i]], 0.75), self.df[a[i]].max(), self.df[a[i]].mean(),
                          self.df[a[i]].std()]

            elif np.issubdtype(self.df[a[i]].dtype, np.datetime64):
                keys = ["Min", "Mean", "Max"]
                values = [self.df[a[i]].min(), self.df[a[i]].min(), self.df[a[i]].max()]

            elif np.issubdtype(self.df[a[i]].dtype, np.bool_):
                keys = ["Levels", "Frequency"]
                values = [np.unique(self.df[a[i]]), np.unique(self.df[a[i]], return_counts=True)]
            elif np.issubdtype(self.df[a[i]].dtype, np.object_):
                keys = ["Count", "Unique"]
                values = [self.df[a[i]].count(), len(np.unique(self.df[a[i]]))]

            else:
                continue

            d = dict(zip(keys, values))
            print(a[i])

            for k, v in d.items():
                print(k, ": ", v)
            print('\n')
