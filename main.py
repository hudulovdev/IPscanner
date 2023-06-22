import socket

def scan_ip(ip_address, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout value for the socket connection

        # Attempt to connect to the IP address and port
        result = sock.connect_ex((ip_address, port))

        if result == 0:
            print(f"Port {port} on {ip_address} is open")
        else:
            print(f"Port {port} on {ip_address} is closed")

        sock.close()

    except socket.error:
        print("An error occurred while scanning the IP address and port.")

# Example usage
ip_address = str(input("Enter IP: "))
port = int(input("Enter port: "))

scan_ip(ip_address, port)
