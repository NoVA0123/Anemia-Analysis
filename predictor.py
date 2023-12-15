import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


# Importing the data

df = pd.read_excel('anemia.xlsx')
df.drop('Anemic level.1', axis = 1)
