from tools.models import go, np

class EqCobweb:
    def __init__(self, d_shift, d_slope, s_shift, s_slope, n_iterations, initial_price):
        self.d_shift = d_shift
        self.d_slope = d_slope
        self.s_shift = s_shift
        self.s_slope = s_slope
        self.n_iterations = n_iterations
        self.initial_price = initial_price
        self.prices = [self.initial_price]

    def eq_price(self):
        pe = (self.s_shift - self.d_shift) / (self.d_slope - self.s_slope)
        return pe

    def demand(self, price):
        return self.d_shift + self.d_slope * price 

    def supply(self, price):
        return self.s_shift + self.s_slope * price

    def find_eq_cobweb(self):
        pe = self.eq_price()

        for i in range(1, self.n_iterations + 1):
            price = (self.initial_price - pe) * (self.s_slope / self.d_slope) ** i + pe
            self.prices.append(price)

        p_min = min(self.prices) - (max(self.prices) - min(self.prices)) * 0.5
        p_max = max(self.prices) + (max(self.prices) - min(self.prices)) * 0.5
        p_range = np.linspace(p_min, p_max, 200)

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=self.demand(p_range), y=p_range, mode='lines', name="Demand", line=dict(color="blue"), showlegend=True))
        fig.add_trace(go.Scatter(x=self.supply(p_range), y=p_range, mode='lines', name="Supply", line=dict(color="red"), showlegend=True))

        q_equilibrium = self.s_shift + (self.s_slope * pe)
        fig.add_trace(
            go.Scatter(x=[q_equilibrium], y=[pe],
                    mode='markers', marker=dict(color="green", size=10),
                    name="Equilibrium"))

        for i in range(len(self.prices) - 1):
            #horizontal
            fig.add_trace(go.Scatter(
                x=[self.demand(self.prices[i]), self.supply(self.prices[i])],
                y=[self.prices[i], self.prices[i]],
                mode='lines', line=dict(color="black"),
                showlegend=False
            ))

            #vertical
            if i < len(self.prices) - 1:
                fig.add_trace(go.Scatter(
                    x=[self.supply(self.prices[i]), self.demand(self.prices[i+1])],
                    y=[self.prices[i], self.prices[i + 1]],
                    mode='lines', line=dict(color="black"),
                    showlegend=False
                ))

        fig.update_layout(xaxis_title="Quantity", yaxis_title="Price", template="plotly_white")

        return fig

    def return_periods_and_prices(self):
        return self.n_iterations, self.prices


# model = EqCobweb(
#     d_shift=100,    # Початковий попит
#     d_slope=5,      # Чутливість попиту до зміни ціни
#     s_shift=20,     # Початкова пропозиція
#     s_slope=3,      # Чутливість пропозиції до зміни ціни
#     n_iterations=20, # Кількість ітерацій павутиння
#     initial_price=50
# )
#
# fig = model.find_eq_cobweb()
# fig.show()