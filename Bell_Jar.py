import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("Amazon.csv")

avg = df["Avg Rating"].tolist()

fig = ff.create_distplot([avg],["average"],show_hist = False)
fig.show()