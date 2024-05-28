import pytest

@pytest.fixture()
def set_up_tear_down(page):
    page.goto("https://www.amazon.in/")
    yield page
