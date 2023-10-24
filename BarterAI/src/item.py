```python
from database import Database

class Item:
    def __init__(self, item_id, user_id, description, photos, desired_exchanges):
        self.item_id = item_id
        self.user_id = user_id
        self.description = description
        self.photos = photos
        self.desired_exchanges = desired_exchanges

    def save_to_db(self):
        Database.insert(collection='items', data=self.json())

    def json(self):
        return {
            'item_id': self.item_id,
            'user_id': self.user_id,
            'description': self.description,
            'photos': self.photos,
            'desired_exchanges': self.desired_exchanges
        }

    @classmethod
    def find_by_item_id(cls, item_id):
        item_data = Database.find_one(collection='items', query={'item_id': item_id})
        if item_data:
            return cls(**item_data)

    @classmethod
    def find_by_user_id(cls, user_id):
        items = Database.find(collection='items', query={'user_id': user_id})
        return [cls(**item) for item in items]
```