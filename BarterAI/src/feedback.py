```python
from database import DatabaseConnection

class Feedback:
    def __init__(self):
        self.db = DatabaseConnection()

    def create_feedback(self, feedback_data):
        """
        Create a new feedback entry in the database.
        """
        feedback_id = self.db.insert('feedback', feedback_data)
        return feedback_id

    def get_feedback(self, feedback_id):
        """
        Retrieve a feedback entry from the database.
        """
        feedback_data = self.db.select('feedback', {'feedback_id': feedback_id})
        return feedback_data

    def update_feedback(self, feedback_id, updated_data):
        """
        Update a feedback entry in the database.
        """
        self.db.update('feedback', {'feedback_id': feedback_id}, updated_data)

    def delete_feedback(self, feedback_id):
        """
        Delete a feedback entry from the database.
        """
        self.db.delete('feedback', {'feedback_id': feedback_id})

    def get_feedback_for_trade(self, trade_id):
        """
        Retrieve all feedback entries for a specific trade.
        """
        feedback_data = self.db.select('feedback', {'trade_id': trade_id})
        return feedback_data

    def get_feedback_for_user(self, user_id):
        """
        Retrieve all feedback entries for a specific user.
        """
        feedback_data = self.db.select('feedback', {'user_id': user_id})
        return feedback_data
```