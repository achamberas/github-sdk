import requests
import json
import pandas as pd
from requests.auth import HTTPBasicAuth

class github_sdk:
    def __init__(self, user, token):
        self.user = user
        self.token = token
        self.s = requests.Session()
        url = "https://api.github.com/user"
        self.s.request("GET", url, auth=HTTPBasicAuth(user, token))
        
    def list_repos(self):
        url = "https://api.github.com/user/repos"
        response = self.s.request("GET", url, auth=HTTPBasicAuth(self.user, self.token))
        response_json = json.loads(response.text)
        self.message = "The list of repos is:"
        self.type = 'list'
        self.result = pd.DataFrame.from_dict(response_json)[['name', 'url']]
        return self._repr_html_()
        
    def list_orgs(self):
        url = "https://api.github.com/user/orgs"
        response = self.s.request("GET", url, auth=HTTPBasicAuth(self.user, self.token))
        response_json = json.loads(response.text)
        self.message = "The list of orgs is:"
        self.type = 'list'
        self.result = pd.DataFrame.from_dict(response_json)[['login', 'url']]
        return self._repr_html_()

    def count_repos(self):
        url = "https://api.github.com/user/repos"
        response = self.s.request("GET", url, auth=HTTPBasicAuth(self.user, self.token))
        response_json = json.loads(response.text)
        self.message = "The number of repos is:"
        self.type = 'number'
        self.result = pd.DataFrame.from_dict(response_json)['id'].count()
        return self._repr_html_()
        
    def count_orgs(self):
        url = "https://api.github.com/user/orgs"
        response = self.s.request("GET", url, auth=HTTPBasicAuth(self.user, self.token))
        response_json = json.loads(response.text)
        self.message = "The number of orgs is:"
        self.type = 'number'
        self.result = pd.DataFrame.from_dict(response_json)['id'].count()
        return self.result
    
    def _repr_html_(self):
        if self.type == 'list':
            obj = self.result._repr_html_()
        else:
            obj = '<h1>' + str(self.result) + '</h1>'
        return (
            '<h3>' + self.message + '</h3>'
            f'{obj}<br>\n'
        )
