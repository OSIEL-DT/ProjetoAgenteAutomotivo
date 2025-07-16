import socket
import json

HOST = 'localhost'
PORT = 65432

def send_message(message: dict):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(message).encode('utf-8'))
        data = s.recv(100000)
    return json.loads(data.decode('utf-8'))

def start_server(on_request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)        
        s.bind((HOST, PORT))        
        s.listen()
        print("Servidor iniciado. Aguardando conexões...")
        print("==============================================================")        
        print(f"Servidor ouvindo em {HOST}:{PORT}...")
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(100000)
                if not data:
                    print("Conexão encerrada pelo cliente.")
                    continue                
                if not data:
                    continue
                request = json.loads(data.decode('utf-8'))
                response = on_request(request)
                conn.sendall(json.dumps(response).encode('utf-8'))
