import json
from news_article import NewsArticle

class NewsDatabase:
    def __init__(self, filename="news_data.json"):
        """
        Initializes the NewsDatabase class with a filename.

        Parameters:
        filename (str): The filename of the JSON file containing news articles.
        """

        self.filename = filename
        self.articles = self.load_articles()

    def load_articles(self):
        """
        Loads articles from a JSON file and returns a list of NewsArticle objects.

        Returns:
        List[NewsArticle]: A list of NewsArticle objects.
        """

        with open(self.filename, 'r') as f:
            articles_data = json.load(f)
            return [NewsArticle(data["title"], data["content"], data["author"]) for data in articles_data]

    def get_article(self, index):
        """
        Gets an article by index from the list of articles.

        Parameters:
        index (int): The index of the article in the list.

        Returns:
        NewsArticle or None: The requested article if the index is valid, otherwise None.
        """

        if 0 <= index < len(self.articles):
            return self.articles[index]
        return None

    def list_articles(self):
        """
        Lists all the articles in the database with their index, title, and author.
        """
        
        for idx, article in enumerate(self.articles):
            print(f"{idx + 1}. {article.title} by {article.author}")

