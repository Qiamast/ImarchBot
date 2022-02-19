class CSEAPIError(Exception):
    """Base exception class for CSE API errors."""

    def __init__(self, message: str, status_code: int) -> None:
        self.message = message
        self.status_code = status_code


class AuthError(CSEAPIError):
    """Exception class for authentication errors."""

    def __init__(self, message: str, status_code: int = 401) -> None:
        super().__init__(message, status_code)
