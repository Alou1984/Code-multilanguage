from operator import index

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import imshow, figure

pd.set_option('future.no_silent_downcasting', True)
pd.set_option('display.max_row', 200)
pd.set_option('display.max_column', 200)
data = pd.read_excel("carac_old_proto_serie2.xlsx")
df = data.copy()
df.drop(['2 decks'], axis = 1, inplace = True)
#print(df.head())
'''
df["ligne_tir_50m"] = df["ligne_tir_50m"].replace('OK', 1)
df["ligne_tir_50m"] = df["ligne_tir_50m"].replace('KO', 0)

df["ligne_tir_150m"] = df["ligne_tir_150m"].replace('OK', 1)
df["ligne_tir_150m"] = df["ligne_tir_150m"].replace('KO', 0)

df["ligne_tir_250m"] = df["ligne_tir_250m"].replace('OK', 1)
df["ligne_tir_250m"] = df["ligne_tir_250m"].replace('KO', 0)

df["ligne_tir_500m"] = df["ligne_tir_500m"].replace('OK', 1)
df["ligne_tir_500m"] = df["ligne_tir_500m"].replace('KO', 0)

df["ligne_tir_750m"] = df["ligne_tir_750m"].replace('OK', 1)
df["ligne_tir_750m"] = df["ligne_tir_750m"].replace('KO', 0)

df["ligne_tir_1000m"] = df["ligne_tir_1000m"].replace('OK', 1)
df["ligne_tir_1000m"] = df["ligne_tir_1000m"].replace('KO', 0)
'''
#print(df.head())
#print(df.shape)


'''
# heatmap
sns.set_theme()
dfs = (
    df
    .pivot(index="Nbre de det", columns="DBD", values="ligne_tir_50m")
)

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(dfs, annot=True, fmt="d", linewidths=5, ax=ax)
'''
#line plot
'''
sns.set_theme(style="whitegrid")
values = df[['ligne_tir_50m','ligne_tir_125m','ligne_tir_250m','ligne_tir_500m','ligne_tir_750m','ligne_tir_1000m']]
det_list =  df.Nbre_de_det
conf = df.conf_DBD
sns.lineplot(data=values,  palette="tab10", linewidth=2.5, legend="full")
plt.show()
'''
#pair plot
'''
sns.set_theme(style="ticks")
sns.pairplot(df, hue="DBD")
plt.show()
'''
