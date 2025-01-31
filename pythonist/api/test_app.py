import pytest

from pythonist.api.app import app


@pytest.fixture
def client():
    """Cria um cliente de teste do Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def mock_requests(requests_mock):
    """Fixture para mockar requests"""
    return requests_mock


def test_get_external_data_success(client, mock_requests):
    """Testa se a API retorna os dados corretamente quando a API externa responde com sucesso."""
    mock_url = "https://jsonplaceholder.typicode.com/posts/1"
    mock_response = {"userId": 1, "id": 1, "title": "Teste", "body": "Corpo do post"}

    mock_requests.get(mock_url, json=mock_response, status_code=200)

    response = client.get('/external-data')

    assert response.status_code == 200
    assert response.json == mock_response


def test_get_external_data_failure(client, mock_requests):
    """Testa se a API trata erros quando a API externa falha."""
    mock_url = "https://jsonplaceholder.typicode.com/posts/1"
    mock_requests.get(mock_url, status_code=500)

    response = client.get('/external-data')

    assert response.status_code == 500
    assert response.json == {"error": "Falha ao obter dados"}
