from .orderDetailPage import OrderDetailPage


class OrderHistoryPage:

    def __init__(self, page):
        self.page = page

    def selectOrder(self, orderId):
        orderRow = self.page.locator("tr").filter(has_text=orderId)
        orderRow.get_by_role("button", name="View").click()
        orderDetailPage = OrderDetailPage(self.page)
        return orderDetailPage