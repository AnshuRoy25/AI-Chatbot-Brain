from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-gpu")  # Helps with GPU-related issues

service = Service("C:/WebDrivers/chromedriver.exe")  # Adjust path if needed
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.youtube.com")
input("Press Enter to exit...")  # Keeps the browser open
