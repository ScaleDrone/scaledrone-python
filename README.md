# ScaleDrone Python
Official ScaleDrone Python pushing library. This is a wrapper around the REST API.

##Installation

```
pip install scaledrone
```

##Usage
Create a new instance of ScaleDrone passing it the `channelId` and `secretKey` that you can find from the channel's page
```python
from scaledrone import ScaleDrone

drone = ScaleDrone('channel_id', 'secret_key')
```

Publishing a message
```python
room = 'notifications'
message = {'foo': 'bar'}
response = drone.publish(room, message)
```

Channel stats
```python
response = drone.channel_stats()
```

Connected users list
```python
response = drone.users_list()
```
