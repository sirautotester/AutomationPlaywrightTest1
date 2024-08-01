from playwright.sync_api import expect


class JourneyDetailPage:
    def __init__(self, page):
        self.page = page

    def verify_journey_detail_page(self):
        expect(self.page.get_by_text("Automation_journey")).to_be_visible()
    