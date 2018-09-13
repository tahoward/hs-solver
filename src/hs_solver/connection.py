import requests


class Connection:
    def __init__(self):
        self.session = requests.Session()

    def call(self, endpoint=None, params=None, post=False):
        if post:
            response = self.session.post(endpoint, params=params)
        else:
            response = self.session.get(endpoint, params=params)

        print("Call: {} {}".format(response.request.method, response.url))

        return response
