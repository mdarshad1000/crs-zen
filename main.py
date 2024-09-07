from fastapi import FastAPI
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
from selenium_stealth import stealth
import uvicorn
import os

app = FastAPI()


def run_playwright():
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")
    # Specify the path to the Chrome binary
    # chrome_binary_path = os.path.join(os.getcwd(), 'chrome', 'chrome')
    # options.binary_location = chrome_binary_path
    # chromedriver_path = os.path.join(os.getcwd(), 'chromedriver')
    
    driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    
    driver.get("https://crsreports.congress.gov/search/results?term=&r=59285836&orderBy=Date&navids=4294966212&pageNumber=5")
    pre_content = driver.page_source
    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(pre_content, 'lxml')
    pre_tag_content = soup.find('pre').text if soup.find('pre') else 'No <pre> tag found'
    content = json.loads(pre_tag_content)

    driver.quit()
    return content


@app.get("/scrape")
def scrape():
    content = run_playwright()
    return {"content": content}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)