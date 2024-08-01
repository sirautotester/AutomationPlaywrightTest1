1. $ source venv/bin/activate

2. $ pytest

**Issues faced:**

**1. Unable to use function from class on Journey Resource Index page.**

CLASS:
class JourneyPage1:
    def __init__(self, page):
        self.page = page
        self.create_journey_button = page.get_by_role("button", name="image Create journey")

    def open_create_journey_page(self):
        self.create_journey_button.click()


TEST:
    jouney_page.open_create_journey_page()


ERROR:
    home.py
from playwright.sync_api import expect


from src.pages.journey import JourneyPage


class HomePage:
    def __init__(self, page):
        self.page = page
        self.home_title = page.get_by_text("Hello, Interviewing!")
        self.journey_side_button = page.locator("a").filter(has_text="Journeys")   

    def open_journey(self):
        self.journey_side_button.click()
        
        return JourneyPage(self.page)
    

Test + error:
/Users/serhiisychyk/Work/AutomationAmazon/Playwright+Pytest/tests/drag_sendemail_widget_test.py::test_example[chromium] failed: page = <Page url='https://app.intempt.com/journeys'>

        #     # 4. Open Journey Detail page
>       home_page.open_journey()

Playwright+Pytest/tests/drag_sendemail_widget_test.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
Playwright+Pytest/src/pages/home.py:16: in open_journey
    return JourneyPage(self.page)
Playwright+Pytest/src/pages/journey.py:9: in __init__
    self.create_scratch_journey_button = page.get_by_role("button", name="Create journey").click()
venv/lib/python3.12/site-packages/playwright/sync_api/_generated.py:14929: in click
    self._sync(
venv/lib/python3.12/site-packages/playwright/_impl/_locator.py:156: in click
    return await self._frame.click(self._selector, strict=True, **params)
venv/lib/python3.12/site-packages/playwright/_impl/_frame.py:488: in click
    await self._channel.send("click", locals_to_params(locals()))
venv/lib/python3.12/site-packages/playwright/_impl/_connection.py:59: in send
    return await self._connection.wrap_api_call(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <playwright._impl._connection.Connection object at 0x10f09cf20>
cb = <function Channel.send.<locals>.<lambda> at 0x10f423a60>
is_internal = False

    async def wrap_api_call(
        self, cb: Callable[[], Any], is_internal: bool = False
    ) -> Any:
        if self._api_zone.get():
            return await cb()
        task = asyncio.current_task(self._loop)
        st: List[inspect.FrameInfo] = getattr(task, "__pw_stack__", inspect.stack())
        parsed_st = _extract_stack_trace_information_from_stack(st, is_internal)
        self._api_zone.set(parsed_st)
        try:
            return await cb()
        except Exception as error:
>           raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E           playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
E           Call log:
E           waiting for get_by_role("button", name="Create journey")

venv/lib/python3.12/site-packages/playwright/_impl/_connection.py:514: TimeoutError

SOLUTION:
I used steps diectly without any classes:
    #     # 5. Open Create Journey page
    
    page.get_by_role("button", name="image Create journey").click()

    #     # 6. Create Journey record from Scratch
    page.get_by_role("button", name="Create a journey").click()



**2. Were not able to Drag and Drop widgets to the work container.**

TEST:
    #     # 8. Drag and Drop "Send Email" widget to the container
    sendEmailWidget = page.locator("#workflow div").filter(has_text="Send email").nth(3)
    workArea = page.locator(".v-window__container")

    page.locator('//*[@id="workflow"]/section/aside/div[1]/section/div[2]/div[2]/div[1]/p').drag_to(page.locator(".v-window__container"))
    
    #     # 9. Verify "Send Email" widget is added to the container
    expect(page.get_by_text("SEND EMAIL Need setup Send").first).to_be_visible()
    time.sleep(2)

ERROR: 
page.get_by_text("SEND EMAIL Need setup Send").first - is not visible, because widget is not dragged.

What was used:
.drag_to function. 
I tried directly with elements locators and through variables.

sendEmailWidget locators were used:
locator("div:nth-child(2) > div > .transformersDrawer__body__transformerType__transformer__drag").first
locator("#workflow div").filter(has_text="Send email").nth(3)
get_by_text("Send email", exact=True)
locator(".transformersDrawer__body__transformerType__transformer__icon__image").first
(//div[@class='transformersDrawer__body__transformerType__transformer'])[3]

workArea locators were used:
page.locator(".v-window__container")
v-window-item v-window-item--active
//*[@id="app"]/div/main/div/section/div[1]/div
journeyConstructor
//*[@id="workflow"]/section
