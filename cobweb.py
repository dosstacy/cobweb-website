import plotly.graph_objs as go
import plotly.io as pio
import numpy as np

class Cobweb:
    def __init__(self, d_shift, d_slope, s_shift, s_slope, n_iterations, initial_price):
        self.d_shift = d_shift
        self.d_slope = d_slope
        self.s_shift = s_shift
        self.s_slope = s_slope
        self.n_iterations = n_iterations
        self.initial_price = initial_price

# d_shift = 10
# d_slope = 1
# s_shift = 2
# s_slope = 0.8
# n_iterations = 15
# initial_price = 5

    def demand(self, price):
        return self.d_shift - self.d_slope * price

    def supply(self, price):
        return self.s_shift + self.s_slope * price


    def find_cobweb(self):
        # Розрахунок рівноваги
        equilibrium_price = (self.d_shift - self.s_shift) / (self.d_slope + self.s_slope)
        equilibrium_quantity = self.demand(equilibrium_price)

        # Побудова павутини
        prices = [self.initial_price]
        quantities = [self.demand(self.initial_price)]

        for i in range(self.n_iterations):
            if i % 2 == 0:
                quantities.append(self.demand(prices[-1]))
            else:
                prices.append((quantities[-1] - self.s_shift) / self.s_slope)

        if len(prices) < len(quantities):
            prices.append((quantities[-1] - self.s_shift) / self.s_slope)

        # Побудова графіка
        price_range = np.linspace(0, self.n_iterations, 500)

        fig = go.Figure()

        # Лінії попиту та пропозиції
        fig.add_trace(go.Scatter(x=price_range, y=self.demand(price_range), mode='lines', name="Demand", line=dict(color="blue")))
        fig.add_trace(go.Scatter(x=price_range, y=self.supply(price_range), mode='lines', name="Supply", line=dict(color="red")))

        # Павутинні лінії
        for i in range(1, len(prices)):
            fig.add_trace(go.Scatter(x=[prices[i-1], prices[i-1]], y=[quantities[i-1], quantities[i]], mode='lines', line=dict(color="black", dash="dash"),showlegend=False))
            fig.add_trace(go.Scatter(x=[prices[i-1], prices[i]], y=[quantities[i], quantities[i]], mode='lines', line=dict(color="black", dash="dash"),showlegend=False))

        # Точка рівноваги
        fig.add_trace(go.Scatter(x=[equilibrium_price], y=[equilibrium_quantity], mode='markers', marker=dict(color="green", size=10), name="Equilibrium"))

        # Оформлення
        fig.update_layout(xaxis_title="Price", yaxis_title="Amount", template="plotly_white")

        return fig

    def generate_image(self, fig):
        fig.write_image("cobweb.png")

    def generate_graph(self, fig):
        return pio.to_json(fig)