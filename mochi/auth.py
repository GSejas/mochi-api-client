class Auth:
    class Token:
        def __init__(self, api_key):
            self.api_key = api_key

        def get_headers(self):
            from base64 import b64encode

            encoded_credentials = b64encode(bytes(f"{self.api_key}:", "utf-8")).decode(
                "utf-8"
            )
            return {
                "Authorization": f"Basic {encoded_credentials}",
                "Content-Type": "application/json",
            }
