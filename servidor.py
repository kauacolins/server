import socket
import threading

#192.168.250.157

HOST = '0.0.0.0'  # Aceita conexões de qualquer IP na rede local
PORT = 3003       # Porta para comunicação

# Criar o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor escutando em {HOST}:{PORT}")

# Função para lidar com um cliente individualmente
def handle_client(conn, addr):
    print(f"Nova conexão de {addr}")

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break  # Sai do loop se não receber dados (cliente desconectado)

            mensagem = data.decode()
            print(f"({addr[0]}:{addr[1]}) {mensagem}")  # Exibe IP, porta e mensagem recebida
            conn.sendall(b"Mensagem recebida pelo servidor!")

        except ConnectionResetError:
            break  # Cliente desconectado abruptamente

    print(f"Cliente {addr} desconectado.")
    conn.close()  # Fecha a conexão do cliente

# Loop para aceitar múltiplos clientes
while True:
    conn, addr = server_socket.accept()  # Aceita um novo cliente
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()  # Inicia uma thread para cada cliente
