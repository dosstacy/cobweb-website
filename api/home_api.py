from api import render_template, session

def configure_routes(app):
    @app.route("/")
    def home():
        lang = session["lang"]
        return render_template("index.html", language=lang)
