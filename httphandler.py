from models.request import Request
from models.response import Response

# http message handler
# try
# parse arbitrary data sent to the server as html request
# if data cannot be parsed as an http request send 400 error
# otherwise, respond with 200 and send the index page
# or 404 and send the not found page if any path other than root is used


def http_message_handler(message) -> Response:
    try:
        request = Request(message)
        url = request.message["path"]

        match url:
            case "/":
                with open("./www/index.html") as file:
                    content = file.read()
                    length = len(content)

                    server_response = Response("HTTP/1.1", "200", "OK", content)
                    server_response.headers["Content-Type:"] = (
                        "text/html; charset=UTF-8"
                    )
                    server_response.headers["Connection:"] = "close"
                    server_response.headers["Content-Length:"] = str(length)
                    return server_response
            case "/health-check":
                    server_response = Response("HTTP/1.1", "200", "OK", "")
                    server_response.headers["Connection:"] = "close"
                    return server_response
            case _:
                with open("./www/not-found.html") as file:
                    content = file.read()
                    length = len(content)

                    server_response = Response("HTTP/1.1", "404", "Not Found", content)
                    server_response.headers["Content-Type:"] = (
                        "text/html; charset=UTF-8"
                    )
                    server_response.headers["Connection:"] = "close"
                    server_response.headers["Content-Length:"] = str(length)
                    return server_response
    except:
        server_response = Response("HTTP/1.1", "400", "Bad Request", "")
        server_response.headers["Connection:"] = "close"
        return server_response
