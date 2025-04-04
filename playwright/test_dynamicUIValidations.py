from playwright.sync_api import Page, expect


def test_UIValidationDynamicSctipt(page:Page):
    #iphoneX and Nokia Edge - verify 2 items are showing in cart.
    #select_option, filter, check, click, to_have_count
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media")).to_have_count(2)
    expect(page.get_by_text("iphone X")).to_be_visible()
    expect(page.get_by_text("Nokia Edge")).to_be_visible()


def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    #Next 3 lines is how to handle child windows
    with page.expect_popup() as childPage_info:
        page.locator(".blinkingText").click()
        childPage = childPage_info.value
        #extracting part of the string and asserting
        text = childPage.locator(".red").text_content()
        text_split = text.split("at")
        email = text_split[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"


