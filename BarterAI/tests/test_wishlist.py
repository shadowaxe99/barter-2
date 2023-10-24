```python
import unittest
from BarterAI.src.user_profile_and_listings import wishlist

class TestWishlist(unittest.TestCase):

    def setUp(self):
        self.user_data = {
            "user_id": "123",
            "username": "test_user",
            "email": "test_user@example.com",
            "trade_history": [],
            "wishlist": []
        }

    def test_add_to_wishlist(self):
        item_id = "456"
        wishlist.add_to_wishlist(self.user_data, item_id)
        self.assertIn(item_id, self.user_data["wishlist"])

    def test_remove_from_wishlist(self):
        item_id = "456"
        self.user_data["wishlist"].append(item_id)
        wishlist.remove_from_wishlist(self.user_data, item_id)
        self.assertNotIn(item_id, self.user_data["wishlist"])

    def test_get_wishlist(self):
        item_id_1 = "456"
        item_id_2 = "789"
        self.user_data["wishlist"].append(item_id_1)
        self.user_data["wishlist"].append(item_id_2)
        result = wishlist.get_wishlist(self.user_data)
        self.assertEqual(result, [item_id_1, item_id_2])

if __name__ == '__main__':
    unittest.main()
```