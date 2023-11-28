import pandas as pd

from sklearn.datasets import load_iris

iris = load_iris()

iris

iris.columns

Iris_set = pd.read_csv("iris.csv", index_col="number")

Iris_set.columns

Iris_set.head()

Iris_set.tail(1)

Iris_set.describe()
