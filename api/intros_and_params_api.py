from api import check_intro, render_template, check_params
from flask import session

def configure_info(app):
    @app.route("/intro/<model_name>", methods=["GET"])
    def intro_get_page(model_name):
        lang = session["lang"]
        intro = check_intro(model_name, lang)
        return render_template("intros_base.html", intros=intro, language=lang, model=model_name)

    @app.route("/params/<model_name>", methods=["GET"])
    def params_get_page(model_name):
        lang = session["lang"]
        model_name, param = check_params()
        return render_template("params_base.html", params=param, language=lang, model=model_name)