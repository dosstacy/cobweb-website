from api import render_template

def configure_calculator(app):
    @app.route("/calculator", methods=["GET"])
    def calc_page():
        return render_template("calculator.html")
