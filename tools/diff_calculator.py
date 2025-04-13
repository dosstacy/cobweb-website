from sympy import rsolve, Eq, Function, solve
from tools import convert_to_sympy
from tools.models import symbols, sympify

class Calculator:
    def __init__(self, equation, p0, p1):
        self.equation = equation
        self.p0 = p0
        self.p1 = p1

    def calculate_diff_eq(self):
        n = symbols('n', integer=True)
        x = Function('x')

        eq_str = convert_to_sympy(self.equation)
        left_side, right_side = eq_str.split("=")

        left_expr = sympify(left_side.strip(), locals={'x': x, 'n': n})
        print(left_expr)
        right_expr = sympify(right_side.strip(), locals={'x': x, 'n': n})
        print(right_expr)

        eq = Eq(left_expr, right_expr)
        print("Equation:", eq)
        general_solution = rsolve(eq, x(n))
        print("General solution", general_solution)
        general_result = str(general_solution)

        if self.p0 is "" and self.p1 is "":
            return general_result

        C0, C1 = symbols('C0 C1')
        x_general = general_solution.subs({'C0': C0, 'C1': C1})

        equations = []

        if self.p0.strip() is not "":
            self.p0 = float(self.p0)
            equations.append(Eq(x_general.subs(n, 0), self.p0))

        if self.p1.strip() is not "":
            self.p1 = float(self.p1)
            equations.append(Eq(x_general.subs(n, 1), self.p1))

        constants = (C0, C1) if len(equations) == 2 else (C0,) if len(equations) == 1 else ()
        constants_solution = solve(equations, constants)

        particular_solution = x_general.subs(constants_solution)
        particular_simple = particular_solution.simplify()
        print("\nParticular solution with initial conditions:")
        print(particular_simple)
        final_result = str(particular_simple)

        return general_result, final_result