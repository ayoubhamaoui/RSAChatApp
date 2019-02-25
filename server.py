import time, socket, sys
import pickle

print('Setup Server...')
time.sleep(1)
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
soc.bind((host_name, port))
print(host_name, '({})'.format(ip))
name = input('Enter name: ')
soc.listen(1) #Try to locate using socket
print('Waiting for incoming connections...')
connection, addr = soc.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")
print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
#get a connection from client side
client_name = connection.recv(1024)
client_name = client_name.decode()

n_client = connection.recv(1024)
e_client = connection.recv(1024)

n_client = int(n_client.decode())
e_client = int(e_client.decode())

print(client_name+":  e="+str(e_client)+" n="+str(n_client))


print(client_name + ' has connected.')
print('Press [bye] to leave the chat room')
connection.send(name.encode())
while True:
   message = input('Me > ')
   if message == '[bye]':
      message = 'Good Night...'
      connection.send(message.encode())
      print("\n")
      break

   dataE=[]
   for i in range(0,len(message)):
        C=(ord(message[i])**e_client)%n_client
        dataE.append(C)
   print(dataE)
   dataS=pickle.dumps(dataE)
   connection.send(dataS)

   #for car in dataE:
         #connection.sendall(str(car).encode())
         #time.sleep(1)

   #message = connection.recv(1024)
   #message = message.decode()
   print(client_name, '>', message)
