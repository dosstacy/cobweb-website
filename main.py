from flask import Flask
from api.home_api import configure_routes
from api.calculator_api import configure_calculator
from api.models_api import configure_models
from api.intros_and_params_api import configure_info
app = Flask(__name__)

configure_routes(app)
configure_calculator(app)
configure_models(app)
configure_info(app)

if __name__ == "__main__":
    app.run(debug=True)