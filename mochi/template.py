class Templates:
    def __init__(self, session, base_url="https://app.mochi.cards/api/"):
        self.session = session
        self.base_url = f"{base_url}templates/"

    def get_template(self, template_id):
        response = self.session.get(f"{self.base_url}{template_id}")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def list_templates(self):
        response = self.session.get(self.base_url)
        if response.status_code == 200:
            return response.json()["docs"]
        else:
            response.raise_for_status()
