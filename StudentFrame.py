import tkinter as tk
from database import Database
from authenticate import Authenticate
from CoursesFrame import CoursesFrame
from QuizFrame import QuizFrame
from ProgressFrame import ProgressInterfaceGUI
from WordSearchGameFrame import WordSearchGameFrame
import json
from NewsFrame import NewsFrame
from ResourcesFrame import ResourcesFrame


class StudentDashboardFrame(tk.Frame):
    """
    A class for the student dashboard frame in the tkinter interface.

    Attributes:
        master (tk.Tk): The main tkinter window.
        login_frame: The login frame for user authentication.
        user (dict): The user information.

    Methods:
        view_courses(): Display the course modules.
        start_quiz(): Start a quiz.
        view_progress(): View the progress interface.
        play_puzzle(): Play a word search game.
        quit(): Quit the application.
    """
    def __init__(self, master, login_frame, user):
        """
        Initializes the StudentDashboardFrame.

        Args:
            master (tk.Tk): The main tkinter window.
            login_frame: The login frame for user authentication.
            user (dict): The user information.
        """
        super().__init__(master,bg="light blue")
        self.master = master
        self.user = user
        self.login_frame = login_frame

        # Create a Student Dashboard Title
        dashboard_title = tk.Label(self, text=f"Welcome back, {self.user['firstname']}!" , font=("Arial", 20, "bold"), bg="pink")
        dashboard_title.pack(pady=(20, 10))

        # Create a "View Modules" Button
        view_modules_button = tk.Button(self, text="View Courses", background="#FF9966", font=("Arial", 15),
                                        width=15, height=1, borderwidth=2, relief=tk.RAISED, command=self.view_courses)
        view_modules_button.pack(pady=10)

        # Create a "Quiz" Button
        quiz_button = tk.Button(self, text="Quiz", background="#FF9966", font=("Arial", 15),
                                width=15, height=1, borderwidth=2, relief=tk.RAISED, command=self.start_quiz)
        quiz_button.pack(pady=10)

        # Create a "View Progress" Button
        progress_button = tk.Button(self, text="View Progress", background="#FF9966", font=("Arial", 15),
                                    width=15, height=1, borderwidth=2, relief=tk.RAISED, command=self.view_progress)
        progress_button.pack(pady=10)

        # Create a "Games" Button
        games_button = tk.Button(self, text="Games", background="#FF9966", font=("Arial", 15),
                                 width=15, height=1, borderwidth=2, relief=tk.RAISED, command=self.play_puzzle)
        games_button.pack(pady=10)

        # Create a "View News" Button
        news_button = tk.Button(self, text="View News", background="#FF9966", font=("Arial", 15),
                                     width=15, height=1, borderwidth=2, relief=tk.RAISED, command=self.view_news)
        news_button.pack(pady=10)

        # Create a "View Resources" Button
        resources_button = tk.Button(self, text="View Resources", background="#FF9966", font=("Arial", 15),
                                width=15, height=1, borderwidth=2, relief=tk.RAISED, command=self.view_resources)
        resources_button.pack(pady=10)

        # Create a "Quit" Button
        quit_button = tk.Button(self, text="Exit Codeventure", background="#FF9966", font=("Arial", 15),
                                width=15, height=1, borderwidth=2, relief=tk.RAISED, command=self.quit)
        quit_button.pack(pady=10)

    def view_news(self):
        """
        Display the news and information resources.
        """
        self.place_forget()
        self.news_frame = NewsFrame(self.master, self, self.user)
        self.news_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def view_resources(self):
        """
        Display the news and information resources.
        """
        self.place_forget()
        self.resources = ResourcesFrame(self.master, self, self.user)
        self.resources.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def view_courses(self):
        """
        Display the course modules.
        """
        self.place_forget()
        with open("course_content.json", "r") as course_file:
            course_data = json.load(course_file)
        self.courses = CoursesFrame(self.master, self, self.user,course_data)
        self.courses.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def start_quiz(self):
        """
        Start a quiz.
        """
        self.place_forget()
        with open("quiz_content.json", "r") as quiz_file:
            quiz_data = json.load(quiz_file)
        self.quiz = QuizFrame(self.master, self, self.user,quiz_data)
        self.quiz.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def view_progress(self):
        """
        View the progress interface.
        """
        self.place_forget()

        # Show the progress frame
        self.progress = ProgressInterfaceGUI(self.master, self,self.user, 'course_content.json', 'users.json')
        self.progress.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def play_puzzle(self):
        """
        Play a word search game.
        """
        self.place_forget()
        self.game_frame = WordSearchGameFrame(self.master, self)
        self.game_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def quit(self):
        """
        Quit the application.
        """
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)