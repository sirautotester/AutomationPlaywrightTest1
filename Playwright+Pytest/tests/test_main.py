from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright, Playwright


from src.pages.main import MainPage
from src.pages.search import SearchPage
from src.pages.cart import CartPage


def test_example(page):
    main_page = MainPage(page)
    

    #     # 1. Navigate to Amazon homepage
    main_page.navigate()

    #     # 2. Search for product
    main_page.search("Samsung Galaxy s24")
  
    #     # 3. Verify search results
    # expect(page.get_by_text("Results", exact=True)).to_be_visible()
    search_page = SearchPage(page)
    expect(page.get_by_text("Results", exact=True)).to_be_visible()


    #     # 4. Add product to cart
    search_page.add_product_to_cart()
    
        # 5. Verify add to cart message (adjust selector if needed)
    expect(page.get_by_role("strong")).to_be_visible()

    #     # 6. Go to cart page
    search_page.open_cart()

    #     # 7. Open quantity dropdown
    cart_page = CartPage(page)
    
    #     # 8. Select new quantity
    cart_page.select_quantity()
    page.evaluate('location.reload();')


        # 9. Verify quantity update
    expect(page.get_by_text("Qty:2")).to_be_visible()         