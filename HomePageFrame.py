import tkinter as tk
from database import Database
from RegisterFrame import RegisterFrame
from authenticate import Authenticate
from LoginFrame import LoginFrame


class HomePageFrame(tk.Frame):
    """
    A class for the home page frame of CodeVenture.

    Attributes:
        master: The main window containing the home page frame.
        database: An instance of the Database class for managing user data.
        authenticate: An instance of the Authenticate class for user authentication.

    Methods:
        __init__(self, master): Constructor for the HomePageFrame class.
        navigate_to_login(self): Handle the action when the "Login" button is clicked.
        navigate_to_register(self): Handle the action when the "Register" button is clicked.
        shutdown_application(self): Shut down the application.
    """
    def __init__(self, master):
        """
        Constructor for the HomePageFrame class.

        Args:
            master (Tk): The main window that the home page frame is contained in.
        """
        super().__init__(master=master,bg="turquoise")
        self.master = master

        self.database = Database('users.json')
        self.authenticate = Authenticate(self.database)

        self.grid_columnconfigure(0, weight=1)

        home_page_title = tk.Label(self, text="Welcome to CodeVenture", font=("Helvetica", 25, "bold"), bg = "turquoise", fg="dark green")
        home_page_title.grid(row=0, columnspan=3)

        # Create a canvas for the image
        self.home_canvas = tk.Canvas(master=self, width=500, height=500, bg="light green")
        self.home_canvas.grid(row=1, column=0, padx=20, pady=20)


        # Load and display an image on the canvas
        self.home_image = tk.PhotoImage(file="images/homepage.png")
        self.home_image = self.home_image.subsample(4)
        self.home_canvas.create_image(100, 30,
                                      anchor=tk.NW,
                                      image=self.home_image)

        # Create a frame for the "Login" and "Register" buttons
        button_frame = tk.Frame(master=self,bg="turquoise")
        button_frame.grid(row=1, column=1, sticky=tk.N, columnspan=1)

        # Create a "Register" button
        # Create a "Register" button with custom colors and font
        register_button = tk.Button(master=button_frame, text="Register", font=("Arial", 15),
                                    width=15, height=2, borderwidth=2, relief=tk.RAISED,
                                    command=self.navigate_to_register, bg="dodger blue", fg="white")
        # Make the button span 2 columns to center it
        register_button.grid(row=0, column=0, padx=20, pady=10)

        # Create a "Login" button with custom colors and font
        login_button = tk.Button(master=button_frame, text="Login", font=("Arial", 15),
                                width=15, height=2, borderwidth=2, relief=tk.RAISED,
                                command=self.navigate_to_login, bg="forest green", fg="white")
        login_button.grid(row=1, column=0, padx=10, pady=10)

        # Create a "Shutdown" button with custom colors and font
        shutdown_button = tk.Button(master=button_frame, text="Shutdown", font=("Arial", 15),
                                    width=15, height=2, borderwidth=2, relief=tk.RAISED,
                                    command=self.shutdown_application, bg="firebrick", fg="white")
        shutdown_button.grid(row=2, column=0, padx=10, pady=10)


    def navigate_to_login(self):
        """
        Function to handle the action when the "Login" button is clicked.
        """
        self.place_forget()
        login_frame = LoginFrame(self.master, self, self.authenticate)
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def navigate_to_register(self):
        """
        Function to handle the action when the "Register" button is clicked.
        """
        self.place_forget()
        register_frame = RegisterFrame(self.master, self, self.authenticate)
        register_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def shutdown_application(self):
        """
        Function to shut down the application.
        """
        self.master.quit()