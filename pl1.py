import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
x = [1,2,3,4,5,6,7,8,9,10]
y = [7,8,2,4,5,3,9,8,6,5]
fig = px.line(x=x,y=y,title="Line graph")
fig.show()

# another way to draw graph
import plotly.graph_objects as go
fig = go.Figure(go.Scatter(x=x,y=y))
fig.update_layout(title="Line Graph",xaxis_title="This is x axis",yaxis_title="this is y axis")
fig.show()

# drawing multiple library 
x1 , y1 =[1,2,3,4,5] ,[5,6,7,8,9]
x2 , y2 = [1,2,3,4,5],[7,4,9,6,3]
x3 , y3 =[ 3,7,8,2,7],[9,3,4,6,7]
fig = go.Figure()
fig.add_trace(go.Scatter(x=x1,y=y1))
fig.add_trace(go.Scatter(x=x2,y=y2))
fig.add_trace(go.Scatter(x=x3,y=y3))
fig.show()

# changing 
fig = go.Figure()
fig.add_trace(go.Scatter(x=x1,y=y1,name="line1",mode="lines"))
fig.add_trace(go.Scatter(x=x2,y=y2,name="line2",mode="markers"))
fig.add_trace(go.Scatter(x=x3,y=y3,name="line3",mode="lines+markers"))
fig.show()

# BUbble Chart
import plotly.graph_objects as go
x = [12,3,4,5]
y=[4,6,8,10]
fig = go.Figure(go.Scatter(x=x,y=y,mode="markers",marker_size=[40,50,70,90],text=["product A","product C","product B","product D"])) # bubble size and name
fig.show()
