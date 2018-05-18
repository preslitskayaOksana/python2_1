# import socket
# from datetime import datetime
# server_address = ('localhost', 6789)
# max_size = 4096
# print('Starting the client at', datetime.now())
# client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client.sendto(b'Hey!', server_address)
# data, server = client.recvfrom(max_size)
# print('At', datetime.now(), server, 'said', data)
# client.close()


import socket
from datetime import datetime
address = ('localhost', 7777)
max_size = 1024
print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.send(b'hey')
data = client.recv(max_size)
print('вы подключились', data.decode('UTF-8'))
client.close()
