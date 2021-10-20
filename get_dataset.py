import numpy as np
import pandas as pd

cols = ['Title','Instructions','Image_Name','Cleaned_Ingredients','dataset','id']
file = "archive/dataset_1.csv"
df = pd.read_csv(file, index_col=False)


df.head(10)
df.columns

df['dataset'] = 'https://www.kaggle.com/pes12017000148/food-ingredients-and-recipe-dataset-with-images'


df['id'] = 1

df[cols].to_csv('archive/cleaned_dataset_1.csv', index=False)
