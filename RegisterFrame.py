import tkinter as tk
from authenticate import Authenticate


class RegisterFrame(tk.Frame):
    """
    A class for the registration frame in the tkinter interface.

    Attributes:
        master (tk.Tk): The main tkinter window.
        homepage_frame: The homepage frame to return to.
        auth (Authenticate): An authentication object for user registration.

    Methods:
        register(): Register a new user account.
        return_to_home(): Return to the homepage frame.
    """
    def __init__(self, master, homepage_frame, authenticator: Authenticate):
        """
        Initializes the RegisterFrame.

        Args:
            master (tk.Tk): The main tkinter window.
            homepage_frame: The homepage frame to return to.
            authenticator (Authenticate): An authentication object for user registration.
        """
        super().__init__(master, bg = "orange")
        self.master = master
        self.homepage_frame = homepage_frame
        self.authenticate = authenticator

        # Create a Register Title with Arial font
        register_title = tk.Label(self, text="Create Account", font=("Arial", 24, "bold"),bg="pink")
        register_title.pack(padx=10, pady=(20, 10))

        # Create First Name Label and Entry with Arial font
        first_name_label = tk.Label(self, text="First Name", font=("Arial", 12))
        first_name_label.pack(padx=10, pady=5, anchor="w")
        self.first_name = tk.StringVar()
        self.first_name_entry = tk.Entry(self, textvariable=self.first_name, font=("Arial", 12))
        self.first_name_entry.pack(padx=10, pady=5, fill="both", expand=True)

        # Create Last Name Label and Entry with Arial font
        last_name_label = tk.Label(self, text="Last Name", font=("Arial", 12))
        last_name_label.pack(padx=10, pady=5, anchor="w")
        self.last_name = tk.StringVar()
        self.last_name_entry = tk.Entry(self, textvariable=self.last_name, font=("Arial", 12))
        self.last_name_entry.pack(padx=10, pady=5, fill="both", expand=True)

        # Create Password Label and Entry with Arial font
        password_label = tk.Label(self, text="Password", font=("Arial", 12))
        password_label.pack(padx=10, pady=5, anchor="w")
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(self, textvariable=self.password, show="•", font=("Arial", 12))
        self.password_entry.pack(padx=10, pady=5, fill="both", expand=True)

        # Create User Type Label and Dropdown with Arial font
        user_type_label = tk.Label(self, text="User Type", font=("Arial", 12))
        user_type_label.pack(padx=10, pady=5, anchor="w")
        self.user_type = tk.StringVar()
        self.user_type.set("YoungLearner")
        user_type_dropdown = tk.OptionMenu(self, self.user_type, "YoungLearner", "Educator", "Parent")
        user_type_dropdown.configure(font=("Arial", 12))  # Modify the font of the dropdown
        user_type_dropdown.pack(padx=10, pady=5, fill="both", expand=True)

        # Create Register Button with Arial font
        register_button = tk.Button(self, text="Register", command=self.register,
                                    font=("Arial", 15), width=15, height=1, borderwidth=2, relief=tk.RAISED)
        register_button.pack(padx=10, pady=(10, 20), fill="both", expand=True)

        # Create Back Button with Arial font
        back_button = tk.Button(self, text="Back", command=self.return_to_home,
                                font=("Arial", 15), width=15, height=1, borderwidth=2, relief=tk.RAISED)
        back_button.pack(padx=10, pady=10, fill="both", expand=True)

        # Create Register Text Message with Arial font
        self.register_text = tk.StringVar()
        register_message = tk.Message(self, textvariable=self.register_text, width=350, font=("Arial", 11))
        register_message.pack(padx=10, pady=(10, 0), fill="both", expand=True)

    def register(self):
        """
        Register a new user account.
        """
        self.register_text.set("Registering...")

        user = self.authenticate.register_user(self.first_name.get(), self.last_name.get(), self.password.get(), self.user_type.get())
        if user:
            self.register_text.set("Registration Successful")
            self.register_text.set("Registration Successful!\nYour username is: " + user["username"] + ".")
        else:
            self.register_text.set("Registration Failed")

    def return_to_home(self):
        """
        Return to the homepage frame.
        """
        self.place_forget()
        self.homepage_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
