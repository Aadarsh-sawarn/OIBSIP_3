
import socket
import threading 
# from server import send_message_to_client


HOST = '127.0.0.1'
PORT = 5500

def listen_to_server(client):
    while 1:
     
        message=client.recv(2048).decode('utf-8')
        if message !='':
            user_name=message.split("~")[0]
            content=message.split('~')[1]
            print(f"[{user_name}] {content.replace('{user_name}', user_name)}")

        else:
            print(f"Message should not be vacant")

def Send_to_Server(client):
    while True:
        message = input("Enter Your Meassage: ")
        if message !='':
            client.sendall(message.encode())

        else:
            print("Message is Vacant")
            exit(0)


def connect_to_server(client):
    user_name = input("Please Enter your user Name: ")
    if user_name !='':
      client.sendall(user_name.encode())
          
    else:
          print("UserName should not be Vacant")
          exit(0)
        
    threading.Thread( target= listen_to_server, args= (client,)).start()

    Send_to_Server(client)


def main():
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
        print("RUNNING CLIENT")

    except:
        print("Cannot connect to the server {HOST} {PORT}")

        
    connect_to_server(client)


if __name__ == '__main__' :
    main()    
          



