```python
import unittest
from BarterAI.src.user_profile_and_listings.trade_history import TradeHistory
from BarterAI.src.database import Database
from BarterAI.src.user import User
from BarterAI.src.trade import Trade

class TestTradeHistory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = Database()
        cls.user1 = User("user1", "user1@email.com", "password1")
        cls.user2 = User("user2", "user2@email.com", "password2")
        cls.trade1 = Trade(cls.user1.user_id, cls.user2.user_id, "item1", "item2")
        cls.trade2 = Trade(cls.user2.user_id, cls.user1.user_id, "item3", "item4")

    def test_add_trade(self):
        trade_history = TradeHistory(self.user1.user_id)
        trade_history.add_trade(self.trade1.trade_id)
        self.assertIn(self.trade1.trade_id, trade_history.trades)

    def test_remove_trade(self):
        trade_history = TradeHistory(self.user1.user_id)
        trade_history.add_trade(self.trade1.trade_id)
        trade_history.remove_trade(self.trade1.trade_id)
        self.assertNotIn(self.trade1.trade_id, trade_history.trades)

    def test_get_trade(self):
        trade_history = TradeHistory(self.user1.user_id)
        trade_history.add_trade(self.trade1.trade_id)
        trade_history.add_trade(self.trade2.trade_id)
        trade = trade_history.get_trade(self.trade1.trade_id)
        self.assertEqual(trade, self.trade1)

    def test_get_all_trades(self):
        trade_history = TradeHistory(self.user1.user_id)
        trade_history.add_trade(self.trade1.trade_id)
        trade_history.add_trade(self.trade2.trade_id)
        trades = trade_history.get_all_trades()
        self.assertEqual(len(trades), 2)

    @classmethod
    def tearDownClass(cls):
        cls.db.delete_user(cls.user1.user_id)
        cls.db.delete_user(cls.user2.user_id)
        cls.db.delete_trade(cls.trade1.trade_id)
        cls.db.delete_trade(cls.trade2.trade_id)

if __name__ == '__main__':
    unittest.main()
```