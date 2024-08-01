from src.pages.journey import JourneyPage

class HomePage:
    def __init__(self, page):
        self.page = page

    def open_journey(self):
        self.page.locator("a").filter(has_text="Journeys").click()

