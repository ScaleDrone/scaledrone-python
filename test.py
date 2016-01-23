import unittest
from scaledrone import ScaleDrone

drone = ScaleDrone('G3TYvCzoXtrIuEtQ', 'M7Oc1DY2FgkCaUh4aQFC3TRV1R3RThPd')

class Test(unittest.TestCase):

    def test_publish(self):
        r = drone.publish('notifications', {'foo': 'bar'})
        self.assertEqual(r.status_code, 200)

    def test_publish(self):
        r = drone.channel_stats()
        self.assertTrue('users_count' in r.json())
        self.assertEqual(r.status_code, 200)

    def users_list(self):
        r = drone.users_list()
        self.assertTrue('users' in r.json())
        self.assertEqual(r.status_code, 200)
