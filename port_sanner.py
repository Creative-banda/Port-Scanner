import pyfiglet
from termcolor import colored
import socket
import threading

lenght = 5

header = pyfiglet.figlet_format("Port Scanner")

print("-"*70)

print(colored(header,color="green"))
print("-"*70)

target = input("Enter Your Target : ")
port = eval(input("Enter Port in a List : "))
def port_scan(port):
    s = socket.socket()
    s.settimeout(1)
    conn = s.connect_ex((target,port))
    if not(conn):
        print(f"Port {port} is open ")
    s.close()

for port in range(port[0],port[1]+1):
    t1 = threading.Thread(target=port_scan, args=(port,))
    t1.start()

