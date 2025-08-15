import socket
import threading

your_ip = "0.0.0.0" 
your_port = int(input("Your Port (e.g., 5001): "))

peer_ip = input("Node IP (e.g., 127.0.0.1): ").strip()
peer_port = int(input("Node Port (e.g., 5002): "))
peer_name = input("Node Name (Ex : Manju): ").strip()

#Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((your_ip, your_port))

def receive_messages():
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            label = f"{peer_name}" if (addr[0] == peer_ip and addr[1] == peer_port) else f"{addr[0]}:{addr[1]}"
            print(f"\n[{label}] > {data.decode()}")
        except Exception as e:
            print(f"[!] Error receiving: {e}")
            break

def send_messages():
    while True:
        msg = input("> ")
        sock.sendto(msg.encode(), (peer_ip, peer_port))

threading.Thread(target=receive_messages, daemon=True).start()
send_messages()
