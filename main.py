from flask import Flask, request, render_template, jsonify
from cobweb import *
from adaptive_expectations import *

app = Flask(__name__)

models = {
    "cobweb": {"name": "Cobweb Model", "fields": ["Demand shift", "Demand slope", "Supply shift", "Supply slope", "Iterations", "Initial price"]},
    "adapt_exp": {"name": "Adaptive expectations", "fields": ["Previous price", "Normal price", "Adjustment factor", "Periods"]},
}

intros = {
    "cobweb": {
        "name": "Cobweb Model",
        "intro": "This economic model describes how changes in the price and quantity of a good on the market can lead to fluctuations instead of equilibrium. It is based on the assumption that producers make decisions about future output based on current prices, but do not take into account that prices may change. If supply and demand react with a delay, the market can fluctuate, forming a “spider's web” trajectory.",
    },
    "adapt_exp": {
        "name": "Adaptive expectations",
        "intro": "This model is used in economics to explain how people predict future values of economic indicators, such as price levels. It assumes that expectations about future prices are formed on the basis of previous data with gradual adjustments. If prices grow faster than expected, people begin to expect even higher growth in the future. This approach is used, for example, to analyze inflation.",
    },
    "diff_eq": {
        "name": "Difference equations",
        "intro": "These are mathematical equations that describe how a quantity changes at discrete points in time. They are analogous to differential equations, but are used when time is not considered continuous, but as a set of separate points (for example, years or months). Such equations are widely used in economics, physics, and computer modeling to predict the development of systems.",
    }
}

cobweb = 0
adapt_exp = 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/model", methods=["GET"])
def model_get_page():
    model_name, model = check_model()

    graph_json = cobweb if model_name == "cobweb" else adapt_exp

    return render_template("data.html", model=model, graph_json=graph_json)

@app.route("/model", methods=["POST"])
def model_post_page():
    model_name, model = check_model()
    print("model name: ", model_name)
    print("model: ", model)

    data = request.json

    if not data:
        return "Error: JSON is not found", 400
    else:
        print("Data obtained:", data)

    if model_name == "cobweb":
        cobweb = Cobweb(data["demand shift"], data["demand slope"], data["supply shift"], data["supply slope"], data["iterations"], data["initial price"])
        return jsonify({"graph_json": cobweb.generate_graph(cobweb.find_cobweb())})
    else:
        adapt_exp = AdaptiveExpectations(data["previous price"], data["normal price"], data["adjustment factor"], data["periods"])
        time_steps, prices = adapt_exp.ad_exp()
        figure = adapt_exp.draw_graph(time_steps, prices)
        return jsonify({"graph_json": adapt_exp.generate_graph(figure)})

@app.route("/intro", methods=["GET"])
def intro_get_page():
    intro_name, intro = check_intro()
    return render_template("intros_base.html", intros=intro)

@app.route("/calculator", methods=["GET"])
def calc_page():
    return render_template("calculator.html")

def check_model():
    model_name = request.args.get('name')
    if not model_name:
        return jsonify({"error": "Missing model name"}), 400

    model = models.get(model_name)

    if not model:
        return jsonify({"error": "Unknown model"}), 400

    return model_name, model

def check_intro():
    intro_name = request.args.get('name')
    if not intro_name:
        return jsonify({"error": "Missing intro name"}), 400

    intro = intros.get(intro_name)

    if not intro:
        return jsonify({"error": "Unknown intro"}), 400

    return intro_name, intro

if __name__ == "__main__":
    app.run(debug=True)