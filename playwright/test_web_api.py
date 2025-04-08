from playwright.sync_api import Playwright, expect
from utils.apiBase import APIUtils


def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order --- orderId
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill("testing@wp.pl")
    page.locator("#userPassword").fill("Test12345")
    page.get_by_role("button", name = "Login").click()

    #orders History page -> order is present
    page.get_by_role("button", name = "ORDERS").click()
    orderRow = page.locator("tr").filter(has_text = orderId)
    orderRow.get_by_role("button", name = "View").click()
    expect(page.locator("body")).to_contain_text("Thank you for Shopping With Us")
    context.close()