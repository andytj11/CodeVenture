import tkinter as tk
from tkinter import ttk


class EducatorDashboardFrame(tk.Frame):
    """
    A class for the educator dashboard frame in the tkinter interface.

    Attributes:
        master (tk.Tk): The main tkinter window.
        login_frame: The login frame for navigation.
        users (list): A list of user data.
        topics (dict): A dictionary of topics data.

    Methods:
        view_student_progress(): View the progress of a selected student.
        return_to_dashboard(): Return to the educator dashboard frame.
    """
    def _init_(self, master, login_frame, users, topics):
        """
        Initializes the EducatorDashboardFrame.

        Args:
            master (tk.Tk): The main tkinter window.
            login_frame: The login frame for navigation.
            users (list): A list of user data.
            topics (dict): A dictionary of topics data.
        """
        super()._init_(master)
        self.master = master
        self.login_frame = login_frame
        self.users = users
        self.topics = topics  # Store the topics

        # Create a dropdown menu to select a student
        self.student_var = tk.StringVar()
        student_options = ["Select a student"] + [user["username"] for user in self.users]
        self.student_dropdown = ttk.Combobox(self, textvariable=self.student_var, values=student_options)
        self.student_dropdown.pack(pady=10, padx=10)

        # Create a widget to display student progress (e.g., a listbox)
        self.progress_listbox = tk.Listbox(self, width=55, height=15)
        self.progress_listbox.pack()

        # Create a button to view progress
        self.view_progress_button = tk.Button(self, text="View Progress", command=self.view_student_progress, bg="green", fg="white", font=("Helvetica", 12))
        self.view_progress_button.pack(pady=10)

        # Back button to return to the educator dashboard
        self.back_button = tk.Button(self, text="Back", command=self.return_to_dashboard, bg="blue", fg="white", font=("Helvetica", 12))
        self.back_button.pack(pady=10)

    def view_student_progress(self):
        """
        View the progress of a selected student.
        Retrieves and displays the progress in the progress_listbox.
        """
        selected_student = self.student_var.get()
        if selected_student == "Select a student":
            # Handle the case where no student is selected
            return

        # Find the selected student's progress data in the users list
        student_progress = None
        for user in self.users:
            if user["username"] == selected_student:
                student_progress = user.get("progress", {})
                break

        # Display the progress in the progress_listbox with titles and completeness status
        self.progress_listbox.delete(0, tk.END)
        for key, value in student_progress.items():
            topic = self.topics.get(key, {})
            title = topic.get("title", "Title Not Found")
            status = "Completed" if value else "Not Completed"
            self.progress_listbox.insert(tk.END, f"{key}. {title} - {status}")

    def return_to_dashboard(self):
        """
        Return to the educator dashboard frame.
        """
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)