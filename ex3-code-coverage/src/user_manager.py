from src.utils import validate_user_data

class UserManager:
    """A class to manage user-related operations."""

    def __init__(self):
        """Initializes the UserManager with an empty user list."""
        self.users = []

    def add_user(self, user_data: dict) -> bool:
        """Adds a new user to the user list.

        Args:
            user_data: A dictionary containing user information.

        Returns:
            True if the user was added successfully, False otherwise.
        """
        try:
            if not validate_user_data(user_data):
                raise ValueError("Invalid user data")
            if any(user["id"] == user_data["id"] for user in self.users):
                print("User with this ID already exists.")
                return False
            self.users.append(user_data)
            return True
        except Exception as e:
            print(f"Failed to add user: {e}")
            return False

    def remove_user(self, user_id: int) -> bool:
        """Removes a user from the user list by ID.

        Args:
            user_id: The ID of the user to remove.

        Returns:
            True if the user was removed successfully, False otherwise.
        """
        try:
            user_to_remove = next((user for user in self.users if user["id"] == user_id), None)
            if user_to_remove is None:
                raise ValueError("User not found")
            self.users.remove(user_to_remove)
            return True
        except Exception as e:
            print(f"Failed to remove user: {e}")
            return False

    def get_user(self, user_id: int) -> dict:
        """Retrieves a user from the user list by ID.

        Args:
            user_id: The ID of the user to retrieve.

        Returns:
            A dictionary containing user information, or None if not found.
        """
        try:
            user = next((user for user in self.users if user["id"] == user_id), None)
            if user is None:
                raise ValueError("User not found")
            return user
        except Exception as e:
            print(f"Failed to get user: {e}")
            return None