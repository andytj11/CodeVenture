import tkinter as tk
import json


class CoursesFrame(tk.Frame):
    """
    Represents a frame for displaying course options.

    Args:
        master: The parent widget.
        student_dashboard: The student dashboard frame.
        user: The current user.
        course_data: A dictionary containing course information.

    Attributes:
        master: The parent widget.
        student_dashboard: The student dashboard frame.
        user: The current user.
        course_data: A dictionary containing course information.

    Methods:
        show_content(title, content): Display the content of a selected course.
        navigate_to_dashboard(): Navigate back to the student dashboard.
    """
    def __init__(self, master, student_dashboard, user, course_data):
        super().__init__(master)
        self.master = master
        self.student_dashboard = student_dashboard
        self.user = user
        self.course_data = course_data

        # Create a Courses Frame Title
        courses_title = tk.Label(self, text="Courses", font=("Arial", 20, "bold"))
        courses_title.pack(pady=(20, 10))

        # Create buttons for each course
        for course_id, course_info in self.course_data.items():
            course_title = course_info["title"]
            course_button = tk.Button(self, text=course_title, font=("Arial", 14),
                                      command=lambda title=course_title, content=course_info["content"]: self.show_content(title, content))
            course_button.pack(pady=5)

        # Create a Back Button to return to the Student Dashboard
        back_button = tk.Button(self, text="Back", background="#FF9966", font=("Arial", 15),
                                width=15, height=1, borderwidth=2, relief=tk.RAISED, command=self.navigate_to_dashboard)
        back_button.pack(pady=10)

    def show_content(self, title, content):
        """
        Display the content of the selected course.

        Args:
            title (str): The title of the selected course.
            content (list): The content of the selected course.
        """
        self.place_forget()
        content_frame = ContentFrame(self.master, self, title, content)
        content_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def navigate_to_dashboard(self):
        """
        Navigate back to Student DashBoard
        """
        self.place_forget()
        self.student_dashboard.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class ContentFrame(tk.Frame):
    """
    Represents a frame for displaying course content.

    Args:
        master: The parent widget.
        courses_frame: The CoursesFrame.
        title: The title of the course.
        content: The content of the course.

    Attributes:
        master: The parent widget.
        courses_frame: The CoursesFrame.
        title: The title of the course.
        content: The content of the course.

    Methods:
        navigate_to_courses(): Navigate back to the CoursesFrame.
    """
    def __init__(self, master, courses_frame ,title, content):
        super().__init__(master)
        self.master = master
        self.courses_frame = courses_frame

        # Create a label for the course title
        title_label = tk.Label(self, text=title, font=("Arial", 18, "bold"))
        title_label.pack(pady=(10, 5))

        # Create a label to display course content
        content_label = tk.Label(self, text="\n".join(content), font=("Arial", 12))
        content_label.pack(pady=(5, 10))

        # Create a Back Button to return to the CoursesFrame
        back_button = tk.Button(self, text="Back", background="#FF9966", font=("Arial", 15),
                                width=15, height=1, borderwidth=2, relief=tk.RAISED, command=self.navigate_to_courses)
        back_button.pack(pady=10)

    def navigate_to_courses(self):
        """
        Navigate back to CourseFrame
        """
        self.place_forget()
        self.courses_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)