import requests
import urllib
from requests.auth import HTTPBasicAuth

BASE_URL = 'https://api2.scaledrone.com'

class Scaledrone:

    def __init__(self, channel_id, secret_key, base_url=BASE_URL):
        auth = HTTPBasicAuth(channel_id, secret_key)
        self.auth = auth
        self.base_url = base_url + '/' + channel_id + '/'

    def publish(self, room, data = {}):
        if isinstance(room, list):
            url = self.base_url + 'publish/rooms'
            return requests.post(url, json=data, auth=self.auth, params={'r': room})
        else:
            url = self.base_url + room + '/publish'
            return requests.post(url, json=data, auth=self.auth)

    def channel_stats(self):
        url = self.base_url + 'stats'
        return requests.get(url, auth=self.auth)

    def members_list(self):
        url = self.base_url + 'members'
        return requests.get(url, auth=self.auth)

    def rooms_list(self):
        url = self.base_url + 'rooms'
        return requests.get(url, auth=self.auth)

    def room_members_list(self, room):
        url = self.base_url + room + '/members'
        return requests.get(url, auth=self.auth)

    def all_room_members_list(self):
        url = self.base_url + 'room-members'
        return requests.get(url, auth=self.auth)
