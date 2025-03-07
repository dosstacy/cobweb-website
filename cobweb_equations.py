import plotly.graph_objs as go
import numpy as np
import plotly.io as pio

class EqCobweb: 
    def __init__(self, d_shift, d_slope, s_shift, s_slope, n_iterations, initial_price):
        self.d_shift = d_shift
        self.d_slope = d_slope
        self.s_shift = s_shift
        self.s_slope = s_slope
        self.n_iterations = n_iterations
        self.initial_price = initial_price

    def eq_price(self):
        pe = (self.s_shift - self.d_shift) / (self.d_slope - self.s_slope)
        return pe

    def demand(self, price):
        return self.d_shift + self.d_slope * price 

    def supply(self, price):
        return self.s_shift + self.s_slope * price

    def find_eq_cobweb(self):
        prices = [self.initial_price]

        pe = self.eq_price()

        for i in range(1, self.n_iterations + 1):
            price = (self.initial_price - pe) * (self.s_slope / self.d_slope) ** i + pe
            prices.append(price)

        print(prices)
        p_min = min(prices) - (max(prices) - min(prices)) * 0.5 
        p_max = max(prices) + (max(prices) - min(prices)) * 0.5
        p_range = np.linspace(p_min, p_max, 200)

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(x=self.demand(p_range), y=p_range, mode='lines', name="Demand", line=dict(color="blue"), showlegend=True))
        fig.add_trace(
            go.Scatter(x=self.supply(p_range), y=p_range, mode='lines', name="Supply", line=dict(color="red"), showlegend=True))

        q_equilibrium = self.s_shift + (self.s_slope * pe)
        fig.add_trace(
            go.Scatter(x=[q_equilibrium], y=[pe],
                    mode='markers', marker=dict(color="green", size=10),
                    name="Equilibrium"))

        for i in range(len(prices) - 1):
            #horizontal
            fig.add_trace(go.Scatter(
                x=[self.demand(prices[i]), self.supply(prices[i])],
                y=[prices[i], prices[i]],
                mode='lines', line=dict(color="black", dash="dash"),
                showlegend=False
            ))
            print(f"Coordinates: x=[", self.demand(prices[i]), self.demand(prices[i]), "], y=[",prices[i], prices[i + 1],"]")

            #vertical
            if i < len(prices) - 1:
                fig.add_trace(go.Scatter(
                    x=[self.supply(prices[i]), self.demand(prices[i+1])],
                    y=[prices[i], prices[i + 1]],
                    mode='lines', line=dict(color="black", dash="dash"),
                    showlegend=False
                ))

        fig.update_layout(
            xaxis_title="Amount",
            yaxis_title="Price",
            template="plotly_white"
        )

        return fig
        
    def generate_graph(self, fig):
        return fig.to_plotly_json()

# model = EqCobweb(
#     d_shift=100,    # Початковий попит
#     d_slope=5,      # Чутливість попиту до зміни ціни
#     s_shift=20,     # Початкова пропозиція
#     s_slope=3,      # Чутливість пропозиції до зміни ціни
#     n_iterations=20, # Кількість ітерацій павутиння
#     initial_price=50
# )

# fig = model.find_eq_cobweb()
# fig.show()