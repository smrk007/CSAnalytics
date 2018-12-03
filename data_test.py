# Checks to see the top several words
import pandas as pd
dataset = pd.read_csv("data/ArXiv_MachineLearning_2018-12-03.csv")
print(dataset.nlargest(100,'frequency'))
