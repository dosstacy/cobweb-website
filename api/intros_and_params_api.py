from api import check_intro, render_template, check_params, check_model
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
        print(model_name)
        param = check_params(model_name, lang)
        model = check_model(model_name, lang)
        return render_template("params_base.html", model=model, model_name=model_name, params=param, language=lang)