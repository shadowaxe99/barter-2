```python
import datetime
from ..database import Database
from ..user import User
from ..trade import Trade

class TradeConfirmation:
    def __init__(self):
        self.db = Database()

    def confirm_trade(self, trade_id, user_id):
        trade = self.db.get_trade(trade_id)
        if not trade:
            return "Trade not found."

        if trade.user_id_1 != user_id and trade.user_id_2 != user_id:
            return "User not involved in the trade."

        if trade.status != "pending":
            return "Trade not in pending status."

        if trade.user_id_1 == user_id:
            trade.user_1_confirmed = True
        else:
            trade.user_2_confirmed = True

        if trade.user_1_confirmed and trade.user_2_confirmed:
            trade.status = "confirmed"
            trade.confirmation_date = datetime.datetime.now()

        self.db.update_trade(trade)

        return "Trade confirmed."

    def cancel_trade(self, trade_id, user_id):
        trade = self.db.get_trade(trade_id)
        if not trade:
            return "Trade not found."

        if trade.user_id_1 != user_id and trade.user_id_2 != user_id:
            return "User not involved in the trade."

        if trade.status != "pending":
            return "Trade not in pending status."

        trade.status = "cancelled"
        self.db.update_trade(trade)

        return "Trade cancelled."
```