import tkinter as tk
from HomePageFrame import HomePageFrame


class Interface(tk.Tk):
    """
    A class for CodeVenture's main interface.

    Attributes:
        title (str): The title of the application window.
        width (int): The width of the application window.
        height (int): The height of the application window.
        homepage: An instance of the HomePageFrame.

    Methods:
        __init__(self, title, width=800, height=650): Constructor for the Interface class.
    """
    def __init__(self, title, width=800, height=650):
        """
        Constructor for the Interface class.

        Args:
            title (str): The title of the application window.
            width (int): The width of the application window.
            height (int): The height of the application window.
        """
        super().__init__()
        self.title(title)
        self.configure(bg="light green")
        self.geometry(f"{width}x{height}")
        self.homepage = HomePageFrame(self)
        self.homepage.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


if __name__ == "__main__":
    # DO NOT MODIFY THIS
    codeventure = Interface("CodeVenture")

    codeventure.mainloop()
    print("--- End of program execution ---")
