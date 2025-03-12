from api import check_intro, render_template, check_params

def configure_info(app):
    @app.route("/intro", methods=["GET"])
    def intro_get_page():
        intro_name, intro = check_intro()
        return render_template("intros_base.html", intros=intro)

    @app.route("/params", methods=["GET"])
    def params_get_page():
        params_name, param = check_params()
        return render_template("params_base.html", params=param)