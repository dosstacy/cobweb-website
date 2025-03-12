from models.cobweb_equations import *
from models.adaptive_expectations import *
from models.cobweb_functions import *
from models.demand_and_supply import *
from models import generate_graph
from utils import jsonify

def find_model_solution(model_name, data):
    if model_name == "cobweb":
        return find_eq_cobweb_solution(data)
    elif model_name == "cobweb_func":
        return find_func_cobweb_solution(data)
    elif model_name == "adapt_exp":
        return find_adapt_expect_solution(data)
    elif model_name == "demand_supply":
        return find_demand_supply_solution(data)

def find_eq_cobweb_solution(data):
    eq_cobweb = EqCobweb(data["demand shift"], data["demand slope"], data["supply shift"], data["supply slope"],
                         data["iterations"], data["initial price"])
    return jsonify({"graph_json": generate_graph(eq_cobweb.find_eq_cobweb())})

def find_func_cobweb_solution(data):
    func_cobweb = FuncCobweb(data["function"], data["min value on x-axis"], data["max value on x-axis"],
                             data["min value on y-axis"], data["max value on y-axis"], data["seed"], data["iterations"])
    return jsonify({"graph_json": generate_graph(func_cobweb.find_func_cobweb())})

def find_adapt_expect_solution(data):
    adapt_exp = AdaptiveExpectations(data["previous price"], data["normal price"], data["adjustment factor"],
                                     data["periods"])
    time_steps, prices = adapt_exp.ad_exp()
    figure = adapt_exp.draw_graph(time_steps, prices)
    return jsonify({"graph_json": generate_graph(figure)})

def find_demand_supply_solution(data):
    demand_supply = DemandSupply(data["demand shift"], data["demand slope"], data["supply shift"], data["supply slope"],
                                 data["start price"], data["end price"], data["functions"])
    return jsonify({"graph_json": generate_graph(demand_supply.find_demand_supply())})