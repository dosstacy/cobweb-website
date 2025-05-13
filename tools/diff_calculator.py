from sympy import rsolve, Eq, Function, solve, sin, cos, exp, log, expand
from tools import convert_to_sympy
from tools.models import symbols, sympify

class Calculator:
    def __init__(self, equation, p0, p1):
        self.equation = equation
        self.p0 = p0
        self.p1 = p1

    def calculate_diff_eq(self):
        n = symbols('n', integer=True)
        x_func = Function('x')

        eq_str = convert_to_sympy(self.equation)
        left_side, right_side = eq_str.split("=")


        left_expr = sympify(left_side.strip(), locals={'x': x_func, 'n': n, 'sin': sin, 'cos': cos, 'exp': exp, 'log': log})
        right_expr = sympify(right_side.strip(), locals={'n': n, 'sin': sin, 'cos': cos, 'exp': exp, 'log': log})

        rhs = expand(right_expr)
        print('expanded right side: ')
        print(rhs)
        eq = Eq(left_expr, rhs)
        print("Equation:", eq)
        general_solution = rsolve(eq, x_func(n))
        general_result = str(general_solution)

        if self.p0 == "" and self.p1 == "":
            return general_result

        C0, C1 = symbols('C0 C1')
        x_general = general_solution.subs({'C0': C0, 'C1': C1})

        equations = []

        if self.p0.strip():
            self.p0 = float(self.p0)
            equations.append(Eq(x_general.subs(n, 0), self.p0))

        if self.p1.strip():
            self.p1 = float(self.p1)
            equations.append(Eq(x_general.subs(n, 1), self.p1))

        constants = (C0, C1) if len(equations) == 2 else (C0,) if len(equations) == 1 else ()
        constants_solution = solve(equations, constants)

        particular_solution = x_general.subs(constants_solution)
        particular_simple = particular_solution.simplify()
        final_result = str(particular_simple)

        if general_result is None or final_result is None:
            raise ValueError("Result is None.")


        return general_result, final_result