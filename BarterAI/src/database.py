```python
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class Database:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['BarterAI']

    def insert_user(self, user_data):
        users = self.db.users
        user_id = users.insert_one(user_data).inserted_id
        return user_id

    def get_user(self, user_id):
        users = self.db.users
        user_data = users.find_one({'_id': ObjectId(user_id)})
        return user_data

    def update_user(self, user_id, user_data):
        users = self.db.users
        users.update_one({'_id': ObjectId(user_id)}, {"$set": user_data}, upsert=False)

    def delete_user(self, user_id):
        users = self.db.users
        users.delete_one({'_id': ObjectId(user_id)})

    def insert_item(self, item_data):
        items = self.db.items
        item_id = items.insert_one(item_data).inserted_id
        return item_id

    def get_item(self, item_id):
        items = self.db.items
        item_data = items.find_one({'_id': ObjectId(item_id)})
        return item_data

    def update_item(self, item_id, item_data):
        items = self.db.items
        items.update_one({'_id': ObjectId(item_id)}, {"$set": item_data}, upsert=False)

    def delete_item(self, item_id):
        items = self.db.items
        items.delete_one({'_id': ObjectId(item_id)})

    def insert_trade(self, trade_data):
        trades = self.db.trades
        trade_id = trades.insert_one(trade_data).inserted_id
        return trade_id

    def get_trade(self, trade_id):
        trades = self.db.trades
        trade_data = trades.find_one({'_id': ObjectId(trade_id)})
        return trade_data

    def update_trade(self, trade_id, trade_data):
        trades = self.db.trades
        trades.update_one({'_id': ObjectId(trade_id)}, {"$set": trade_data}, upsert=False)

    def delete_trade(self, trade_id):
        trades = self.db.trades
        trades.delete_one({'_id': ObjectId(trade_id)})

    def insert_feedback(self, feedback_data):
        feedbacks = self.db.feedbacks
        feedback_id = feedbacks.insert_one(feedback_data).inserted_id
        return feedback_id

    def get_feedback(self, feedback_id):
        feedbacks = self.db.feedbacks
        feedback_data = feedbacks.find_one({'_id': ObjectId(feedback_id)})
        return feedback_data

    def update_feedback(self, feedback_id, feedback_data):
        feedbacks = self.db.feedbacks
        feedbacks.update_one({'_id': ObjectId(feedback_id)}, {"$set": feedback_data}, upsert=False)

    def delete_feedback(self, feedback_id):
        feedbacks = self.db.feedbacks
        feedbacks.delete_one({'_id': ObjectId(feedback_id)})
```