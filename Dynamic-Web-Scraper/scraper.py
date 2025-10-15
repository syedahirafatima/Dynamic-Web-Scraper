from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_dynamic(url, query):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(url)
    time.sleep(3)

    # Example: scrape all matching elements (like paragraphs or divs)
    elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{query}')]")
    data = [el.text for el in elements if el.text.strip()]

    driver.quit()
    return {"count": len(data), "results": data[:10]}  # return first 10 matches
