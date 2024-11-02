import socket
from models.response import response

new_line = "\r\n"

# Define server address and port
server_address = ("localhost", 8080)

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print(f"Server is listening on {server_address}")

try:
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} has been established.")

        # split request into lines
        request = client_socket.recv(1024).decode().split(new_line)

        # parse request line
        method, url, version = request.pop(0).split(" ")

        # parse headers
        headers = {}
        for index, element in enumerate(request):
            if (element == ""):
                break;
            entry = element.split(" ")
            headers[entry[0]] = entry[1]
        
        if url:
            match url:
                case "/":
                    file = open("./www/index.html")
                    content = file.read()
                    length = len(content)
                    file.close()                
                    
                    server_response = response("HTTP/1.1", "200", "OK", content)
                    server_response.headers["Content-Type:"] = "text/html; charset=UTF-8"
                    server_response.headers["Connection:"] = "close"
                    server_response.headers["Content-Length:"] = str(length)

                    client_socket.sendall(server_response.encoded())
                case _:
                    file = open("./www/not-found.html")
                    content = file.read()
                    length = len(content)
                    file.close()                

                    server_response = response("HTTP/1.1", "404", "Not Found", content)
                    server_response.headers["Content-Type:"] = "text/html; charset=UTF-8"
                    server_response.headers["Connection:"] = "close"
                    server_response.headers["Content-Length:"] = str(length)

                    client_socket.sendall(server_response.encoded())
            client_socket.close()
except KeyboardInterrupt:
    print("\nGracefully shutting down the server...")
    client_socket.close()
    server_socket.close()
finally:
    client_socket.close()
    server_socket.close()
    print("Server has been shut down.")
