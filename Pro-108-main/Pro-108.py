import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import csv
df=pd.read_csv("e:/Python/Pro-108/data.csv")

fig = ff.create_distplot([df["Days Present"].tolist()],["Days Present"],show_hist=False)
fig.show()