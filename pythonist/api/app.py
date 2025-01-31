import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/external-data', methods=['GET'])
def get_external_data():
    """Consulta uma API externa e retorna os dados."""
    url = "https://jsonplaceholder.typicode.com/posts/1"  # API de teste
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Falha ao obter dados"}), response.status_code


if __name__ == '__main__':
    app.run(debug=True)
