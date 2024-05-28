from src.pages.search import SearchPage

class MainPage:
    def __init__(self, page):
        self.page = page
        self.search_term_input = page.get_by_placeholder("Search Amazon.in")

    def navigate(self):
        self.page.goto("https://www.amazon.in/")

    def search(self, text):
        self.search_term_input.fill(text)
        self.search_term_input.press("Enter")    
        return  SearchPage(self.page)