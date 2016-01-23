import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'https://api2.scaledrone.com'

class ScaleDrone:

    def __init__(self, channel_id, secret_key, base_url=BASE_URL):
        auth = HTTPBasicAuth(channel_id, secret_key)
        self.auth = auth
        self.base_url = base_url + '/' + channel_id + '/'

    def publish(self, room, data = {}):
        url = self.base_url + room + '/publish'
        return requests.post(url, data=data, auth=self.auth)

    def channel_stats(self):
        url = self.base_url + 'stats'
        return requests.get(url, auth=self.auth)

    def users_list(self):
        url = self.base_url + 'users'
        return requests.get(url, auth=self.auth)
