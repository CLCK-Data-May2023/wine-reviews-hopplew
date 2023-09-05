import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np
wine_data = pd.read_csv("data/winemag-data-130k-v2.csv.zip", index_col=0)

country_count = wine_data.country.value_counts()
avg_points = wine_data.groupby(['country']).points.mean().round(1)

wine_matrix = pd.concat([country_count, avg_points], axis=1).rename(columns={'country' : 'count'})

wine_matrix

wine_matrix.to_csv(r'data\reviews-per-country.csv')

