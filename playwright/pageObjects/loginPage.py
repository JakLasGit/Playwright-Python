from .dashboardPage import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page


    def goto(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self, userName, userPassword):
        self.page.locator("#userEmail").fill(userName)
        self.page.locator("#userPassword").fill(userPassword)
        self.page.get_by_role("button", name="Login").click()
        dashboardPage = DashboardPage(self.page)
        return dashboardPage