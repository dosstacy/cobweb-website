import plotly.io as pio
import plotly.graph_objs as go
import numpy as np
from sympy import symbols, sympify, lambdify, solve

def generate_graph(fig):
    return pio.to_json(fig)

def draw_graph(time_steps, prices):
    trace = go.Scatter(x=time_steps, y=prices, mode='lines+markers', name='Expected price')
    layout = go.Layout(xaxis=dict(title='Periods'), yaxis=dict(title='Price'))
    figure = go.Figure(data=[trace], layout=layout)

    return figure