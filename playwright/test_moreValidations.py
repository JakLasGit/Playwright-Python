from playwright.sync_api import Page, expect


def test_UIChecks(page:Page):
    #hidden/visible, placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.locator("#hide-textbox").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

def test_handlingAlerts(page:Page):
    #alert boxes
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    #nasłuchiwanie czy otworzy się jakiś dialog i jeżeli tak to akceptowanie
    page.on("dialog", lambda dialog: dialog.accept())
    #przycisk wywołujący dialog więc będzie automatycznie kliknięty przez poprzednią linijke
    page.get_by_role("button", name="Confirm").click()

def test_mouseHover(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()

def test_handlingFrames(page:Page):
    #frames
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")

#Check the price of rice is equal to 37
#indetify the price column
#identify rice row
#extract the price of the rice
def test_riceCheck(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            priceColValue = index
            print(f"Price column value is {priceColValue}")
            break

    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(priceColValue)).to_have_text("37")
    