from api import request, render_template
from api import check_model, find_model_solution

def configure_models(app):
    @app.route("/model/<model_name>", methods=["GET"])
    def model_get_page(model_name):
        graph_json = 0
        model = check_model(model_name)

        return render_template("data.html", model=model, model_name=model_name, graph_json=graph_json)

    @app.route("/model/<model_name>", methods=["POST"])
    def model_post_page(model_name):
        model = check_model(model_name)
        print("model name: ", model_name)
        print("model: ", model)

        data = request.json

        if not data:
            return "Error: JSON is not found", 400
        else:
            print("Data obtained:", data)

        return find_model_solution(model_name, data)