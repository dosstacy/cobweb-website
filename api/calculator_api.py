from flask import session

from api import render_template, request, calculate_eq, jsonify
from sympy import latex, sympify

##TODO: не можуть бути дублікати (n+1) і тд


def configure_calculator(app):
    @app.route("/calculator", methods=["GET"])
    def calc_get_page():
        lang = session["lang"]
        return render_template("calculator.html", language=lang)

    @app.route("/calculator", methods=["POST"])
    def calc_post_page():
        data = request.json
        if not data:
            return jsonify({"error": "JSON is not found"}), 400

        result = calculate_eq(data)

        if isinstance(result, tuple):
            general_result, final_result = result

            latex_general = latex(sympify(general_result))
            latex_final = latex(sympify(final_result))
            if session["lang"] == "en":
                html_output = f"<p>General solution: $${latex_general}$$</p>"
                html_output += f"<p>Partial solution: $${latex_final}$$</p>"
            else:
                html_output = f"<p>Všeobecné riešenie: $${latex_general}$$</p>"
                html_output += f"<p>Čiastočné riešenie: $${latex_final}$$</p>"

            return jsonify({
                "general_solution": latex_general,
                "final_solution": latex_final,
                "html": html_output
            })
        else:
            general_result = result

            latex_general = latex(sympify(general_result))
            if session["lang"] == "en":
                html_output = f"<p>General solution: $${latex_general}$$</p>"
            else:
                html_output = f"<p>Všeobecné riešenie: $${latex_general}$$</p>"

            return jsonify({
                "general_solution": latex_general,
                "html": html_output
            })
