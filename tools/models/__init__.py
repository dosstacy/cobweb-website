import plotly.io as pio
import plotly.graph_objs as go
import numpy as np
from sympy import symbols, sympify, lambdify, solve

def generate_graph(fig):
    return pio.to_json(fig)

def draw_graph(time_steps, prices, lang):
    trace = go.Scatter(x=time_steps, y=prices, mode='lines+markers', name='Expected price')
    if lang == 'en':
        layout = go.Layout(xaxis=dict(title='Periods'), yaxis=dict(title='Price'))
    else:
        layout = go.Layout(xaxis=dict(title='Periody'), yaxis=dict(title='Cena'))
    figure = go.Figure(data=[trace], layout=layout)

    return figure

def eq_price(s_shift, d_shift, d_slope, s_slope):
    pe = (s_shift - d_shift) / (d_slope - s_slope)
    return pe

def demand(d_shift, d_slope, price):
    return d_shift + d_slope * price

def supply(s_shift, s_slope, price):
    return s_shift + s_slope * price
