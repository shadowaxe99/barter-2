```python
import unittest
from BarterAI.src.trade import Trade
from BarterAI.src.user import User
from BarterAI.src.item import Item

class TestTrade(unittest.TestCase):

    def setUp(self):
        self.user1 = User("user1", "user1@email.com")
        self.user2 = User("user2", "user2@email.com")
        self.item1 = Item("item1", self.user1.user_id, "description1", ["photo1"], ["exchange1"])
        self.item2 = Item("item2", self.user2.user_id, "description2", ["photo2"], ["exchange2"])
        self.trade = Trade(self.user1.user_id, self.user2.user_id, self.item1.item_id, self.item2.item_id)

    def test_trade_creation(self):
        self.assertEqual(self.trade.user_id_1, self.user1.user_id)
        self.assertEqual(self.trade.user_id_2, self.user2.user_id)
        self.assertEqual(self.trade.item_id_1, self.item1.item_id)
        self.assertEqual(self.trade.item_id_2, self.item2.item_id)
        self.assertEqual(self.trade.status, "pending")

    def test_trade_confirmation(self):
        self.trade.confirm_trade()
        self.assertEqual(self.trade.status, "confirmed")

    def test_trade_cancellation(self):
        self.trade.cancel_trade()
        self.assertEqual(self.trade.status, "cancelled")

if __name__ == '__main__':
    unittest.main()
```