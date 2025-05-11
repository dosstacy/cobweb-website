from tools.models import go, np, demand, supply

class DemandSupply:
    def __init__(self, d_shift, d_slope, s_shift, s_slope, start_price, end_price, function, lang):
        self.d_shift = d_shift
        self.d_slope = d_slope
        self.s_shift = s_shift
        self.s_slope = s_slope
        self.start_price = start_price
        self.end_price = end_price
        self.function = function
        self.lang = lang

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

        if self.lang == "en":
            match self.function:
                case "linear" | "lineárna":
                    fig.add_trace(go.Scatter(x=supply(self.s_shift, self.s_slope, p_range), y=p_range, mode='lines', name="Supply", line=dict(color="red"), showlegend=True))
                    fig.add_trace(go.Scatter(x=demand(self.d_shift, self.d_slope, p_range), y=p_range, mode='lines', name="Demand", line=dict(color="blue"), showlegend=True))
                case "cos":
                    fig.add_trace(go.Scatter(x=p_range, y=self.cos_demand(p_range), mode='lines', name="Demand", line=dict(color="blue"), showlegend=True))
                    fig.add_trace(go.Scatter(x=p_range, y=self.cos_supply(p_range), mode='lines', name="Supply", line=dict(color="red"), showlegend=True))
                case "exp":
                    fig.add_trace(go.Scatter(x=p_range, y=self.exp_demand(p_range), mode='lines', name="Demand", line=dict(color="blue"), showlegend=True))
                    fig.add_trace(go.Scatter(x=p_range, y=self.exp_supply(p_range), mode='lines', name="Supply", line=dict(color="red"), showlegend=True))
                case "ln":
                    fig.add_trace(go.Scatter(x=p_range, y=self.ln_demand(p_range), mode='lines', name="Demand", line=dict(color="blue"), showlegend=True))
                    fig.add_trace(go.Scatter(x=p_range, y=self.ln_supply(p_range), mode='lines', name="Supply", line=dict(color="red"), showlegend=True))

            fig.update_layout(xaxis_title="Quantity", yaxis_title="Price", template="plotly_white")
        else:
            match self.function:
                case "lineárna":
                    fig.add_trace(go.Scatter(x=supply(self.s_shift, self.s_slope, p_range), y=p_range, mode='lines', name="Ponuka", line=dict(color="red"), showlegend=True))
                    fig.add_trace(go.Scatter(x=demand(self.d_shift, self.d_slope, p_range), y=p_range, mode='lines', name="Dopyt", line=dict(color="blue"), showlegend=True))
                case "cos":
                    fig.add_trace(go.Scatter(x=p_range, y=self.cos_demand(p_range), mode='lines', name="Ponuka", line=dict(color="red"), showlegend=True))
                    fig.add_trace(go.Scatter(x=p_range, y=self.cos_supply(p_range), mode='lines', name="Dopyt", line=dict(color="blue"), showlegend=True))
                case "exp":
                    fig.add_trace(go.Scatter(x=p_range, y=self.exp_demand(p_range), mode='lines', name="Ponuka", line=dict(color="red"), showlegend=True))
                    fig.add_trace(go.Scatter(x=p_range, y=self.exp_supply(p_range), mode='lines', name="Dopyt", line=dict(color="blue"), showlegend=True))
                case "ln":
                    fig.add_trace(go.Scatter(x=p_range, y=self.ln_demand(p_range), mode='lines', name="Ponuka", line=dict(color="red"), showlegend=True))
                    fig.add_trace(go.Scatter(x=p_range, y=self.ln_supply(p_range), mode='lines', name="Dopyt", line=dict(color="blue"), showlegend=True))

            fig.update_layout(xaxis_title="Množstvo", yaxis_title="Cena", template="plotly_white")

        return fig