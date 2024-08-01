import time

from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright, Playwright


from src.pages.main import MainPage
from src.pages.home import HomePage
from src.pages.journey1 import JourneyPage1


def test_example(page):
    main_page = MainPage(page)
    #     # 1. Navigate to Amazon homepage
    main_page.navigate()

    #     # 2. Enter Email
    main_page.login_email("bolam74153@apn7.com")

    #     # 3. Enter Password and Log in
    main_page.login_password("IntemptRocks$1")
  
    #     # 3. Verify user is Logged In
    home_page = HomePage(page)

    #     # 4. Open Journey Resouce page
    home_page.open_journey()

    #     # 5. Open Project Template tab
    page.get_by_role("button", name="icon Public templates").click()
    expect(page.get_by_text("Preview template Use template I I Intempt Internal Use Only jv6 SendGrid")).to_be_visible()
    page.get_by_text("Use template").first.click()
    

    #     # 6. Drag and Drop "Send Email" widget to the container
    sendEmailWidget = page.locator("#workflow div").filter(has_text="Send email").nth(3)
    workArea = page.locator(".v-window__container")

    page.locator('//*[@id="workflow"]/section/aside/div[1]/section/div[2]/div[2]/div[1]/p').drag_to(page.locator(".v-window__container"))
    
    #     # 7. Verify "Send Email" widget is added to the container
    expect(page.get_by_text("SEND EMAIL Need setup Send").first).to_be_visible()
    time.sleep(2)

