import socket
import threading

HOST = '127.0.0.1'
PORT = 9753

def handle_client(client_socket, addr):
    print(f"[SERVER] New connection from {addr}")

    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            print(f"[SERVER] Client {addr} disconnected")
            break

        print(f"[FROM {addr}] {data}")

        if data.lower() == "exit":
            client_socket.send("Goodbye from server!".encode('utf-8'))
            break

        # Echo back
        reply = f"Echo from server: {data}"
        client_socket.send(reply.encode('utf-8'))

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[SERVER] Listening on {HOST}:{PORT} ...")

    while True:
        client_socket, addr = server_socket.accept()
        # Start a new thread for each client
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()
        print(f"[SERVER] Active connections: {threading.active_count() - 1}")

if __name__ == "__main__":
    main()

