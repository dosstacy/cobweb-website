from tools.models import symbols, sympify, lambdify, go, np
from tools import convert_to_sympy

##TODO: 1. edit text pages
##TODO: 4. add modal window for solution error
##TODO: 9. придумати якийсь прикол з n-1
##TODO: 5. спробувати переробити модель нормальної ціни та адаптивних очікувань під ті рівняння, які я розв'язала
##TODO: 6. пофіксити карусель

class FuncCobweb:
    def __init__(self, str_func, x_min, x_max, y_min, y_max, seed, iterates):
        self.str_func = str_func
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.seed = seed ##початкове значення, звідки починається графік
        self.iterates = iterates
        self.prices = []

    def find_func_cobweb(self):
        x_sym = symbols('x')
        expr = sympify(convert_to_sympy(self.str_func))
        print(expr)
        func = lambdify(x_sym, expr, "numpy")

        x_values = np.linspace(self.x_min, self.x_max, 1000)
        y_values = func(x_values)

        cobweb_x = [self.seed]
        cobweb_y = [self.seed]

        for i in range(self.iterates):
            y_new = func(cobweb_x[-1])
            cobweb_x.append(cobweb_x[-1])
            cobweb_y.append(y_new)

            cobweb_x.append(y_new)
            cobweb_y.append(y_new)

        iteration_points_x = [self.seed]
        iteration_points_y = [self.seed]
        x_current = self.seed

        for i in range(self.iterates):
            x_current = func(x_current)
            iteration_points_x.append(x_current)
            iteration_points_y.append(x_current)

        self.prices = iteration_points_y
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=x_values,
            y=y_values,
            mode='lines',
            name=f"f(x) = {self.str_func}",
            line=dict(color="red", width=2),
            showlegend=True
        ))

        fig.add_trace(go.Scatter(
            x=x_values,
            y=x_values,
            mode='lines',
            name="y = x",
            line=dict(color="blue", width=2),
            showlegend=True
        ))

        fig.add_trace(go.Scatter(
            x=cobweb_x,
            y=cobweb_y,
            mode='lines',
            name="Cobweb",
            line=dict(color="black", width=1.5),
            showlegend=False
        ))

        fig.update_layout(
            xaxis=dict(range=[self.x_min, self.x_max]),
            yaxis=dict(range=[self.y_min, self.y_max]),
            xaxis_title="x",
            yaxis_title="f(x)",
            template="plotly_white",
            legend=dict(x=0.01, y=0.99, bordercolor="Black", borderwidth=1)
        )

        return fig

    def return_periods_and_prices(self):
        return self.iterates, self.prices

# if __name__ == "__main__":
#     model = FuncCobweb(
#         str_func="4*x*(1-x)",
#         x_min=-0.1,
#         x_max=1.5,
#         y_min=0,
#         y_max=1.2,
#         seed=0.1,
#         iterates=5
#     )
#
#     fig = model.find_func_cobweb()
#     fig.show()