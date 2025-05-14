from flask import Flask
from api.home_api import configure_routes
from api.calculator_api import configure_calculator
from api.models_api import configure_models
from api.intros_and_params_api import configure_info
from api.language_api import configure_language
import os
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-key-for-dev')

configure_language(app)
configure_routes(app)
configure_calculator(app)
configure_models(app)
configure_info(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)