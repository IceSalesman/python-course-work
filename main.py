from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json

service = Service()
option = webdriver.ChromeOptions()
option.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=service, options=option)


name = input("Ievadiet konvērtējamo vārdu: ")

url = "https://minecraft-serverlist.com/tools/offline-uuid"
driver.get(url)
delay = 5


find = WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.CLASS_NAME, "cookies__cta")))
find.click()
find = WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.ID, "uuids")))
find.click()
find.send_keys(name)

find = driver.find_element(By.CLASS_NAME, "btn--green")
find.click()

if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[-1])
    
find = WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.TAG_NAME, "pre")))
json_text = find.text

data = json.loads(json_text)
uuid = data["players"][0]["uuid"]

print(uuid)