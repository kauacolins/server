from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Permite conexões de qualquer origem

@socketio.on("connect")
def handle_connect():
    print("Um cliente se conectou.")

@socketio.on("disconnect")
def handle_disconnect():
    print("Um cliente se desconectou.")

@socketio.on("mensagem")
def handle_mensagem(data):
    print(f"Mensagem recebida: {data}")
    socketio.emit("resposta", f"Servidor recebeu: {data}")  # Envia para todos os clientes conectados

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=3003, debug=True)
