```python
import datetime
from database import Database

class Chat:
    def __init__(self, user1_id, user2_id):
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.messages = []

    def add_message(self, sender_id, text):
        timestamp = datetime.datetime.now()
        message = Message(sender_id, text, timestamp)
        self.messages.append(message)

    def get_messages(self):
        return self.messages

class Message:
    def __init__(self, sender_id, text, timestamp):
        self.sender_id = sender_id
        self.text = text
        self.timestamp = timestamp

class Negotiation:
    def __init__(self, user1_id, user2_id, item1_id, item2_id):
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.item1_id = item1_id
        self.item2_id = item2_id
        self.chat = Chat(user1_id, user2_id)
        self.status = "ongoing"

    def add_message(self, sender_id, text):
        self.chat.add_message(sender_id, text)

    def get_messages(self):
        return self.chat.get_messages()

    def agree_trade(self):
        self.status = "agreed"
        Database.update_trade_status(self.user1_id, self.user2_id, self.item1_id, self.item2_id, self.status)
```
