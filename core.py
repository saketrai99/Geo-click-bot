import time, random
import undetected_chromedriver as uc
from selenium_stealth import stealth
from .utils import human_scroll, random_click

def run_bot_session(proxy, target_url):
    options = uc.ChromeOptions()
    options.add_argument(f'--proxy-server=http://{proxy["ip"]}:{proxy["port"]}')
    options.add_argument('--window-size=1280,720')
    options.add_argument('--disable-blink-features=AutomationControlled')

    # Headless=False by default for realism; set True if needed
    driver = uc.Chrome(options=options, headless=False)

    # Apply stealth patches
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL",
            fix_hairline=True)

    try:
        driver.get(target_url)
        human_scroll(driver)
        random_click(driver)
        time.sleep(random.uniform(4, 10))
    except Exception as e:
        print(f"[ERROR] Session failed: {e}")
    finally:
        driver.quit()
