# FORMAT OF HTML REQUEST
# method sp url sp version crlf
# header field name: sp value sp crlf
# ...headers crlf
# crlf
# body
class Request:
    def __init__(self, message):
        self.message = self.__parse_http_request(message)

    def __parse_http_request(self, message):
        """Parse an HTTP request string into its components."""
        # Initialize the response dictionary
        parsed_request = {
            'method': '',
            'path': '',
            'protocol': '',
            'headers': {},
            'query_params': {},
            'body': ''
        }
        
        try:
            # Split headers and body
            request_parts = message.split('\r\n\r\n', 1)
            headers_part = request_parts[0]
            
            # Get body if it exists
            if len(request_parts) > 1:
                parsed_request['body'] = request_parts[1]
            
            # Split headers into lines
            header_lines = headers_part.split('\r\n')
            
            # Parse request line
            if header_lines[0]:
                request_line = header_lines[0].split(' ')
                if len(request_line) >= 3:
                    parsed_request['method'] = request_line[0]
                    
                    # Handle query parameters in path
                    path_parts = request_line[1].split('?', 1)
                    parsed_request['path'] = path_parts[0]
                    
                    if len(path_parts) > 1:
                        query_string = path_parts[1]
                        query_params = {}
                        for param in query_string.split('&'):
                            if '=' in param:
                                key, value = param.split('=', 1)
                                query_params[key] = value
                        parsed_request['query_params'] = query_params
                    
                    parsed_request['protocol'] = request_line[2]
            
            # Parse headers
            for line in header_lines[1:]:
                if ': ' in line:
                    key, value = line.split(': ', 1)
                    parsed_request['headers'][key.lower()] = value
                    
            return parsed_request
        
        except Exception as e:
            raise ValueError(f"Failed to parse HTTP request: {str(e)}")
