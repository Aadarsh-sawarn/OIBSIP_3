# Idea : Browser Based Chat Application

import socket
import threading

HOST = '127.0.0.1'
PORT = 5500
LISTENER_LIMIT = 6
active_clients = []

def listen_message (client, user_name):
    while 1:
        try:
            message = client.recv(2048).decode('utf-8')
            if message != '':
                final_message = f"{user_name}~{message}"
                sending_message_to_all (final_message)

            else:
             print(f"Message  sent from client {user_name} is vacant")
        except Exception as e:
            print(f"Error: {e}")
            break


def send_message_to_client(client, message):
    client.sendall(message.encode())

def sending_message_to_all (message):
    for user in active_clients:
        send_message_to_client (user[1], message)


def client_handler(client):
    while True:
        user_name = client.recv(2048).decode('utf-8')
        if user_name != '':
            active_clients.append((user_name,client))
            prompt_message = f"CHATBOT ~{user_name} entered into the chat"
            sending_message_to_all(prompt_message)
            break

        else:
            print("Username should not be VACANT")

    
    threading.Thread (target = listen_message, args = (client,user_name,)).start() 


def main():
    server = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    print ("the server is running on {HOST} {PORT}")
    try:
        server.bind ((HOST, PORT))
    except:
        print ("Unable to connect to Host {HOST}and port{PORT}")


    server.listen(LISTENER_LIMIT)


    while True:
            client , address = server.accept()
            print (f"Successfully connected to the client {address[0]} {address[1]}")
            threading.Thread(target = client_handler , args = (client,)).start()


if __name__ == '__main__':
    main()