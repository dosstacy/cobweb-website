import plotly.io as pio
import plotly.graph_objs as go
import numpy as np
from sympy import symbols, sympify, lambdify, solve

def generate_graph(fig):
    return pio.to_json(fig)