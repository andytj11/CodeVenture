# Import the necessary libraries
import tkinter as tk
from tkinter import scrolledtext
from news_database import NewsDatabase


class NewsFrame(tk.Frame):
    """
    A class for creating and managing the GUI of a news application.

    Attributes:
    master (tk.Tk): The main window of the application.
    database (NewsDatabase): An instance of the NewsDatabase class to handle the news articles.
    listbox (tk.Listbox): A listbox to display the titles of news articles.
    read_button (tk.Button): A button to read the selected article.
    quit_button (tk.Button): A button to quit the application.
    """

    def __init__(self, master, student_frame, user):
        """
        The constructor for the NewsApp class.

        Parameters:
        master (tk.Tk): The main window of the application.
        """
        super().__init__(master)
        self.master = master
        self.student_frame = student_frame
        self.user = user
        master.title("Coding News and Information - Python Programming")

        self.database = NewsDatabase()

        self.listbox = tk.Listbox(master)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.display_articles()

        self.read_button = tk.Button(master, text="Read Article", command=self.read_article)
        self.read_button.pack()

        self.return_button = tk.Button(master, text="Return to Dashboard", background="#FF9966", font=("Arial", 15),
                                       width=15, height=1, borderwidth=2, relief=tk.RAISED,
                                       command=self.return_to_dashboard)
        self.return_button.pack()

        self.center_window()

    def center_window(self):
        """
        Centers the main window on the screen and sets its size.
        """
        self.master.geometry("800x600")  # Set the size of the main window
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def display_articles(self):
        """
        Displays the titles of the news articles in the listbox.
        """
        articles = self.database.articles
        for idx, article in enumerate(articles):
            self.listbox.insert(idx, f"{article.title} by {article.author}")

    def read_article(self):
        """
        Opens a new window to display the content of the selected news article.
        """
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            article = self.database.get_article(selected_index)
            if article:
                self.display_article(article)

    def return_to_dashboard(self):
        """
        Return to the student dashboard frame.
        """
        # Hide the current frame
        self.place_forget()

        # Show the student dashboard frame
        self.student_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def display_article(self, article):
        """
        Displays the content of the selected news article in a new window.

        Parameters:
        article (Article): The selected news article to be displayed.
        """
        top = tk.Toplevel(self.master)
        top.title(article.title)

        author_label = tk.Label(top, text=f"Author: {article.author}")
        author_label.pack()

        content_text = scrolledtext.ScrolledText(top, wrap=tk.WORD)
        content_text.insert(tk.INSERT, article.content)
        content_text.config(state="disabled")
        content_text.pack(fill=tk.BOTH, expand=True)

        self.center_article_window(top)

    def center_article_window(self, top):
        """
        Centers the article window on the screen and sets its size.

        Parameters:
        top (tk.Toplevel): The window to be centered.
        """
        top.geometry("600x400")  # Set the size of the article window
        top.update_idletasks()
        width = top.winfo_width()
        height = top.winfo_height()
        x = (top.winfo_screenwidth() // 2) - (width // 2)
        y = (top.winfo_screenheight() // 2) - (height // 2)
        top.geometry(f"{width}x{height}+{x}+{y}")

