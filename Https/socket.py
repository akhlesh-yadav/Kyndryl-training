import socket

# Secure server socket configuration example
HOST = '127.0.0.1'  # Localhost binding (prevents exposure to external networks)
PORT = 65432        # Non-privileged port

def start_server():
    # Enforce safe socket creation and options
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"Server listening on {HOST}:{PORT}...")
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                # Set a socket timeout to prevent Slowloris / hung connection attacks
                conn.settimeout(10.0) 
                
                try:
                    # Enforce strict maximum payload byte limits
                    data = conn.recv(1024) 
                    if not data:
                        break
                    
                    # Sanitize/validate incoming bytes before processing
                    message = data.decode('utf-8', errors='replace').strip()
                    response = f"Echo: {message}"
                    conn.sendall(response.encode('utf-8'))
                    
                except socket.timeout:
                    print(f"Connection timed out for {addr}")
                except Exception as e:
                    print(f"Error handling request: {e}")

if __name__ == "__main__":
    start_server()