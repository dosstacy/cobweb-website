from utils import request, jsonify
from dictionaries.intros_dictionary import *
from dictionaries.models_dictionary import *
from dictionaries.params_dictionary import *

def check_model(model_name, lang="en"):
    if not model_name:
        return jsonify({"error": "Missing model name"}), 400

    if lang == "sk":
        model = models_sk.get(model_name)
    else:
        model = models.get(model_name)

    if not model:
        return jsonify({"error": "Unknown model"}), 400

    return model

def check_intro(intro_name, lang):
    if not intro_name:
        return jsonify({"error": "Missing intro name"}), 400

    if lang == "sk":
        intro = intros_sk.get(intro_name)
    else:
        intro = intros.get(intro_name)

    if not intro:
        return jsonify({"error": "Unknown intro"}), 400

    return intro

def check_params():
    params_name = request.args.get('name')
    if not params_name:
        return jsonify({"error": "Missing params name"}), 400

    param = params.get(params_name)

    if not param:
        return jsonify({"error": "Unknown params"}), 400

    return params_name, param