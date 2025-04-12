from api import render_template, request, calculate_eq, jsonify
from sympy import latex


def configure_calculator(app):
    @app.route("/calculator", methods=["GET"])
    def calc_get_page():
        return render_template("calculator.html")

    @app.route("/calculator", methods=["POST"])
    def calc_post_page():
        data = request.json
        if not data:
            return jsonify({"error": "JSON is not found"}), 400

        solution = calculate_eq(data)  # Отримуєте розв'язок
        latex_solution = latex(solution)  # Перетворюєте у LaTeX (не забудьте from sympy import latex)
        return jsonify({
            "solution": latex_solution,
            "html": f"<p>Розв'язок: $${latex_solution}$$</p>"
        })
