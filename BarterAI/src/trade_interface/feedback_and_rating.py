```python
from database import Database
from feedback import Feedback

class FeedbackAndRating:
    def __init__(self):
        self.db = Database()

    def leave_feedback(self, user_id, trade_id, rating, comments):
        feedback = Feedback(user_id, trade_id, rating, comments)
        self.db.save_feedback(feedback)

    def get_feedback(self, trade_id):
        feedback = self.db.get_feedback(trade_id)
        return feedback

    def get_user_rating(self, user_id):
        feedbacks = self.db.get_user_feedbacks(user_id)
        if feedbacks:
            total_rating = sum([feedback.rating for feedback in feedbacks])
            average_rating = total_rating / len(feedbacks)
            return average_rating
        else:
            return None
```