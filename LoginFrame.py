import tkinter as tk
from database import Database
from authenticate import Authenticate
from StudentFrame import StudentDashboardFrame
from EducatorDashboardFrame import EducatorDashboardFrame
from ParentFrame import ParentDashboardFrame
import json


class LoginFrame(tk.Frame):
    """
    A class for the login frame in the tkinter interface.

    Attributes:
        master (tk.Tk): The main tkinter window.
        homepage_frame: The homepage frame for navigation.
        auth (Authenticate): An authentication object for user authentication.
        username (tk.StringVar): The username input variable.
        password (tk.StringVar): The password input variable.
        login_text (tk.StringVar): The text message variable for login outcomes.

    Methods:
        login(): Attempt to log in with the provided credentials.
        return_to_homepage(): Return to the homepage frame.
        get_young_learners(users): Filter users with "YoungLearner" role.
    """
    def __init__(self, master, homepage_frame, auth):
        """
        Initializes the LoginFrame.

        Args:
            master (tk.Tk): The main tkinter window.
            homepage_frame: The homepage frame for navigation.
            auth (Authenticate): An authentication object for user authentication.
        """
        super().__init__(master,bg = "light blue")
        self.master = master
        self.homepage_frame = homepage_frame
        self.auth = auth

        # Create a Login Title
        login_title = tk.Label(self, text="Welcome Back to CodeVenture!", font=("Arial", 20, "bold"), bg="pink")
        login_title.pack(pady=(20, 10))

        # Create a Username Label and Entry
        username_label = tk.Label(self, text="Username", font=("Arial", 12))
        username_label.pack(pady=(10, 0), anchor="w")
        self.username = tk.StringVar()
        self.username_entry = tk.Entry(self, textvariable=self.username)
        self.username_entry.pack(pady=(0, 10), fill="x", expand=True)

        # Create a Password Label and Entry
        password_label = tk.Label(self, text="Password", font=("Arial", 12))
        password_label.pack(pady=(10, 0), anchor="w")
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(self, textvariable=self.password, show="•")
        self.password_entry.pack(pady=(0, 10), fill="x", expand=True)

        # Create a Login Button with changed color
        login_button = tk.Button(self, text="Login", background="#FF9966", font=("Arial", 15),
                                 width=15, height=1, borderwidth=2, relief=tk.RAISED, command=self.login)
        login_button.pack(pady=10)

        # Create a Back Button with changed color
        back_button = tk.Button(self, text="Back", background="#FF9966", font=("Arial", 15),
                                width=15, height=1, borderwidth=2, relief=tk.RAISED, command=self.return_to_homepage)
        back_button.pack(pady=10)

        # Create a Login outcome message
        self.login_text = tk.StringVar()
        login_message = tk.Message(self, textvariable=self.login_text, width=350, font=("Arial", 11))
        login_message.pack(pady=(10, 0), fill="x", expand=True)

    def login(self):
        """
        Attempt to log in with the provided credentials.
        Redirect to the student or educator dashboard based on the user's role.
        Display a message in case of login failure.
        """

        user = self.auth.login_user(self.username.get(), self.password.get())
        if user:
            if user["user_role"] == "YoungLearner":
                self.place_forget()
                student_frame = StudentDashboardFrame(self.master, self, user)
                student_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            elif user["user_role"] == "Educator":
                self.place_forget()
                with open('users.json', 'r') as users_f:
                    all_users = json.load(users_f)
                    young_learners = self.get_young_learners(all_users)

                with open('course_content.json', "r") as content:
                    course_content = json.load(content)

                educator_frame = EducatorDashboardFrame(self.master, self, young_learners, course_content)
                educator_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            elif user["user_role"] == "Parent":
                self.place_forget()
                with open('users.json', 'r') as users_f:
                    all_users = json.load(users_f)
                    young_learners = self.get_young_learners(all_users)

                with open('course_content.json', "r") as content:
                    course_content = json.load(content)

                parent_frame = ParentDashboardFrame(self.master, self, user, young_learners, course_content)
                parent_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        else:
            self.login_text.set("Login Failed")

    def return_to_homepage(self):
        """Return to the homepage frame."""
        self.place_forget()
        self.homepage_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def get_young_learners(self, users):
        """
        Filter the list of users to include only those with the "YoungLearner" role.

        Args:
            users (list): A list of user data.

        Returns:
            list: A filtered list containing only young learners.
        """
        # Filter the list of users to include only those with the "YoungLearner" role
        young_learners = [user for user in users if user["user_role"] == "YoungLearner"]
        return young_learners