"""
    Filename: auth.py
    Description: A class used for handling authentication.
    Author: Jorge Sequeira <jsequeira03@gmail.com>
    Date Created: November 16, 2024
    Version: 0.1.1
    Last Modified: November 16, 2024 by Jorge Sequeira
    License: MIT License
    Dependencies:
        - base64 (standard library)
    Examples:
        # Example usage of the Auth class
        from mochi.auth import Auth

        auth = Auth.Token(api_key="your_api_key")
        headers = auth.get_headers()
        print(headers)
    History log:
        - Version 0.1.1: Initial version created on November 16, 2024 by Jorge Sequeira
"""


class Auth:
    """
    A class used for handling authentication.
    ...
    Nested Classes
    --------------
    Token
        A nested class used for handling token-based authentication.
    """
    class Token:
        """
        Constructs all the necessary attributes for the Token object.
        Parameters
        ----------
        api_key : str
            The API key used for authentication.
        """
        
        def __init__(self, api_key):
            """
            Initializes the authentication with the provided API key.

            Args:
                api_key (str): The API key to be used for authentication.
            """
            self.api_key = api_key

        def get_headers(self):
            """
            Generates the headers required for authentication.
            This method encodes the API key using Base64 encoding and constructs
            the headers needed for making authenticated requests to the API.
            Returns:
                dict: A dictionary containing the 'Authorization' and 'Content-Type' headers.
            """
            from base64 import b64encode

            encoded_credentials = b64encode(bytes(f"{self.api_key}:", "utf-8")).decode(
                "utf-8"
            )
            return {
                "Authorization": f"Basic {encoded_credentials}",
                "Content-Type": "application/json",
            }
