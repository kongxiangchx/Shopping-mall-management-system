import socket
import json


class Send_data:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('127.0.0.1', 5000))

    def message(self, data):
        dealdata = json.dumps(data)
        self.s.send(dealdata.encode())
        recvdata = self.s.recv(1024)
        recvdata = recvdata.decode()
        return json.loads(recvdata)

    def close(self):
        self.s.close()
