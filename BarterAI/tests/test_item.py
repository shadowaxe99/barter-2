```python
import unittest
from BarterAI.src.item import Item

class TestItem(unittest.TestCase):

    def setUp(self):
        self.item = Item("1", "2", "A rare book", ["photo1.jpg", "photo2.jpg"], ["Another rare book"])

    def test_item_id(self):
        self.assertEqual(self.item.item_id, "1")

    def test_user_id(self):
        self.assertEqual(self.item.user_id, "2")

    def test_description(self):
        self.assertEqual(self.item.description, "A rare book")

    def test_photos(self):
        self.assertEqual(self.item.photos, ["photo1.jpg", "photo2.jpg"])

    def test_desired_exchanges(self):
        self.assertEqual(self.item.desired_exchanges, ["Another rare book"])

if __name__ == '__main__':
    unittest.main()
```