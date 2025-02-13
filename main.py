from flask import Flask, request, render_template, jsonify, url_for, redirect
from cobweb import *

app = Flask(__name__)

models = {
    "cobweb": {"name": "Cobweb Model", "fields": ["Demand shift", "Demand slope", "Supply shift", "Supply slope", "Iterations", "Initial price"]},
    "demand": {"name": "Demand Model", "fields": ["Ціна", "Обсяг", "Еластичність"]},
    "supply": {"name": "Supply Model", "fields": ["Кількість", "Витрати", "Рентабельність"]},
}

cobweb = 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/model", methods=["GET"])
def model_page():
    return render_template("data.html", model=get_model_name(), graph_json=cobweb)

@app.route("/model", methods=["POST"])
def model_page_post():
    data = request.json

    if not data:
        return "Помилка: не отримано JSON", 400
    else:
        print("Отримані дані:", data)

    cobweb = Cobweb(data["demand shift"], data["demand slope"], data["supply shift"], data["supply slope"], data["iterations"], data["initial price"])

    return jsonify({"graph_json": cobweb.find_cobweb()})

def get_model_name():
    model_name = request.args.get("name")
    model = models.get(model_name)
    if not model:
        return "Model is not found", 404
    return model

if __name__ == "__main__":
    app.run(debug=True)