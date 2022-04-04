import csv
import plotly.graph_objects as go
import pandas as pd
data1=pd.read_csv('data1.csv')
print(data1.groupby("level")["attempt"].mean())

fig=go.Figure(go.Scatter(y=data1.groupby("level")["attempt"].mean(),x=['level1','level2','level3','level4'],orientation='v'))
fig.show()