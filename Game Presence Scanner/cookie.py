from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\Prescence_Scanner")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--disable-logging");
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--remote-debugging-port=5555')
#chrome_options.add_argument("--headless=new")
chrome_service = Service()
#chrome_service.creation_flags = CREATE_NO_WINDOW
driver = webdriver.Chrome(service=chrome_service,options=chrome_options)
driver.get("https://developer.hypixel.net/dashboard")
def get_roblox_cookie():
    driver = webdriver.Chrome(service=chrome_service,options=chrome_options)
    driver.get("https://roblox.com")
    all_cookies=driver.get_cookies();
    
    cookies_dict = {}
    for cookie in all_cookies:
        cookies_dict[cookie['name']] = cookie['value']
    driver.quit()

    return cookies_dict[".ROBLOSECURITY"]
