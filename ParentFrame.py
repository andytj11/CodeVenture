import tkinter as tk

class ParentDashboardFrame(tk.Frame):
    def __init__(self, master, login_frame, user, users, topics):
        super().__init__(master)
        self.master = master
        self.login_frame = login_frame
        self.user = user
        self.users = users
        self.topics = topics  

        # Create a label to display the parent's name
        self.welcome_label = tk.Label(self, text=f"Welcome Parent, {self.user['firstname']}", font=("Arial", 18, "bold"), fg="blue")
        self.welcome_label.pack(pady=10)

        # Create a label to enter child usernames
        self.child_label = tk.Label(self, text="Enter your child's username:", font=("Arial", 14))
        self.child_label.pack()

        # Create an entry field for child usernames
        self.child_username_entry = tk.Entry(self, font=("Arial", 12))
        self.child_username_entry.pack(padx=10, pady=5)

        # Create a button to view child progress
        self.view_progress_button = tk.Button(self, text="View Progress", font=("Arial", 14), bg="green", fg="white",
                                            command=self.view_child_progress)
        self.view_progress_button.pack(pady=10)

        # Create a frame to display child progress
        self.child_progress_frame = tk.Frame(self)
        self.child_progress_frame.pack()

        self.child_progress_label = tk.Label(self.child_progress_frame, text="", font=("Arial", 12), justify="left")
        self.child_progress_label.pack()

        # Create a "Back" button to return to the dashboard
        self.back_button = tk.Button(self, text="Back", font=("Arial", 14), bg="red", fg="white",
                                    command=self.return_to_dashboard)
        self.back_button.pack(pady=10)

    def view_child_progress(self):
        """
        Method to view and display the child's progress when the "View Progress" button is clicked.
        """
        child_username = self.child_username_entry.get()
        
        # Retrieve progress data for the child and display it
        child_progress = self.get_child_progress(child_username)
        self.display_child_progress(child_progress)

    def get_child_progress(self, child_username):
        """
        Method to retrieve the progress data for a child with a given username.

        Parameters:
        - child_username: The username of the child.

        Returns:
        - child_progress: Progress data for the child or None if not found.
        """
        # Look up the child's progress in your JSON data
        for user in self.users:
            if user["username"] == child_username and "progress" in user:
                return user["progress"]
        return None

    def display_child_progress(self, child_progress):
        """
        Method to display the child's progress.

        Parameters:
        - child_progress: Progress data for the child.
        """
        if child_progress is not None:
            progress_text = "Child Progress:\n"
            for key, value in child_progress.items():
                topic = self.topics.get(key, {})
                title = topic.get("title", "Title Not Found")
                status = "Completed" if value else "Not Completed"
                progress_text += f"{key}. {title} - {status}\n"
            self.child_progress_label.config(text=progress_text)
        else:
            self.child_progress_label.config(text="Child not found or has no progress data.")
        
    def return_to_dashboard(self):
        """
        Method to return to the parent's dashboard and clear the input fields.
        """
        self.child_username_entry.delete(0, tk.END)  # Clear the child username entry field
        self.child_progress_label.config(text="")  # Clear the progress label
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
