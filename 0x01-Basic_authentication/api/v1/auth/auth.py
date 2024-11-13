""" Modules """
from flask import request
from typing import Typevar, List

class Auth:
    """
    Auth class for handling authentication and authorization.

    Methods:
    - require_auth(path: str, excluded_paths: List[str]) -> bool: Checks if
    authentication is required for the given path.
    - authorization_header(request=None) -> str: Retrieves the
    authorization header from the request.
    - current_user(request=None) -> TypeVar('User'): Retrieves
    the current user based on the request.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required for the given path.

        Args:
        - path: Path to be checked
        - excluded_paths: Paths that have been excluded
        
        Returns:
        - True if authorization is required
        """

        pass

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.

        Args:
        - request: Request object

        Returns:
        Authorization header
        """

        pass

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on the request.

        Args:
        - request: The Request object

        Returns:
        The current user
        """

        pass

