import unittest
from scaledrone import Scaledrone

drone = Scaledrone('KtJ2qzn3CF3svSFe', 'secret')

class Test(unittest.TestCase):

    def test_publish(self):
        r = drone.publish('notifications', {'foo': 'bar'})
        self.assertEqual(r.status_code, 200)

    def test_bulk_publish(self):
        r = drone.publish(['notifications', 'room1', 'room2'], {'foo': 'bar'})
        self.assertEqual(r.status_code, 200)

    def test_channel_stats(self):
        r = drone.channel_stats()
        self.assertEqual(r.status_code, 200)
        self.assertTrue('users_count' in r.json())

    def test_members_list(self):
        r = drone.members_list()
        self.assertEqual(r.status_code, 200)
        self.assertTrue(isinstance(r.json(), list))

    def test_rooms_list(self):
        r = drone.members_list()
        self.assertEqual(r.status_code, 200)
        self.assertTrue(isinstance(r.json(), list))

    def test_room_members_list(self):
        r = drone.room_members_list('notifications')
        self.assertEqual(r.status_code, 200)
        self.assertTrue(isinstance(r.json(), list))

    def test_all_room_members_list(self):
        r = drone.all_room_members_list()
        self.assertEqual(r.status_code, 200)
        self.assertTrue(isinstance(r.json(), dict))

if __name__ == '__main__':
    unittest.main()
