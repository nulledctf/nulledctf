import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format( "PORT SCANNER" )
print(ascii_banner)
print("                                              author : nulled.ctf")
print("")
targetip = input(str("Targets IP: "))

#banner
print("_" * 50)
print("Scanning target: " + targetip)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

try:
    
    #this will scan every port on the ip
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        
        #returns open ports
        result = s.connect_ex((targetip,port))
        if result == 0:       #if no ports are open
            print("[*] Port {} is open".format(port))
        s.close()
        
except KeyboardInterrupt:
    print("\n Exiting :(")
    sys.exit()

except socket.error:
    print("\ Host not responding :(")
    sys.exit()
