import plotly.graph_objs as go
import numpy as np
import plotly.io as pio

# d_shift = 100
# d_slope = -3
# s_shift = 20
# s_slope = 2

# p0 = 12
# n = 4

class EqCobweb: 
    def __init__(self, d_shift, d_slope, s_shift, s_slope, n_iterations, initial_price):
        self.d_shift = d_shift
        self.d_slope = d_slope
        self.s_shift = s_shift
        self.s_slope = s_slope
        self.n_iterations = n_iterations
        self.initial_price = initial_price

    def eq_price(self):
        pe = (self.d_shift + self.s_shift ) / (self.s_slope + self.d_slope )
        print(f"Eequilibrium price: {pe}")
        return pe

    def demand(self, price):
        print("Demand ", self.d_shift - self.d_slope * price)
        return self.d_shift - self.d_slope * price 

    def supply(self, price):
        print("Supply ", self.s_shift + self.s_slope * price)
        return self.s_shift + self.s_slope * price

    def find_eq_cobweb(self):
        prices = []

        pe = self.eq_price()

        for i in range(1, self.n_iterations + 1):
            price = (self.initial_price - pe) * (self.s_slope / self.d_slope) ** i + pe
            prices.append(price)

        p_range = np.linspace(0, max(prices) * 1.2, 100)

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(x=p_range, y=self.demand(p_range), mode='lines', name="Demand", line=dict(color="blue"), showlegend=True))
        fig.add_trace(
            go.Scatter(x=p_range, y=self.supply(p_range), mode='lines', name="Supply", line=dict(color="red"), showlegend=True))


        q_equilibrium = self.d_shift + self.d_slope * pe
        fig.add_trace(
            go.Scatter(x=[q_equilibrium], y=[pe],
                    mode='markers', marker=dict(color="green", size=10),
                    name="Equilibrium"))


        prices = [self.initial_price] + prices  
        for i in range(len(prices) - 1):
            q_demand = self.d_shift + self.d_slope * prices[i]

            fig.add_trace(go.Scatter(
                x=[q_demand, q_demand],
                y=[prices[i], prices[i + 1]],
                mode='lines', line=dict(color="black", dash="dash"),
                showlegend=False
            ))

            if i < len(prices) - 1:
                q_next = self.d_shift + self.d_slope * prices[i + 1]
                fig.add_trace(go.Scatter(
                    x=[q_demand, q_next],
                    y=[prices[i + 1], prices[i + 1]],
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
#     d_shift=50,    # вільний член кривої попиту
#     d_slope=-2,     # нахил кривої попиту
#     s_shift=-10,     # вільний член кривої пропозиції
#     s_slope=3,     # нахил кривої пропозиції
#     n_iterations=4,
#     initial_price=12
# )

# fig = model.find_eq_cobweb()
# fig.show()