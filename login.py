def simple_login(username_input, password_input):
    """
    A simple login function that checks hardcoded credentials.

    Args:
        username_input (str): The username entered by the user.
        password_input (str): The password entered by the user.

    Returns:
        bool: True if login is successful, False otherwise.
    """
    # Hardcoded credentials for demonstration purposes
    correct_username = "user123"
    correct_password = "password123"

    if username_input == correct_username and password_input == correct_password:
        return True
    else:
        return False

# Get user input
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

# Attempt to log in
if simple_login(entered_username, entered_password):
    print("Login successful! Welcome.")
else:
    print("Login failed. Invalid username or password.")
<<<<<<< HEAD
	
	print("Login functionality by features/login")
=======

	print("Login functionality by dev")
>>>>>>> 17d0e46 (version 2)
