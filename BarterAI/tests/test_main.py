```python
import unittest
from BarterAI.src.main import app
from BarterAI.src.user import User
from BarterAI.src.item import Item
from BarterAI.src.trade import Trade
from BarterAI.src.database import Database

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = Database()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_user_registration(self):
        user = User("test_user", "test_user@email.com", "password")
        self.db.add_user(user)
        self.assertIn(user, self.db.get_all_users())

    def test_item_upload(self):
        user = User("test_user", "test_user@email.com", "password")
        item = Item("test_item", "test_description", user.user_id)
        self.db.add_item(item)
        self.assertIn(item, self.db.get_all_items())

    def test_trade_confirmation(self):
        user1 = User("test_user1", "test_user1@email.com", "password")
        user2 = User("test_user2", "test_user2@email.com", "password")
        item1 = Item("test_item1", "test_description1", user1.user_id)
        item2 = Item("test_item2", "test_description2", user2.user_id)
        trade = Trade(user1.user_id, user2.user_id, item1.item_id, item2.item_id)
        self.db.add_trade(trade)
        self.assertIn(trade, self.db.get_all_trades())

    def tearDown(self):
        self.db.clear_database()

if __name__ == "__main__":
    unittest.main()
```