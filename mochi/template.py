"""
    Filename: template.py
    Description: A client for interacting with the Templates API.
    Author: Jorge Sequeira <jsequeira03@gmail.com>
    Date Created: November 16, 2024
    Version: 0.1.1
    Last Modified: November 16, 2024 by Jorge Sequeira
    License: MIT License
    Dependencies:
        - requests (external library)
    Examples:
        # Example usage of the Templates client
        from mochi.template import Templates
        from mochi.auth import Auth

        auth = Auth(api_key="your_api_key")
        templates_client = Templates(session=requests.Session(), base_url="https://app.mochi.cards/api/")
        
        # Get a template by ID
        template = templates_client.get_template(template_id="template_id")
        print(template)
        
        # List all templates
        templates = templates_client.list_templates()
        print(templates)
    History log:
        - Version 0.1.1: Initial version created on November 16, 2024 by Jorge Sequeira
"""


class Templates:
    """
    A class to interact with the Mochi API templates endpoint.
    Attributes:
        session (requests.Session): The session object to make HTTP requests.
        base_url (str): The base URL for the Mochi API, defaults to "https://app.mochi.cards/api/templates/".
    Methods:
        get_template(template_id):
            Retrieves a specific template by its ID.
        list_templates():
            Lists all available templates.
        Initializes the Templates class with a session and an optional base URL.
        Args:
            session (requests.Session): The session object to make HTTP requests.
            base_url (str, optional): The base URL for the Mochi API, defaults to "https://app.mochi.cards/api/".
        ...
        Retrieves a specific template by its ID.
        Args:
            template_id (str): The ID of the template to retrieve.
        Returns:
            dict: The template data if the request is successful.
        Raises:
            requests.exceptions.HTTPError: If the request to the API fails.
        ...
        Lists all available templates.
        Returns:
            list: A list of templates if the request is successful.
        Raises:
            requests.exceptions.HTTPError: If the request to the API fails.
        ...
    """
    def __init__(self, session, base_url="https://app.mochi.cards/api/"):
        """_summary_

        :param session: _description_
        :type session: _type_
        :param base_url: _description_, defaults to "https://app.mochi.cards/api/"
        :type base_url: str, optional
        """
        self.session = session
        self.base_url = f"{base_url}templates/"

    def get_template(self, template_id):
        """_summary_

        :param template_id: _description_
        :type template_id: _type_
        :return: _description_
        :rtype: _type_
        """
        response = self.session.get(f"{self.base_url}{template_id}")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def list_templates(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        response = self.session.get(self.base_url)
        if response.status_code == 200:
            return response.json()["docs"]
        else:
            response.raise_for_status()
