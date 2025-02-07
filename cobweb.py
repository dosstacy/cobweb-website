import plotly.graph_objs as go
import plotly.io as pio
import numpy as np

d_shift = 10
d_slope = 1
s_shift = 2
s_slope = 0.8
n_iterations = 15
initial_price = 5

def demand(price):
    return d_shift - d_slope * price

def supply(price):
    return s_shift + s_slope * price


def find_cobweb():
    # Розрахунок рівноваги
    equilibrium_price = (d_shift - s_shift) / (d_slope + s_slope)
    equilibrium_quantity = demand(equilibrium_price)

    # Побудова павутини
    prices = [initial_price]
    quantities = [demand(initial_price)]

    for i in range(n_iterations):
        if i % 2 == 0:
            quantities.append(demand(prices[-1]))
        else:
            prices.append((quantities[-1] - s_shift) / s_slope)

    if len(prices) < len(quantities):
        prices.append((quantities[-1] - s_shift) / s_slope)

    # Побудова графіка
    price_range = np.linspace(0, n_iterations, 500)

    fig = go.Figure()

    # Лінії попиту та пропозиції
    fig.add_trace(go.Scatter(x=price_range, y=demand(price_range), mode='lines', name="Demand", line=dict(color="blue")))
    fig.add_trace(go.Scatter(x=price_range, y=supply(price_range), mode='lines', name="Supply", line=dict(color="red")))

    # Павутинні лінії
    for i in range(1, len(prices)):
        fig.add_trace(go.Scatter(x=[prices[i-1], prices[i-1]], y=[quantities[i-1], quantities[i]], mode='lines', line=dict(color="black", dash="dash"),showlegend=False))
        fig.add_trace(go.Scatter(x=[prices[i-1], prices[i]], y=[quantities[i], quantities[i]], mode='lines', line=dict(color="black", dash="dash"),showlegend=False))

    # Точка рівноваги
    fig.add_trace(go.Scatter(x=[equilibrium_price], y=[equilibrium_quantity], mode='markers', marker=dict(color="green", size=10), name="Equilibrium"))

    # Оформлення
    fig.update_layout(xaxis_title="Price", yaxis_title="Amount", template="plotly_white")

    return pio.to_json(fig)