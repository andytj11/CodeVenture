import tkinter as tk
import json

class ProgressInterfaceGUI(tk.Frame):
    def __init__(self, master, student_frame, user, topics_file, users_file):
        """
        Constructor for the ProgressInterfaceGUI class.

        Args:
        - master (tk.Tk): The main window.
        - student_frame: The student dashboard frame.
        - user (dict): The user information.
        - topics_file (str): The path to the file containing topics data.
        - users_file (str): The path to the file containing user data.

        Attributes:
        - master (tk.Tk): The main window.
        - student_frame: The student dashboard frame.
        - user (dict): The user information.
        - topics (dict): A dictionary of topics and their details.
        - users (list): A list of user dictionaries.
        - progress (dict): A dictionary to track progress status.

        Methods:
        - center_window(): Centers the GUI on the screen.
        - display_progress(): Displays progress in the listbox.
        - update_progress(): Updates the progress when an item is marked as completed.
        - quit(): Quits the progress tracking interface and returns to the student frame.
        """
        super().__init__(master)
        self.master = master
        self.student_frame = student_frame
        self.users_file = users_file
        self.user = user

        with open(topics_file, 'r') as f:
            self.topics = json.load(f)

        with open(users_file, 'r') as users_f:
            self.users = json.load(users_f)

        if 'progress' in self.user:
            self.progress = self.user['progress']
        else:
            # If progress data is not available, initialize it
            self.user['progress'] = {str(key): False for key in self.topics.keys()}

            # Update the user's data in the list of users
            for i, u in enumerate(self.users):
                if u['username'] == self.user['username']:
                    self.users[i] = self.user
                    break

            # Save the updated user data to the users file
            with open(self.users_file, 'w') as users_f:
                json.dump(self.users, users_f, indent=4)

            # Now you can access the initialized progress
            self.progress = self.user['progress']

        self.listbox_frame = tk.Frame(self)
        self.listbox_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.listbox = tk.Listbox(self.listbox_frame, width=55, height=15, font=("Arial", 12))
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.display_progress()

        self.update_button = tk.Button(self, text="Mark as Completed", font=("Arial", 14), bg="green", fg="white",
                                       command=self.update_progress)
        self.update_button.pack(pady=10)

        self.quit_button = tk.Button(self, text="Quit", font=("Arial", 14), bg="red", fg="white", command=self.quit)
        self.quit_button.pack(pady=10)

        self.center_window()

    def center_window(self):
        """
        Centers the GUI on the screen.
        """
        self.master.geometry("800x600")
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def display_progress(self):
        """
        Displays progress in the listbox.
        """
        self.listbox.delete(0, tk.END)
        for key, topic in self.topics.items():
            status = "Completed" if self.progress[key] else "Not Completed"
            self.listbox.insert(tk.END, f"{key}. {topic['title']} - {status}")

    def update_progress(self):
        """
        Updates the progress when an item is marked as completed.
        """
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_index = selected_index[0] + 1

            self.user['progress'][str(selected_index)] = True
            for i, u in enumerate(self.users):
                if u['username'] == self.user['username']:
                    self.users[i] = self.user
                    break

            # Save the updated user data to the users file
            with open(self.users_file, 'w') as users_f:
                json.dump(self.users, users_f, indent=4)

        self.display_progress()

    def quit(self):
        """
        Quits the progress tracking interface and returns to the student frame.
        """
        self.place_forget()
        self.student_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
