import threading
import time
from app.server.server import filter_vehicles
from app.protocol import mcp

def run_test_server():
    mcp.start_server(filter_vehicles)

def test_client_server_interaction(monkeypatch):
    # Inicia o servidor em thread paralela
    thread = threading.Thread(target=run_test_server, daemon=True)
    thread.start()
    time.sleep(1)  # Aguarda o servidor iniciar

    filtros = {"brand": "Fiat"}
    response = mcp.send_message(filtros)
    assert isinstance(response, list)
    assert len(response) > 0
    assert all("brand" in v for v in response)  # Verifica se a resposta contém a chave "brand"
    assert all("model" in v for v in response)  # Verifica se a resposta contém a chave "model"
    assert all("year" in v for v in response)  # Verifica se a resposta contém a chave "year"
    assert all("color" in v for v in response)  # Verifica se a resposta contém a chave "color"
    assert all("mileage" in v for v in response)  # Verifica se a resposta contém a chave "mileage"
    assert all("price" in v for v in response)  # Verifica se a resposta contém a chave "price" 
    assert all(v["brand"] == "Fiat" for v in response)  # Verifica se todos os veículos retornados são da marca "Fiat"
    thread.join(timeout=5)  
    assert not thread.is_alive()   
    print("Teste de interação cliente-servidor concluído com sucesso.")