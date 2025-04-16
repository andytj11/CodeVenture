class NewsArticle:
    def __init__(self, title, content, author):
        """
        Initializes the NewsArticle class with title, content, and author.

        Parameters:
        title (str): The title of the article.
        content (str): The content of the article.
        author (str): The author of the article.
        """

        self.title = title
        self.content = content
        self.author = author

    def display(self):
        """
        Displays the article's title, author, and content.
        """
        
        print("\nTitle:", self.title)
        print("Author:", self.author)
        print("\n" + self.content + "\n")

