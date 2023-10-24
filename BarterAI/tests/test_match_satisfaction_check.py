```python
import unittest
from BarterAI.src.ai_feedback_mechanism.match_satisfaction_check import MatchSatisfactionCheck
from BarterAI.src.user import User
from BarterAI.src.trade import Trade
from BarterAI.src.feedback import Feedback

class TestMatchSatisfactionCheck(unittest.TestCase):

    def setUp(self):
        self.user1 = User("user1", "user1@email.com")
        self.user2 = User("user2", "user2@email.com")
        self.trade = Trade(self.user1, self.user2, "item1", "item2")
        self.feedback = Feedback(self.user1, self.trade, 5, "Great trade!")
        self.match_satisfaction_check = MatchSatisfactionCheck()

    def test_check_satisfaction(self):
        self.match_satisfaction_check.check_satisfaction(self.feedback)
        self.assertEqual(self.match_satisfaction_check.satisfaction_score, 5)

    def test_update_satisfaction_score(self):
        self.match_satisfaction_check.update_satisfaction_score(self.feedback)
        self.assertEqual(self.match_satisfaction_check.satisfaction_score, 5)

    def test_get_satisfaction_score(self):
        self.match_satisfaction_check.satisfaction_score = 5
        self.assertEqual(self.match_satisfaction_check.get_satisfaction_score(), 5)

if __name__ == '__main__':
    unittest.main()
```