###
from playwright.sync_api import expect


class JourneyPage1:
    def __init__(self, page):
        self.page = page
        self.journey_title = page.get_by_text("Journeys")

        self.create_journey_button = page.locator('//*[@id="app"]/div/main/div/section/div/div/section/header/div[1]/button')

        self.create_scratch_journey_button = page.get_by_role("button", name="Create ajourney", exact=True)
        
        self.project_templates_button = page.get_by_role("button", name="icon Project templates")
        self.project_template_card = page.get_by_text("Preview template Use template")
        self.use_project_template_button = page.get_by_text("Use template")

        self.public_templates_button = page.get_by_role("button", name="icon Public templates")
        self.public_template_card = page.get_by_text("Preview template Use template I I Intempt Internal Use Only jv6 SendGrid")
        self.use_public_template_button = page.get_by_text("Use template").first

    
    def verify_journey_page(self):
        self.journey_title.to_be_visible()

    def open_create_journey_page(self):
        self.create_journey_button.click()

    def click_create_scratch_journey_page(self):
        self.create_scratch_journey_button.click()
                
    def create_project_journey_page(self):
        self.project_templates_button.click()
        self.project_template_card.hover()
        self.use_project_template_button.click()

    def create_public_journey_page(self):
        self.public_templates_button.click()
        self.public_template_card.hover()
        self.use_public_template_button.click()

### 
