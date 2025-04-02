from pytest_playwright.pytest_playwright import browser
from playwright.sync_api import Page

# Giga surowe, przydatne jeżeli jest potrzebna jakaś konfiguracja przeglądarek
def test_playwrightBasics(playwright, browser):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

# chromium engine on headless mode, 1 single context
def test_playwrightShortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")


def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

#teścik githuba!