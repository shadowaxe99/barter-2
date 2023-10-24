```python
from database import Database

class Wishlist:
    def __init__(self, user_id):
        self.user_id = user_id
        self.db = Database()

    def get_wishlist(self):
        query = "SELECT * FROM wishlist WHERE user_id = %s"
        params = (self.user_id,)
        return self.db.query(query, params)

    def add_to_wishlist(self, item_id):
        query = "INSERT INTO wishlist (user_id, item_id) VALUES (%s, %s)"
        params = (self.user_id, item_id)
        self.db.execute(query, params)

    def remove_from_wishlist(self, item_id):
        query = "DELETE FROM wishlist WHERE user_id = %s AND item_id = %s"
        params = (self.user_id, item_id)
        self.db.execute(query, params)

    def is_in_wishlist(self, item_id):
        query = "SELECT * FROM wishlist WHERE user_id = %s AND item_id = %s"
        params = (self.user_id, item_id)
        result = self.db.query(query, params)
        return len(result) > 0
```