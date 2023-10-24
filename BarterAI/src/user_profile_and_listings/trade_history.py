```python
from database import Database

class TradeHistory:
    def __init__(self, user_id):
        self.user_id = user_id
        self.db = Database()

    def get_trade_history(self):
        """
        Fetches the trade history of the user from the database.
        """
        trade_history = self.db.get_user_trade_history(self.user_id)
        return trade_history

    def display_trade_history(self):
        """
        Displays the trade history of the user.
        """
        trade_history = self.get_trade_history()
        for trade in trade_history:
            print(f"Trade ID: {trade['trade_id']}")
            print(f"Item Traded: {trade['item_id']}")
            print(f"Trade Partner: {trade['trade_partner']}")
            print(f"Trade Date: {trade['trade_date']}")
            print(f"Trade Status: {trade['trade_status']}")
            print("-------------------------------")

    def add_trade(self, trade):
        """
        Adds a new trade to the user's trade history.
        """
        self.db.add_trade_to_history(self.user_id, trade)

    def update_trade_status(self, trade_id, status):
        """
        Updates the status of a trade in the user's trade history.
        """
        self.db.update_trade_status(self.user_id, trade_id, status)
```