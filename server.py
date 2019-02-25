import time, socket, sys
import pickle


################################################
import socket                                         
import time
import pickle
import random
import math 

check = True


def modexpo(a, n, m):
    if n == 0:
        return 1;
    if n % 2 == 0:
        res = modexpo(a, n / 2, m)
        return (res % m * res % m) % m
    else:
        res = modexpo(a, n / 2, m)
        return a * res * res % m



prime=[]
prime.append(2)
def prime_List():
  L=[]
  L.append(2)
  for i in range(3,100):
    check=True
    for  j in L:
        if not (i%j):
            check=False
    if check:
        L.append(i)
  return L

prime=prime_List()



def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
 
def modInverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


#gcd function
def gcd(a,b):
    return math.gcd(b,a)

#function to check if number is prime
def is_prime(x):
   if x >= 2:
      for y in range(2,x):
        if not ( x % y ):
          return False
   else:
     return False
   return True



p = q = 2
def find(p,q):
  i= random.randint(0, len(prime))
  j= random.randint(0, len(prime))
  p,q = prime[i],prime[j]
  return p,q

#find two prime number in prime list
p,q = find(p,q)
#p=1000000009
#q=1000000007



#calculate n=p*q
n=p*q

#calculate fn
fn = (p-1)*(q-1)

#select integer e / gcd(fn,e)=1, 1 < e < fn
e=2
while(e<n):
   if(gcd(fn,e) == 1):
      break 
   e = e+1


#calculate d / d*e = 1 mod(fn)
d=modInverse(e,fn)

#public key {e,n}
#private key {d,n}

#Encryption: M<n, C= M^e (mod n)
#Decryption C, M= C^d(mod n)

###################################################################



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
print('CLIENT:')
print(client_name+":  e="+str(e_client)+" n="+str(n_client))
print('################################')
print('SERVER:')
print("e: "+str(e)+" n: "+str(n)+" d: "+str(d))


print(client_name + ' has connected.')
print('Press [bye] to leave the chat room')
connection.send(name.encode())
time.sleep(3)
connection.send(str(n).encode())
time.sleep(3)
connection.send(str(e).encode())
while True:
   message = input('Me > ')
   if message == '[bye]':
      message = 'Good Night...'
      connection.send(message.encode())
      print("\n")
      break

   dataE=[]
   for i in range(0,len(message)):
        #C = modexpo(ord(message[i]), e_client, n_client)
        C=(ord(message[i])**e_client)%n_client
        dataE.append(C)
   print(dataE)
   dataS=pickle.dumps(dataE)
   connection.send(dataS)
   
   while 1:
      dataR = connection.recv(1024)
      data = pickle.loads(dataR)
      if data : break
      print(data)
   print(data)
   #message = soc.recv(1024)
   #message = message.decode()
   dataD=[]
   for i in range(len(data)):
      #dataD.append(chr(modexpo(data[i],d,n)))
      dataD.append(chr((data[i]**d)%n))

   #print(data)
   string = ''.join(dataD)
   print(string)
   #for car in dataE:
         #connection.sendall(str(car).encode())
         #time.sleep(1)

   #message = connection.recv(1024)
   #message = message.decode()
   print(client_name, '>', message)
