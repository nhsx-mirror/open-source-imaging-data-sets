from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
from io import BytesIO

# Define settings
chrome_options = Options()
chrome_options.add_argument("--headless")

screenshot_path = "../public/screenshots/"

# Create a new headlesss browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)

# Set the size of the browser
screenshot_width = 1280
screenshot_height = 1024

driver.set_window_size(screenshot_width, screenshot_height)

# Define function to grab, resize and save screenshot
def grab_screenshot(
    url, screenshot, driver=driver, thumbnail_width=300, thumbnail_height=240
):
    """Saves a screenshot of a URL

    Args:
        url (string): URL of website to grab
        screenshot (string): Path and filename of screenshot to save
        driver (object): webdriver object
        thumbnail_width (int): width of thumbnail (px)
        thumbnail_height (int): height of thumbnail (px)
    """

    try:
        # grab the screenshot
        driver.get(url)
        screen = driver.get_screenshot_as_png()

        # resize the screenshot
        img = Image.open(BytesIO(screen))
        img = img.resize((thumbnail_width, thumbnail_height), Image.ANTIALIAS)

        # save the screenshot
        img.save(screenshot)
        # driver.save_screenshot(screenshot_path + "screenshot.png")
    except:
        raise Exception(f"Error snapshotting {url}")


grab_screenshot(
    url="https://stackoverflow.com/questions/53657215/running-selenium-with-headless-chrome-webdriver",
    screenshot=f"{screenshot_path}test.png",
)

driver.close()
