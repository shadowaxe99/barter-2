```python
from database import Database
from feedback import Feedback

class MatchSatisfactionCheck:
    def __init__(self):
        self.db = Database()

    def get_unchecked_feedbacks(self):
        unchecked_feedbacks = self.db.get_feedbacks(status='unchecked')
        return unchecked_feedbacks

    def check_satisfaction(self, feedback_id):
        feedback = self.db.get_feedback(feedback_id)
        if feedback.rating >= 4:
            return True
        else:
            return False

    def update_feedback_status(self, feedback_id, status):
        self.db.update_feedback(feedback_id, status)

    def run_satisfaction_check(self):
        unchecked_feedbacks = self.get_unchecked_feedbacks()
        for feedback in unchecked_feedbacks:
            if self.check_satisfaction(feedback.feedback_id):
                self.update_feedback_status(feedback.feedback_id, 'satisfactory')
            else:
                self.update_feedback_status(feedback.feedback_id, 'unsatisfactory')

if __name__ == "__main__":
    match_satisfaction_check = MatchSatisfactionCheck()
    match_satisfaction_check.run_satisfaction_check()
```