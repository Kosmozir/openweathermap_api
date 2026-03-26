class HTTPError(Exception):
    """Base xception raised for HTTP Errors
    
    """
    def __init__(self, message, status_code):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class ApiKeyError(HTTPError):
    def __init__(self, message, status_code):
        super().__init__(message, status_code)

    def __str__(self):
        return f"{self.message} (Error Code: {self.status_code})"

class ApiBadRequestError(HTTPError):
    def __init__(self, message, status_code):
        super().__init__(message, status_code)
    
    def __str__(self):
        return f"{self.message} (Error Code: {self.status_code})"

class ApiNotFoundError(HTTPError):
    def __init__(self, message, status_code):
        super().__init__(message, status_code)
    
    def __str__(self):
        return f"{self.message} (Error Code: {self.status_code})"