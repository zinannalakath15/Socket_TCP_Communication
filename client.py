import socket

HOST = '127.0.0.1'
PORT = 9753

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("[CLIENT] Connected to server.")
print("Type messages to send. Type 'exit' to close connection.\n")

while True:
    message = input("You: ")

    # Send message to server
    client_socket.send(message.encode('utf-8'))

    # If we want to end:
    if message.lower() == "exit":
        # Receive final server reply (optional)
        reply = client_socket.recv(1024).decode('utf-8')
        print("Server:", reply)
        print("[CLIENT] Connection closed.")
        break

    # Receive server response
    reply = client_socket.recv(1024).decode('utf-8')
    print("Server:", reply)

client_socket.close()
