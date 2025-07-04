def validate_user_data(user_data: dict) -> bool:
    """Validates the user data.

    Args:
        user_data: A dictionary containing user information.

    Returns:
        True if the user data is valid, False otherwise.
    """
    try:
        required_fields = {"id", "name", "email", "age"}
        if not required_fields.issubset(user_data.keys()):
            raise ValueError("Missing required user data fields.")
        
        if not isinstance(user_data["id"], int) or user_data["id"] <= 0:
            raise ValueError("Invalid ID: Must be a positive integer.")
        
        if not isinstance(user_data["name"], str) or not user_data["name"]:
            raise ValueError("Invalid name.")
        
        if not isinstance(user_data["email"], str) or "@" not in user_data["email"]:
            raise ValueError("Invalid email.")
        
        if not isinstance(user_data["age"], int) or user_data["age"] <= 0:
            raise ValueError("Invalid age.")
        
        return True
    except Exception as e:
        print(f"User data validation failed: {e}")
        return False


def format_user_output(user_data: dict) -> str:
    """Formats the user data for output.

    Args:
        user_data: A dictionary containing user information.

    Returns:
        A formatted string representation of the user data.
    """
    try:
        return f"User: {user_data['name']}, Age: {user_data['age']}, Email: {user_data['email']}"
    except KeyError as e:
        print(f"Missing key in user data: {e}")
        raise
    except Exception as e:
        print(f"Failed to format user output: {e}")
        raise