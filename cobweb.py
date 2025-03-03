import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go


class EqCobweb:
    def __init__(self, d_shift, d_slope, s_shift, s_slope, n_iterations, initial_price):
        self.d_shift = d_shift
        self.d_slope = d_slope
        self.s_shift = s_shift
        self.s_slope = s_slope
        self.n_iterations = n_iterations
        self.initial_price = initial_price

    def demand(self, price):
        return self.d_shift - self.d_slope * price

    def supply(self, price):
        return self.s_shift + self.s_slope * price

    def find_cobweb(self):
        pe = (self.d_shift - self.s_shift) / (self.s_slope + self.d_slope)

        prices = [self.initial_price]
        quantities = [self.demand(self.initial_price)]

        for i in range(self.n_iterations):
            if i % 2 == 0:
                quantities.append(self.demand(prices[-1]))
            else:
                prices.append((self.initial_price - pe) * (self.s_slope / self.d_slope) ** i + pe)

        if len(prices) < len(quantities):
            prices.append((quantities[-1] - self.s_shift) / self.s_slope)

        price_range = np.linspace(0, self.n_iterations, 500)

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(x=price_range, y=self.demand(price_range), mode='lines', name="Demand", line=dict(color="blue")))
        fig.add_trace(
            go.Scatter(x=price_range, y=self.supply(price_range), mode='lines', name="Supply", line=dict(color="red")))

        for i in range(1, len(prices)):
            fig.add_trace(
                go.Scatter(x=[prices[i - 1], prices[i - 1]], y=[quantities[i - 1], quantities[i]], mode='lines',
                           line=dict(color="black", dash="dash"), showlegend=False))
            fig.add_trace(go.Scatter(x=[prices[i - 1], prices[i]], y=[quantities[i], quantities[i]], mode='lines',
                                     line=dict(color="black", dash="dash"), showlegend=False))

        fig.add_trace(go.Scatter(x=[pe], y=[pe], mode='markers',
                                 marker=dict(color="green", size=10), name="Equilibrium"))

        fig.update_layout(xaxis_title="Price", yaxis_title="Amount", template="plotly_white")

        fig.show()


# Приклад використання
model = EqCobweb(
    d_shift=20,  # зсув попиту
    d_slope=2,  # нахил попиту
    s_shift=10,  # зсув пропозиції
    s_slope=1,  # нахил пропозиції
    n_iterations=10,  # кількість ітерацій
    initial_price=10  # початкова ціна
)
model.find_cobweb()