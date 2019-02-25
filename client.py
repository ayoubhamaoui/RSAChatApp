import time, socket, sys
import pickle

################################################
import socket                                         
import time
import pickle
import random
import math



def modexpo(a, n, m):
    if n == 0:
        return 1
    if n % 2 == 0:
        res = modexpo(a, n / 2, m)
        return (res % m * res % m) % m
    else:
        res = modexpo(a, n / 2, m)
        return a * res * res % m



check = True

prime=[]
prime.append(2)
def prime_List():
  L=[]
  L.append(2)
  for i in range(3,1000):
    check=True
    for  j in L:
        if not (i%j):
            check=False
    if check:
        L.append(i)
  return L

prime=prime_List()


def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1


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






print('Client Server...')
time.sleep(1)
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
#get information to connect with the server
print(shost, '({})'.format(ip))
server_host = input('Enter server\'s IP address:')
name = input('Enter Client\'s name: ')
port = 1234
print('Trying to connect to the server: {}, ({})'.format(server_host, port))
time.sleep(1)
soc.connect((server_host, port))
print("Connected...\n")
soc.send(name.encode())
time.sleep(3)
soc.send(str(n).encode())
time.sleep(3)
soc.send(str(e).encode())
print('CLIENT:')
print("e: "+str(e)+" n: "+str(n)+" d: "+str(d))

server_name = soc.recv(1024)
server_name = server_name.decode()

n_server = soc.recv(1024)
e_server = soc.recv(1024)

n_server = int(n_server.decode())
e_server = int(e_server.decode())
print("##############################################")
print('SERVER:')
print(server_name+":  e="+str(e_server)+" n="+str(n_server))
print("##############################################")
print('{} has joined...'.format(server_name))
print('Enter [bye] to exit.')
while True:
   
   while 1:
      dataR = soc.recv(1024)
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
   message = input(str("Me > "))
   if message == "[bye]":
      message = "Leaving the Chat room"
      soc.send(message.encode())
      print("\n")
      break

   dataE=[]
   for i in range(0,len(message)):
        #C = modexpo(ord(message[i]), e_server, n_server)
        C=(ord(message[i])**e_server)%n_server
        dataE.append(C)
   print(dataE)
   dataS=pickle.dumps(dataE)
   soc.send(dataS)

      
   #soc.send(message.encode())
