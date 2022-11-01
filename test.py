from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.com/")
location_button = driver.find_element(By.CLASS_NAME, 'glow-toaster-button-dismiss')
location_button.click()
search_bar = driver.find_element(By.ID, 'twotabsearchtextbox')
search_bar.clear()
search_bar.send_keys("computer")
search_bar.send_keys(Keys.RETURN)
selected_item = driver.find_element(By.XPATH, '//*[contains(text(), "HP Elite Desktop PC Computer")]')
driver.execute_script("arguments[0].scrollIntoView();",selected_item)
selected_item.click()
quantity_button = driver.find_element(By.ID, 'a-autoid-0')
quantity_button.click()
total_quantity = driver.find_element(By.ID, 'quantity_9')
total_quantity.click()
add_to_cart = driver.find_element(By.ID, 'add-to-cart-button')
add_to_cart.click()

try:
    WebDriverWait(driver, 9).until(EC.presence_of_element_located((By.ID, 'attach-view-cart-button-form')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

cart_button = driver.find_element(By.XPATH, "//input[@aria-labelledby='attach-sidesheet-view-cart-button-announce']")
driver.implicitly_wait(10)
cart_button.click()
delete_link = driver.find_element(By.XPATH, '//input[@aria-label="Delete HP Elite Desktop PC Computer Intel Core i5 3.1-GHz, 8 gb Ram, 1 TB Hard Drive, DVDRW, 19 Inch LCD Monitor, Keyboard, Mouse, Wireless WiFi, Windows 10 (Renewed)"]')
delete_link.click()

text = driver.find_element(By.XPATH, "//h1[@class='a-spacing-mini a-spacing-top-base']").text
print(text, text == "Your Amazon Cart is empty." )

driver.quit()