from flask import Flask, request, render_template, jsonify, url_for, redirect
from cobweb import *
from adaptive_expectations import *

app = Flask(__name__)

models = {
    "cobweb": {"name": "Cobweb Model", "fields": ["Demand shift", "Demand slope", "Supply shift", "Supply slope", "Iterations", "Initial price"]},
    "adapt_exp": {"name": "Adaptive expectations", "fields": ["Previous price", "Normal price", "Adjustment factor", "Periods"]},
}

cobweb = 0
adapt_exp = 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/model", methods=["GET"])
def model_page():
    model_name = request.args.get('name')
    if not model_name:
        return jsonify({"error": "Missing model name"}), 400

    model = models.get(model_name)

    if not model:
        return jsonify({"error": "Unknown model"}), 400

    graph_json = cobweb if model_name == "cobweb" else adapt_exp

    return render_template("data.html", model=model, graph_json=graph_json)


@app.route("/model", methods=["POST"])
def model_page_post():
    model_name = request.args.get('name')
    print("model name:", model_name)

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

@app.route("/calculator", methods=["GET"])
def calc_page():
    return render_template("calculator.html")

if __name__ == "__main__":
    app.run(debug=True)