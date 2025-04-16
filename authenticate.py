from database import *
import time


class Authenticate:
    """
    This class provides user authentication and registration functionality.

    Args:
        database (Database): An instance of the 'Database' class to store user data.

    Attributes:
        database (Database): The 'Database' instance used for data storage.
        data (list): A list of user data stored in the 'Database' instance.

    Methods:
        validate_name(name: str) -> bool: Validates the user's name.
        validate_password(password: str) -> bool: Validates the user's password.
        validate_user_role(role: str) -> bool: Validates the user's role.
        _prompt_user() -> [str]: Prompts the user for registration information.
        register_user(firstname: str, lastname: str, password: str, user_role: str) -> dict: Registers a new user.
        login_user(username: str, password: str) -> dict or bool: Authenticates and logs in a user.

    """

    def __init__(self, database: Database):
        """
        Initialize the Authenticate class with a Database instance.

        Args:
            database (Database): An instance of the 'Database' class for user data storage.
        """
        self.database = database
        self.data = self.database.data

    def validate_name(self, name: str):
        """
        Validate the user's name.

        Args:
            name (str): The user's name to be validated.

        Returns:
            bool: True if the name is valid, otherwise False.
        """
        if name.isalpha() and len(name) < 12:
            return True
        return False

    def validate_password(self, password):
        """
        Validate the user's password.

        Args:
            password (str): The user's password to be validated.

        Returns:
            bool: True if the password is valid, otherwise False.
        """
        if 6 <= len(password) <= 15:
            return True

        if not (any(char.isalpha() for char in password) and any(char.isdigit() for char in password)):
            return False

        return False

    def validate_user_role(self, role: str):
        """
        Validate the user's role.

        Args:
            role (str): The user's role to be validated.

        Returns:
            bool: True if the role is valid, otherwise False.
        """
        if role.lower() in ['YoungLearner', 'Educator', 'Parent']:
            return True
        return False

    def _prompt_user(self) -> [str]:
        """
        Prompt the user for registration information.

        Returns:
            list: A list of user registration information [firstname, lastname, username, password, user_role].
        """
        output_credential = []

        firstname = input("Enter your first name (Must be all alphabets and cannot exceed 12 letters): ").strip()

        while not self.validate_name(firstname):
            firstname = input(
                "Invalid first name, please enter a valid name (All alphabets and maximum 12 letters): ").strip()

        firstname = firstname[0].upper() + firstname[1:].lower()
        time.sleep(0.5)
        print()

        lastname = input("Enter your last name (Must be all alphabets and cannot exceed 12 letters): ").strip()

        while not self.validate_name(lastname):
            lastname = input(
                "Invalid last name, please enter a valid name (All alphabets and maximum 12 letters): ").strip()

        lastname = lastname[0].upper() + lastname[1:].lower()
        time.sleep(0.5)
        print()

        username = firstname.lower() + lastname[0]

        password = input(
            "Please enter your password (Must consist of 8-15 letters and contain a combination of letters and numbers): ")

        while not self.validate_password(password):
            password = input(
                "Please enter a valid Password (Must consist of 8-15 letters and contain a combination of letters and numbers): ")

        time.sleep(0.5)
        print()

        user_role = input("Please enter your role (Learner: <l>, Educator: <e>, Parent: <p>): ").strip()

        while not self.validate_user_role(user_role):
            user_role = input("Invalid role, Please enter a valid role (Learner: <l>, Educator: <e>, Parent: <p>): ")
        if user_role.lower() == 'l':
            user_role = "younglearner"
        elif user_role.lower() == 'e':
            user_role = "educator"
        elif user_role.lower() == 'p':
            user_role = "parent"
        output_credential.extend([firstname, lastname, username, password, user_role])

        time.sleep(1)
        print()

        return output_credential

    def register_user(self, firstname, lastname, password, user_role):
        """
        Register a new user.

        Args:
            firstname (str): User's first name.
            lastname (str): User's last name.
            password (str): User's password.
            user_role (str): User's role (younglearner, educator, or parent).

        Returns:
            dict: User information if registration is successful, False otherwise.
        """
        if self.validate_name(firstname) and self.validate_name(lastname) and self.validate_password(password):
            firstname = firstname[0].upper() + firstname[1:].lower()

            lastname = lastname[0].upper() + lastname[1:].lower()

            username = firstname.lower() + lastname[0]

            new_user = {
                "firstname": firstname,
                "lastname": lastname,
                "username": username,
                "password": password,
                "user_role": user_role
            }

            if new_user["firstname"] in self.data:
                print("User data already exists in the Database!")

            else:
                self.data.append(new_user)
                self.database.save_data()

                return new_user
            
        else:
            print("Registration failed\n")
            return False

    def login_user(self,username,password):
        """
        Authenticate and log in a user.

        Args:
            username (str): User's username.
            password (str): User's password.

        Returns:
            dict or bool: User information if authentication is successful, False otherwise.
        """
        for user in self.data:
            if username == user["username"] and password == user["password"]:
                return user

        return False
