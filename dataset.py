from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import urllib.request
import time
import os

def download_image(image_name, src, seq, dir):
    try:
        filename = image_name + str(seq) + '.jpg'
        image_path = os.path.abspath(os.path.join(os.getcwd(), dir, filename))
        urllib.request.urlretrieve(src, image_path)
    except Exception:
        pass

def browse_page(url, image_name, pages, dir):
    seq = 0
    for i in range(pages):
        try:
            driver.get(f"{url}{i+1}")
            time.sleep(2)
            images = driver.find_elements("xpath", "//picture/source")
        except:
            continue

        for image in images:
            try:
                src = image.get_attribute('srcset')
                # print(src)
                download_image(image_name, src, seq, dir) 
            except:
                pass
            seq += 1
        time.sleep(2)

if __name__ == '__main__':
    image_name = '90s'
    url = 'https://www.gettyimages.com/photos/image-archive-90s?assettype=image&phrase=image%20archive%2090s&sort=mostpopular&license=rf&page='
    dir = '/content/images'
    pages = 100
    chrome_service = Service(executable_path='/content/chromedriver-linux64/chromedriver')
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)    
    driver.maximize_window()
    if not os.path.isdir(dir):
        os.makedirs(dir)
    browse_page(url, image_name, pages, dir)