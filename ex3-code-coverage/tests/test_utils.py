import unittest
from src.utils import validate_user_data, format_user_output


class TestUtils(unittest.TestCase):
    """Unit tests for utility functions in utils module."""

    def test_validate_user_data_valid(self):
        """Test the validate_user_data function with valid input."""
        user_data = {"id": 1, "name": "Alice", "age": 30, "email": "alice@example.com"}  # Added 'id' field
        self.assertTrue(validate_user_data(user_data))

    def test_validate_user_data_invalid_age(self):
        """Test the validate_user_data function with invalid age."""
        user_data = {"name": "Bob", "age": -5, "email": "bob@example.com"}
        self.assertFalse(validate_user_data(user_data))

    def test_validate_user_data_missing_email(self):
        """Test the validate_user_data function with missing email."""
        user_data = {"name": "Charlie", "age": 25}
        self.assertFalse(validate_user_data(user_data))

    def test_format_user_output(self):
        """Test the format_user_output function."""
        user_data = {"name": "Alice", "email": "alice@example.com", "age": 30}
        expected_output = "User: Alice, Age: 30, Email: alice@example.com"
        self.assertEqual(format_user_output(user_data), expected_output)


if __name__ == "__main__":
    unittest.main()