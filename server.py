#
# from datetime import datetime
# import socket
#
# server_address = ('localhost', 6789)
# max_size = 4096
# print('Starting the server at', datetime.now())
# print('Waiting for a client to call.')
# server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server.bind(server_address)
# data, client = server.recvfrom(max_size)
# print('At', datetime.now(), client, 'said', data)
# server.sendto(b'Are you talking to me?', client)
# server.close()


from datetime import datetime
import socket
address = ('localhost', 7777)
max_size = 1024
# print('Starting the server at', datetime.now())
# print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)


client, address = server.accept()
print('Получен запрос')
data = datetime.now()
tm = client.recv(max_size)
client.send(data.encode('UTF-8'))

client.close()





