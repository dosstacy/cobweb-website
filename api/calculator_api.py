from api import render_template, request, calculate_eq

def configure_calculator(app):
    @app.route("/calculator", methods=["GET"])
    def calc_get_page():
        return render_template("calculator.html")

    @app.route("/calculator", methods=["POST"])
    def calc_post_page():
        data = request.json

        if not data:
            return "Error: JSON is not found", 400
        else:
            print("Data obtained:", data)

        return calculate_eq(data)
