import socket

HOST = '192.168.248.163'  # Endereço do servidor
PORT = 3003        # Porta usada pelo servidor

# Criar o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    msg = input("Digite uma mensagem (ou 'sair' para encerrar): ")
    print(f"Você digitou: {msg}")

    if msg.lower() == 'sair':
        print("Encerrando conexão com o servidor...")
        break

    client_socket.sendall(msg.encode())
    data = client_socket.recv(1024)
    print(f"Resposta do servidor: {data.decode()}")

client_socket.close()  # Fecha a conexão, mas o servidor continua rodando
