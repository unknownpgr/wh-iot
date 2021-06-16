# Import required libriries

# Library for hardware bridge communication
from bridgeclient import BridgeClient as bridgeclient

# Library for system control
import sys

# Library for socket communication
from socket import *

# Enable bridge
sys.path.insert(0, '/usr/lib/python2.7/bridge/')

# Create bridge and open
client = bridgeclient()
client.begin()

# Create socket for communication
s = socket(AF_INET, SOCK_STREAM)

# Open server for data fetching
s.bind(("0.0.0.0", 8080))

# Accept up to 100 connection.
s.listen(100)

# If client(laptop) accesses to arduino, return data.
while True:
    # Wait until client connects
    conn, addr = s.accept()

    # Read data from bridge
    val = client.get('TH_DATA')

    # Print log
    print str(addr) + "connected and got data" + str(val)

    # Send read data to socket
    conn.send(val)
