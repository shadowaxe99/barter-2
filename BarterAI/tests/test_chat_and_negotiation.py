```python
import unittest
from BarterAI.src.trade_interface import chat_and_negotiation
from BarterAI.src.user import User
from BarterAI.src.database import Database

class TestChatAndNegotiation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = Database()
        cls.user1 = User("user1", "user1@email.com", "password1", cls.db)
        cls.user2 = User("user2", "user2@email.com", "password2", cls.db)
        cls.chat = chat_and_negotiation.Chat(cls.user1, cls.user2)

    def test_send_message(self):
        self.chat.send_message(self.user1, "Hello, user2!")
        self.assertEqual(self.chat.messages[-1], ("user1", "Hello, user2!"))

    def test_receive_message(self):
        self.chat.send_message(self.user2, "Hello, user1!")
        self.assertEqual(self.chat.receive_message(self.user1), ("user2", "Hello, user1!"))

    def test_delete_message(self):
        self.chat.send_message(self.user1, "This message will be deleted.")
        self.chat.delete_message(self.user1, 0)
        self.assertNotIn(("user1", "This message will be deleted."), self.chat.messages)

    @classmethod
    def tearDownClass(cls):
        cls.db.delete_user(cls.user1)
        cls.db.delete_user(cls.user2)

if __name__ == '__main__':
    unittest.main()
```