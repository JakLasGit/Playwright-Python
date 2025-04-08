from playwright.sync_api import expect


class OrderDetailPage:

    def __init__(self, page):
        self.page = page

    def verifyOrderMessage(self):
        expect(self.page.locator("body")).to_contain_text("Thank you for Shopping With Us")