from .orderHistoryPage import OrderHistoryPage


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def selectOrdersLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        orderHistoryPage = OrderHistoryPage(self.page)
        return orderHistoryPage