from models import go

class AdaptiveExpectations:
    def __init__(self, p0, pN, c, periods):
        self.p0 = p0
        self.pN = pN
        self.c = c
        self.periods = periods

    def ad_exp(self):
        prices = [self.p0]
        for t in range(1, self.periods + 1):
            pt = prices[-1] + self.c * (self.pN - prices[-1])
            prices.append(pt)
        print("Final prices:", prices)
        return list(range(self.periods + 1)), prices

    def draw_graph(self, time_steps, prices):
        trace = go.Scatter(x=time_steps, y=prices, mode='lines+markers', name='Expected price')
        layout = go.Layout(xaxis=dict(title='Periods'), yaxis=dict(title='Price'))
        figure = go.Figure(data=[trace], layout=layout)

        return figure
