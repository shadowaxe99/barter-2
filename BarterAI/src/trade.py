```python
from datetime import datetime
from database import Database

class Trade:
    def __init__(self, trade_id, user_id_1, user_id_2, item_id_1, item_id_2, status):
        self.trade_id = trade_id
        self.user_id_1 = user_id_1
        self.user_id_2 = user_id_2
        self.item_id_1 = item_id_1
        self.item_id_2 = item_id_2
        self.status = status
        self.created_at = datetime.now()

    def save_to_db(self):
        Database.insert(collection='trades', data=self.json())

    def json(self):
        return {
            'trade_id': self.trade_id,
            'user_id_1': self.user_id_1,
            'user_id_2': self.user_id_2,
            'item_id_1': self.item_id_1,
            'item_id_2': self.item_id_2,
            'status': self.status,
            'created_at': self.created_at
        }

    @classmethod
    def find_by_trade_id(cls, trade_id):
        trade_data = Database.find_one(collection='trades', query={'trade_id': trade_id})
        return cls(**trade_data) if trade_data else None

    @classmethod
    def find_by_user_id(cls, user_id):
        trades = Database.find(collection='trades', query={'$or': [{'user_id_1': user_id}, {'user_id_2': user_id}]})
        return [cls(**trade) for trade in trades]

    def update_status(self, status):
        self.status = status
        Database.update(collection='trades', query={'trade_id': self.trade_id}, data={'status': status})
```