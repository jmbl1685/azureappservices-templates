from datetime import datetime
from src import app, jsonify, request


@app.route('/', methods=['GET'])
def home():
    data = {
        'message': 'Project running in Azure App Services'
    }

    response = jsonify(data)
    response.status_code = 200

    return response


@app.route('/', methods=['POST'])
def Post():
    body = request.json
    return jsonify(body)
