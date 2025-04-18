from api import session, request

def configure_language(app):
    @app.before_request
    def detect_language():
        lang = request.args.get("lang")
        if lang:
            session['lang'] = lang
        elif 'lang' not in session:
            session['lang'] = 'en'

    @app.route("/set-lang")
    def set_lang():
        new_lang = request.args.get("lang", "en")
        session["lang"] = new_lang
        return "", 204

    @app.route('/get-lang')
    def get_lang():
        lang = session.get('lang', 'en')
        return {'lang': lang}