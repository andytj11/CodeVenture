import tkinter as tk
from tkinter import ttk
import json


class ResourcesFrame(tk.Frame):
    """
    A GUI application for displaying and opening online resources for Python programming.

    Attributes:
        master (tk.Tk): The main window of the application.
        resources (dict): A dictionary containing categories and lists of resources loaded from a JSON file.
        category_label (tk.Label): A label for the category combobox.
        categories (list): A list of categories loaded from the resources dictionary.
        category_combobox (ttk.Combobox): A combobox to select the category of resources.
        resources_listbox (tk.Listbox): A listbox to display the resources of the selected category.
        open_button (tk.Button): A button to open the selected resource in a web browser.
        quit_button (tk.Button): A button to quit the application.
    """

    def __init__(self, master, student_frame, user):

        """
        Initializes the OnlineResourcesApp instance.

        Args:
            master (tk.Tk): The main window of the application.
        """
        super().__init__(master)
        self.master = master
        self.student_frame = student_frame
        self.user = user
        master.title("Python Programming Online Resources")

        with open('resources_data.json', 'r') as f:
            self.resources = json.load(f)

        self.category_label = tk.Label(master, text="Categories:")
        self.category_label.pack()

        self.categories = list(self.resources.keys())
        self.category_combobox = ttk.Combobox(master, values=self.categories)
        self.category_combobox.pack()
        self.category_combobox.bind("<<ComboboxSelected>>", self.display_resources)

        self.resources_listbox = tk.Listbox(master, height=10)
        self.resources_listbox.pack(fill=tk.BOTH, expand=True)

        self.open_button = tk.Button(master, text="Open Resource", command=self.open_resource)
        self.open_button.pack()

        self.return_button = tk.Button(master, text="Return to Dashboard", background="#FF9966", font=("Arial", 15),
                                       width=15, height=1, borderwidth=2, relief=tk.RAISED,
                                       command=self.return_to_dashboard)
        self.return_button.pack(pady=10)

        self.set_window_size()
        self.center_window()

    def return_to_dashboard(self):
        """
        Return to the student dashboard frame.
        """
        # Hide the current frame
        self.grid_forget()

        # Show the student dashboard frame
        self.student_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def center_window(self):
        """
        Centers the main window on the screen.
        """
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() - width) // 2
        y = (self.master.winfo_screenheight() - height) // 2
        self.master.geometry(f'+{x}+{y}')

    def set_window_size(self):
        """
        Sets the size of the main window.
        """
        self.master.geometry("800x600")

    def display_resources(self, event):
        """
        Displays the resources of the selected category in the listbox.

        Args:
            event (tk.Event): The event that triggered this method.
        """
        category = self.category_combobox.get()
        self.resources_listbox.delete(0, tk.END)
        for resource in self.resources[category]:
            self.resources_listbox.insert(tk.END, f"{resource['name']} - {resource['url']}")

    def open_resource(self):
        """
        Opens the selected resource in a web browser.
        """
        selected_index = self.resources_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            category = self.category_combobox.get()
            resource = self.resources[category][selected_index]
            url = resource['url']
            import webbrowser
            webbrowser.open(url)
