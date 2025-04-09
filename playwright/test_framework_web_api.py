import pytest
import json
from playwright.sync_api import Playwright

from pageObjects.loginPage import LoginPage
from pageObjects.dashboardPage import DashboardPage
from utils.apiBaseFramework import APIUtils

# JSON file -> util -> access into test
with open("data/credentials.json") as f:
    test_data = json.load(f)
    user_credential_list = test_data["user_credentials"]

@pytest.mark.smoke
@pytest.mark.parametrize("user_credentials", user_credential_list)
def test_e2e_web_api(playwright:Playwright,browserInstance, user_credentials):
    userName = user_credentials["userEmail"]
    userPassword = user_credentials["userPassword"]

    # Create order using API --- extracting orderId
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)

    loginPage = LoginPage(browserInstance)
    loginPage.goto()
    dashboardPage = loginPage.login(userName, userPassword)
    dashboardPage.selectOrdersLink()
    orderHistoryPage = dashboardPage.selectOrdersLink()
    orderDetailPage = orderHistoryPage.selectOrder(orderId)
    orderDetailPage.verifyOrderMessage()