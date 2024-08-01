from src.pages.home import HomePage

class MainPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://app.intempt.com/")

    def login_email(self, email):
        self.page.get_by_role("textbox", name="Enter your email").fill(email)
        
    def login_password(self, password):
        self.page.get_by_placeholder("*******").fill(password)
        self.page.get_by_role("button", name="Login").click()
 
        return HomePage(self.page)