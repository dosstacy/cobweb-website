from tools.models.adaptive_expectations import AdaptiveExpectations
from tools.models.demand_and_supply import DemandSupply
from tools.models.normal_price import NormalPrice
from tools.models.prices_periods_dependency import PPDependency
from tools.models.cobweb_equations import EqCobweb
from tools.models.cobweb_functions import FuncCobweb
from utils import jsonify, session
from tools.models import *
from tools.diff_calculator import Calculator

def find_model_solution(model_name, data):
    if model_name == "cobweb":
        return find_eq_cobweb_solution(data)
    elif model_name == "cobweb_func":
        return find_func_cobweb_solution(data)
    elif model_name == "normal_price":
        return find_normal_price_solution(data)
    elif model_name == "demand_supply":
        return find_demand_supply_solution(data)
    elif model_name == "adapt_exp":
        return find_adapt_exp_solution(data)

def find_eq_cobweb_solution(data):
    #if session['lang'] == 'en':
    eq_cobweb = EqCobweb(data["demand shift"], data["demand slope"], data["supply shift"], data["supply slope"],
                         data["iterations"], data["initial price"])
    # else:
    #     eq_cobweb = EqCobweb(data["posun dopytu"], data["sklon dopytu"], data["posun ponuky"], data["sklon ponuky"],
    #                          data["iterácie"], data["počiatočná cena"])

    graph_json = generate_graph(eq_cobweb.find_eq_cobweb())
    pp_graph_json = find_pp_dep(eq_cobweb)

    print("First plot:", graph_json)
    print("Second plot:", pp_graph_json)

    return jsonify({
        "graph_json": graph_json,
        "pp_graph_json": pp_graph_json
    })

def find_func_cobweb_solution(data):
    func_cobweb = FuncCobweb(data["function"], data["min value on x-axis"], data["max value on x-axis"],
                             data["min value on y-axis"], data["max value on y-axis"], data["seed"], data["iterations"])

    graph_json = generate_graph(func_cobweb.find_func_cobweb())

    return jsonify({
        "graph_json": graph_json,
        "pp_graph_json": find_pp_dep(func_cobweb)
    })

def find_normal_price_solution(data):
    normal_price = NormalPrice(data["previous price"], data["normal price"], data["adjustment factor"],
                               data["periods"])
    time_steps, prices = normal_price.ad_exp()
    figure = draw_graph(time_steps, prices)
    return jsonify({"graph_json": generate_graph(figure)})

def find_adapt_exp_solution(data):
    adapt_exp = AdaptiveExpectations(data["previous expected price"], data["previous actual price"], data["adaptation coefficient"])
    periods, prices = adapt_exp.find_adapt_expectation()
    figure = draw_graph(periods, prices)
    return jsonify({"graph_json": generate_graph(figure)})

def find_demand_supply_solution(data):
    demand_supply = DemandSupply(data["demand shift"], data["demand slope"], data["supply shift"], data["supply slope"],
                                 data["start price"], data["end price"], data["functions"])
    return jsonify({"graph_json": generate_graph(demand_supply.find_demand_supply())})

def find_pp_dep(cobweb_model):
    [periods, prices] = cobweb_model.return_periods_and_prices()
    pp_dep = PPDependency(periods, prices)
    return generate_graph(pp_dep.find_pp_dependency())

def calculate_eq(data):
    calculator = Calculator(data["equation"], data["p0"], data["p1"])
    return calculator.calculate_diff_eq()