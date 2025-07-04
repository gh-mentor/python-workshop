import unittest
from src.user_manager import UserManager


class TestUserManager(unittest.TestCase):
    """Unit tests for the UserManager class."""

    def setUp(self) -> None:
        """Set up a new UserManager instance for each test."""
        self.user_manager = UserManager()

    def test_add_user(self):
        """Test the add_user method of UserManager."""
        user_data = {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30}
        result = self.user_manager.add_user(user_data)
        self.assertTrue(result)
        self.assertEqual(self.user_manager.get_user(1), user_data)

    def test_add_user_duplicate(self):
        """Test adding a duplicate user."""
        self.user_manager.add_user({"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30})
        result = self.user_manager.add_user({"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30})
        self.assertFalse(result)
        self.assertEqual(len(self.user_manager.users), 1)  # Ensure no duplicate is added

    def test_remove_user(self):
        """Test the remove_user method of UserManager."""
        self.user_manager.add_user({"id": 2, "name": "Bob", "email": "bob@example.com", "age": 25})
        result = self.user_manager.remove_user(2)
        self.assertTrue(result)
        self.assertIsNone(self.user_manager.get_user(2))

    def test_remove_user_not_found(self):
        """Test removing a user that does not exist."""
        result = self.user_manager.remove_user(3)
        self.assertFalse(result)
        self.assertEqual(len(self.user_manager.users), 0)  # Ensure no user is removed

    def test_get_user(self):
        """Test the get_user method of UserManager."""
        self.user_manager.add_user({"id": 4, "name": "David", "email": "david@example.com", "age": 40})
        user = self.user_manager.get_user(4)
        self.assertIsNotNone(user)
        self.assertEqual(user["email"], "david@example.com")

    def test_get_user_not_found(self):
        """Test getting a user that does not exist."""
        user = self.user_manager.get_user(5)
        self.assertIsNone(user)
        self.assertEqual(len(self.user_manager.users), 0)  # Ensure no user is found

    def test_add_user_missing_fields(self):
        """Test adding a user with missing required fields."""
        user_data = {"id": 6, "name": "Eve"}  # Missing 'email' and 'age'
        result = self.user_manager.add_user(user_data)
        self.assertFalse(result)
        self.assertEqual(len(self.user_manager.users), 0)  # Ensure no user is added

    def test_add_user_invalid_age(self):
        """Test adding a user with an invalid age."""
        user_data = {"id": 7, "name": "Frank", "email": "frank@example.com", "age": -5}
        result = self.user_manager.add_user(user_data)
        self.assertFalse(result)
        self.assertEqual(len(self.user_manager.users), 0)  # Ensure no user is added

    def test_add_user_invalid_id(self):
        """Test adding a user with an invalid ID."""
        user_data = {"id": "invalid", "name": "Grace", "email": "grace@example.com", "age": 25}
        result = self.user_manager.add_user(user_data)
        self.assertFalse(result)
        self.assertEqual(len(self.user_manager.users), 0)  # Ensure no user is added


if __name__ == "__main__":
    unittest.main()