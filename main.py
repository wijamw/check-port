import socket

def check_port(hostname, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(3)
        # Attempt to connect to the specified host and port
        result = sock.connect_ex((hostname, port))
        # Check if the port is open
        if result == 0:
            print(f"Port {port} is open on {hostname}.")
        else:
            print(f"Port {port} is closed on {hostname}.")
        # Close the socket
        sock.close()
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'example.com' with the hostname you want to check
hostname = 'surabaya.go.id'
port = 443  # Port to check

check_port(hostname, port)
