from models import go, np

class DemandSupply:
    def __init__(self, d_shift, d_slope, s_shift, s_slope, start_price, end_price, function):
        self.d_shift = d_shift
        self.d_slope = d_slope
        self.s_shift = s_shift
        self.s_slope = s_slope
        self.start_price = start_price
        self.end_price = end_price
        self.function = function

    def linear_demand(self, price):
        return self.d_shift + self.d_slope * price

    def linear_supply(self, price):
        return self.s_shift + self.s_slope * price

    def cos_demand(self, price):
        return self.d_shift + self.d_slope * np.cos(price)

    def cos_supply(self, price):
        return self.s_shift + self.s_slope * np.cos(price)

    def exp_demand(self, price):
        return self.d_shift + self.d_slope * np.exp(price)

    def exp_supply(self, price):
        return self.s_shift + self.s_slope * np.exp(price)

    def ln_demand(self, price):
        return self.d_shift + self.d_slope * np.log(price)

    def ln_supply(self, price):
        return self.s_shift + self.s_slope * np.log(price)

    def find_demand_supply(self):
        p_range = np.linspace(self.start_price, self.end_price, 200)
        print(p_range)

        fig = go.Figure()

        match self.function:
            case "linear":
                fig.add_trace(go.Scatter(x=p_range, y=self.linear_demand(p_range), mode='lines', name="Demand", line=dict(color="blue"), showlegend=True))
                fig.add_trace(go.Scatter(x=p_range, y=self.linear_supply(p_range), mode='lines', name="Supply", line=dict(color="red"), showlegend=True))
            case "cos":
                fig.add_trace(go.Scatter(x=p_range, y=self.cos_demand(p_range), mode='lines', name="Demand", line=dict(color="blue"), showlegend=True))
                fig.add_trace(go.Scatter(x=p_range, y=self.cos_supply(p_range), mode='lines', name="Supply", line=dict(color="red"), showlegend=True))
            case "exp":
                fig.add_trace(go.Scatter(x=p_range, y=self.exp_demand(p_range), mode='lines', name="Demand", line=dict(color="blue"), showlegend=True))
                fig.add_trace(go.Scatter(x=p_range, y=self.exp_supply(p_range), mode='lines', name="Supply", line=dict(color="red"), showlegend=True))
            case "ln":
                fig.add_trace(go.Scatter(x=p_range, y=self.ln_demand(p_range), mode='lines', name="Demand", line=dict(color="blue"), showlegend=True))
                fig.add_trace(go.Scatter(x=p_range, y=self.ln_supply(p_range), mode='lines', name="Supply", line=dict(color="red"), showlegend=True))

        fig.update_layout(xaxis_title="Price", yaxis_title="Quantity", template="plotly_white")

        return fig