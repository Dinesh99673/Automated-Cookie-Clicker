from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions object to keep the browser window open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Launch Chrome browser with specified options
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Locate the cookie button element
click = driver.find_element(By.ID, value='cookie')

# List of store item IDs in increasing order of cost
store_items = [
    "buyCursor", "buyGrandma", "buyFactory", "buyMine",
    "buyShipment", "buyAlchemy", "buyPortal", "buyTime"
]

# Main loop runs 20 times (you can change it to run for more longer time)
for i in range(20):
    # Click cookie continuously for 20 seconds
    end_time = time.time() + 20
    while time.time() < end_time:
        click.click()

    # Get the current number of cookies available
    cookie_value = driver.find_element(By.ID, value='money').text

    # Try to buy the most expensive item affordable
    idx = 0
    while idx < 8:
        storePrice = driver.find_element(By.XPATH,value=f'//*[@id="{store_items[idx]}"]/b').text
        temp = storePrice.split()
        print(temp)
        amount = int(temp[2].replace(",",""))
        if amount > int(cookie_value.replace(",","")):
            break
        idx += 1
    # Purchase the most expensive item that is still affordable
    if idx > 0:
        buy_item = driver.find_element(By.ID, value=store_items[idx - 1])
        buy_item.click()

#To close the browser window after execution (You can comment it if you don't want to close the window)
driver.quit()