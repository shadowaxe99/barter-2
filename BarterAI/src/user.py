```python
from database import DatabaseConnection

class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.trade_history = []
        self.wishlist = []
        self.db = DatabaseConnection()

    def register(self, password):
        hashed_password = self.hash_password(password)
        self.db.insert('users', {'user_id': self.user_id, 'username': self.username, 'email': self.email, 'password': hashed_password})

    def login(self, password):
        user = self.db.query('users', {'user_id': self.user_id})
        if user and self.verify_password(password, user['password']):
            return True
        return False

    def hash_password(self, password):
        # Implement password hashing here
        pass

    def verify_password(self, password, hashed_password):
        # Implement password verification here
        pass

    def add_to_wishlist(self, item_id):
        self.wishlist.append(item_id)
        self.db.update('users', {'user_id': self.user_id}, {'wishlist': self.wishlist})

    def remove_from_wishlist(self, item_id):
        self.wishlist.remove(item_id)
        self.db.update('users', {'user_id': self.user_id}, {'wishlist': self.wishlist})

    def add_to_trade_history(self, trade_id):
        self.trade_history.append(trade_id)
        self.db.update('users', {'user_id': self.user_id}, {'trade_history': self.trade_history})

    def get_trade_history(self):
        return self.trade_history

    def get_wishlist(self):
        return self.wishlist
```