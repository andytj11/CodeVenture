import json


class Database:
    """
    A database class for storing and managing user data.

    Args:
        filename (str): The name of the JSON file used to store data.

    Attributes:
        filename (str): The name of the JSON file used to store data.
        data (dict): A dictionary to store user data.

    Methods:
        load_data(): Load user data from the JSON file.
        save_data(): Save user data to the JSON file.
        get_user_by_username(username): Get user data by username.
    """
    def __init__(self, filename):
        """
        Initialize the Database.

        Args:
            filename (str): The name of the JSON file used to store data.
        """
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """
        Load user data from the JSON file.

        Returns:
            dict: The loaded user data as a dictionary.
        """
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            data = {}
            print("File not found!")

        return data

    def save_data(self):
        """
        Save user data to JSON file
        """
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_user_by_username(self, username):
        """
        Get user data by username.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            dict or None: User data if found, None if not found.
        """
        if username in self.data:
            return self.data[username]
        return None


if __name__ == "__main__":
    db = Database("users.json")
    db.data.append('a')
    print(db.data)