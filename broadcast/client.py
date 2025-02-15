import socket
import threading

class Client:
    def __init__(self, host='127.0.0.1', port=5555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        
    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode()
                print(message)
            except:
                print("Connection lost!")
                self.client.close()
                break
    
    def send_message(self, message):
        self.client.send(message.encode())
    
    def start(self):
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()
        
        while True:
            message = input("")
            if message.lower() == 'quit':
                self.client.close()
                break
            self.send_message(message)

if __name__ == "__main__":
    client = Client()
    client.start()



'''
notes

Threads (like having multiple helpers at the party)
Sockets (like phone lines between the server and clients)
Lists (to keep track of who's at the party)

'''
