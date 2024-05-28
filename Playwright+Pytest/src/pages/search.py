from src.pages.cart import CartPage


class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_title = page.get_by_text("Results", exact=True)
        self.add_button = page.locator("#a-autoid-2-announce")
        self.cart = page.get_by_label("items in cart")
    
    def add_product_to_cart(self):
        self.add_button.click()
   
    def open_cart(self):
        self.cart.click()
        return  CartPage(self.page)
    
