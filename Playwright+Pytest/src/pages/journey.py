from src.pages.create_journey import CreateJourneyPage
from src.pages.journey_detail_page import JourneyDetailPage
from playwright.sync_api import expect


class JourneyPage:
    def __init__(self, page):
        self.page = page
        self.automation_journey_record = page.get_by_role("cell", name="Automation_journey")
        self.journey_title = page.locator("(//p[@class='intempt-color-black intempt-font-h3'][normalize-space()='Journeys'])[1]")
        self.create_journey_button = page.get_by_role("button", name="image Create journey")
        self.create_scratch_journey_button = page.get_by_role("button", name="Create ajourney", exact=True)

    
    def verify_journey_page(self):
        expect(self.journey_title).to_be_visible()

    def open_journey_detail_page(self):
        self.page.locator("(//p[@class='intempt-color-black intempt-font-h3'][normalize-space()='Journeys'])[1]").click()

        return JourneyDetailPage(self.page)  

    #def click_create_scratch_journey_page(self):
     #   self.create_scratch_journey_button.click()            


    
