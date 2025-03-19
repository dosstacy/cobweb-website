from models import go


class PPDependency:
    def __init__(self, n_iterations, prices):
        self.n_iterations = n_iterations
        self.prices = prices

    def find_pp_dependency(self):
        x_values = []
        y_values = []

        for i in range(len(self.prices)):
            x_values.extend([i, i + 1])
            y_values.extend([self.prices[i], self.prices[i]])

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', line=dict(color="blue")))
        fig.update_layout(xaxis_title="Periods", yaxis_title="Price", template="plotly_white")

        return fig

# a = PPDependency(
#     n_iterations=20,
#     prices=[50, -14.0, 24.4, 1.3600000000000012, 15.184, 6.889600000000001, 11.86624, 8.880256, 10.6718464, 9.59689216, 10.241864704, 9.8548811776, 10.08707129344, 9.947757223936, 10.0313456656384, 9.98119260061696, 10.011284439629824, 9.993229336222106, 10.004062398266736, 9.997562561039958, 10.001462463376026]
# )
# fig1 = a.find_pp_dependency()
# fig1.show()