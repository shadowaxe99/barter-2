```python
import unittest
from BarterAI.src.user import User
from BarterAI.src.database import Database

class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = Database()
        cls.user = User(cls.db)

    def test_register_user(self):
        user_data = {
            "username": "test_user",
            "email": "test_user@example.com",
            "password": "test_password"
        }
        result = self.user.register_user(user_data)
        self.assertEqual(result, True)

    def test_login_user(self):
        user_data = {
            "username": "test_user",
            "password": "test_password"
        }
        result = self.user.login_user(user_data)
        self.assertEqual(result, True)

    def test_upload_item(self):
        item_data = {
            "user_id": 1,
            "description": "Test item",
            "photos": ["test_photo.jpg"],
            "desired_exchanges": ["Another item"]
        }
        result = self.user.upload_item(item_data)
        self.assertEqual(result, True)

    def test_view_trade_history(self):
        user_id = 1
        result = self.user.view_trade_history(user_id)
        self.assertIsInstance(result, list)

    def test_create_wishlist(self):
        wishlist_data = {
            "user_id": 1,
            "items": ["Test item 1", "Test item 2"]
        }
        result = self.user.create_wishlist(wishlist_data)
        self.assertEqual(result, True)

    @classmethod
    def tearDownClass(cls):
        cls.db.close_connection()

if __name__ == '__main__':
    unittest.main()
```