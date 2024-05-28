

class CartPage:
    def __init__(self, page):
        self.page = page
        self.open_quantity_dropdown = page.locator("#a-autoid-0-announce")
        self.quantity_value = page.get_by_label("2", exact=True).get_by_text("2")

    def select_quantity(self):
        self.open_quantity_dropdown.click()
        self.quantity_value.click()
        

   

    
