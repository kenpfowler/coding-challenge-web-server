# FORMAT OF HTML RESPONSE
# version sp status_code sp phrase crlf
# header field name: sp value sp crlf
# ...headers crlf
# crlf
# body

new_line = "\r\n"

class response:
    def __init__(self, version, status_code, phrase, body):
        self.version = version
        self.status_code = status_code
        self.phrase = phrase
        self.headers = {}
        self.body = body


    def encoded(self):
        headers = "".join(f"{key} {value}\r\n" for key, value in self.headers.items())
        return (f"{self.version} {self.status_code} {self.phrase}{new_line}" + headers + new_line + self.body).encode()