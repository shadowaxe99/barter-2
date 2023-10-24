```python
import unittest
from BarterAI.src.trade_interface.trade_confirmation import TradeConfirmation
from BarterAI.src.user import User
from BarterAI.src.item import Item
from BarterAI.src.trade import Trade

class TestTradeConfirmation(unittest.TestCase):

    def setUp(self):
        self.user1 = User("user1", "user1@email.com")
        self.user2 = User("user2", "user2@email.com")
        self.item1 = Item("item1", self.user1.user_id, "description1", ["photo1"], ["item2"])
        self.item2 = Item("item2", self.user2.user_id, "description2", ["photo2"], ["item1"])
        self.trade = Trade(self.user1.user_id, self.user2.user_id, self.item1.item_id, self.item2.item_id)
        self.trade_confirmation = TradeConfirmation()

    def test_confirm_trade(self):
        self.trade_confirmation.confirm_trade(self.trade)
        self.assertEqual(self.trade.status, "confirmed")

    def test_reject_trade(self):
        self.trade_confirmation.reject_trade(self.trade)
        self.assertEqual(self.trade.status, "rejected")

    def test_trade_status(self):
        self.trade_confirmation.confirm_trade(self.trade)
        status = self.trade_confirmation.get_trade_status(self.trade)
        self.assertEqual(status, "confirmed")

if __name__ == '__main__':
    unittest.main()
```