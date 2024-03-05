class Templates:
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
