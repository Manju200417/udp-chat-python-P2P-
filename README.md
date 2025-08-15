# udp-chat-python-P2P-
A simple Python-based UDP peer-to-peer chat application using sockets and threading. Supports real-time messaging over LAN or internet (with port forwarding).




##  Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Manju200417/udp-chat-python-P2P
   
   cd udp-chat-python-P2P

2. Run the Python file:
    ```bash
   python node-1.py
    
## Usage

# Example: 

Two devices on the same network

Let’s say:

Device 1 will use Port 5001  
Device 2 will use Port 5002  

## in Device 1 :
1. Your Port (e.g., 5001): 5001  
2. Node IP (e.g., 127.0.0.1): 192.168.1.20  
3. Node Port (e.g., 5002): 5002  
4. Node Name (Ex : Manju): Friend  

## in Device 2 :  
1. Your Port (e.g., 5001): 5002  
2. Node IP (e.g., 127.0.0.1): 192.168.1.10  
3. Node Port (e.g., 5002): 5001  
4. Node Name (Ex : Manju): You  

# Notes  
  - Both devices must allow the chosen ports in their firewall.  
  - For internet chatting, set up port forwarding on your router and use your public IP.  
  - UDP is connectionless — some messages might be lost if the network is unstable.  
