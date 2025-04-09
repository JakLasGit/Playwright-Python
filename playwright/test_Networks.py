import pytest
from playwright.sync_api import Page, Playwright, expect
from utils.apiBase import APIUtils

# Passing fake API response to test another test case
fakePayloadOrderResponse = {"data": [], "message": "No Orders"}
def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )
@pytest.mark.smoke
def test_Network_1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.locator("#userEmail").fill("testing@wp.pl")
    page.locator("#userPassword").fill("Test12345")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)


def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")

def test_Network_2(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.locator("#userEmail").fill("testing@wp.pl")
    page.locator("#userPassword").fill("Test12345")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)


def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    get_token = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{get_token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()


