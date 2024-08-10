from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests
from PIL import Image
from io import BytesIO

def download_images(query, num_images=100, folder_path='images'):
    # Create folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Launch Chrome browser using WebDriver
    driver = webdriver.Chrome()

    # Google Images URL
    url = "https://www.google.com/search?tbm=isch&q=" + query

    # Open Google Images
    driver.get(url)

    # Wait for images to load
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//img[@class='rg_i Q4LuWd']")))
    except Exception as e:
        print("Error: Timeout waiting for images to load.")
        driver.quit()
        return

    # Find and download images
    images = driver.find_elements_by_xpath("//img[@class='rg_i Q4LuWd']")
    for i, image in enumerate(images[:num_images]):
        try:
            image_url = image.get_attribute('src')
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            img.save(os.path.join(folder_path, f"{query}_{i+1}.jpg"))
            print(f"Downloaded image {i+1}/{num_images}")
        except Exception as e:
            print(f"Error downloading image {i+1}: {e}")

    # Close browser
    driver.quit()

if __name__ == "__main__":
    query = "apple pie"
    num_images = 100
    folder_path = 'images'

    download_images(query, num_images, folder_path)
