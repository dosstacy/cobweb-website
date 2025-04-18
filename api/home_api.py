from api import render_template, session, request

def configure_routes(app):
    @app.route("/")
    def home():
        lang = session["lang"]
        return render_template("index.html", language=lang)

    @app.route("/set-lang")
    def set_lang():
        new_lang = request.args.get("lang", "en")
        session["lang"] = new_lang
        return "", 204