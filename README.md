# Scaledrone Python API client

Official Scaledrone Python API client. This is a wrapper around the REST API.

## Installation

```
pip install scaledrone
```

## Usage

Create a new instance of Scaledrone passing it the `channel_id` and `secret_key` that you can find from the Scaledrone dashboard channel's page.
```python
from scaledrone import Scaledrone

drone = Scaledrone('channel_id', 'secret_key')
```

### Publishing a message
```python
room = 'notifications'
message = {'foo': 'bar'}
response = drone.publish(room, message)
```

### Publishing a message to multiple rooms
```python
rooms = ['room1', 'room2']
message = {'foo': 'bar'}
response = drone.publish(rooms, message)
```

### Getting the number of users in a channel
```python
response = drone.channel_stats()
print(response.json()) # {users_count: 10}
```

### Getting the list of users from all rooms
```python
response = drone.members_list()
print(response.json()) # ["user1", "user2"]
```

### Getting the list of rooms that have users in them
```python
response = drone.rooms_list()
print(response.json()) # ["room1", "room2"]
```

### Getting the list of users in a room
```python
response = drone.test_room_members_list()
print(response.json()) # ["user3", "user4"]
```

### Getting the list of rooms and their members
```python
response = drone.all_room_members_list()
print(response.json()) # {"room1": ["user1", "user2"], "room2": ["user1"]}
```

## API Response

The API returns [Requests](http://docs.python-requests.org/en/master/) responses.

## Testing

```
python test.py
```
