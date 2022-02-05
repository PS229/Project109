import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("project.csv")
marklist = df["math"].to_list()

mean = sum(marklist)/len(marklist)
median = statistics.median(marklist)
mode = statistics.mode(marklist)
std = statistics.stdev(marklist)

firstst,firstend = mean - std, mean + std
secondst,secondend = mean - (2*std), mean + (2*std)
thirdst,thirdend = mean - (3*std), mean + (3*std)

firstlist = [result for result in marklist if result>firstst and result<firstend]
secondlist = [result for result in marklist if result>secondst and result<secondend]
thirdlist = [result for result in marklist if result>thirdst and result<thirdend]

print("{}% of data lies within first std".format(len(firstlist)*100/len(marklist)))
print("{}% of data lies within second std".format(len(secondlist)*100/len(marklist)))
print("{}% of data lies within third std".format(len(thirdlist)*100/len(marklist)))

fig = ff.create_distplot([marklist],["result"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [firstst,firstst], y = [0,0.17], mode = "lines", name = "stdev1"))
fig.add_trace(go.Scatter(x = [firstend,firstend], y = [0,0.17], mode = "lines", name = "stdev1"))
fig.add_trace(go.Scatter(x = [secondst,secondst], y = [0,0.17], mode = "lines", name = "stdev2"))                     
fig.add_trace(go.Scatter(x = [secondend,secondend], y = [0,0.17], mode = "lines", name = "stdev2"))
fig.show()