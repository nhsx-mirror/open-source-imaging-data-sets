from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
from io import BytesIO

chrome_options = Options()
chrome_options.add_argument("--headless")
# chrome_options.add_argument(f"--force-device-scale-factor=1.0")

screenshot_path = "../public/screenshots/"

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)

screenshot_width = 1280
screenshot_height = 1024
thumbnail_width = 300
thumbnail_height = (int)(thumbnail_width * (screenshot_height / screenshot_width))

driver.set_window_size(screenshot_width, screenshot_height)

url = "https://www.cancerimagingarchive.net/collections/"
try:
    # grab the screenshot
    driver.get(url)
    screen = driver.get_screenshot_as_png()

    # resize the screenshot
    img = Image.open(BytesIO(screen))
    img = img.resize((thumbnail_width, thumbnail_height), Image.ANTIALIAS)

    # save the screenshot
    img.save(screenshot_path + "screenshot.png")
    # driver.save_screenshot(screenshot_path + "screenshot.png")
except:
    raise Exception(f"Error snapshotting {url}")

driver.close()
