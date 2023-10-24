```python
import unittest
from BarterAI.src.feedback_and_rating import FeedbackAndRating
from BarterAI.src.user import User
from BarterAI.src.trade import Trade

class TestFeedbackAndRating(unittest.TestCase):

    def setUp(self):
        self.user1 = User("user1", "user1@email.com")
        self.user2 = User("user2", "user2@email.com")
        self.trade = Trade(self.user1, self.user2, "item1", "item2")
        self.feedback_and_rating = FeedbackAndRating()

    def test_leave_feedback(self):
        feedback = "Great trade!"
        rating = 5
        self.feedback_and_rating.leave_feedback(self.user1, self.trade, feedback, rating)
        self.assertEqual(self.feedback_and_rating.feedback, feedback)
        self.assertEqual(self.feedback_and_rating.rating, rating)

    def test_get_feedback(self):
        feedback = "Great trade!"
        rating = 5
        self.feedback_and_rating.leave_feedback(self.user1, self.trade, feedback, rating)
        feedback_data = self.feedback_and_rating.get_feedback(self.trade)
        self.assertEqual(feedback_data['feedback'], feedback)
        self.assertEqual(feedback_data['rating'], rating)

    def test_get_user_rating(self):
        feedback1 = "Great trade!"
        rating1 = 5
        self.feedback_and_rating.leave_feedback(self.user1, self.trade, feedback1, rating1)
        feedback2 = "Good trade!"
        rating2 = 4
        self.feedback_and_rating.leave_feedback(self.user2, self.trade, feedback2, rating2)
        user_rating = self.feedback_and_rating.get_user_rating(self.user1)
        self.assertEqual(user_rating, (rating1 + rating2) / 2)

if __name__ == '__main__':
    unittest.main()
```