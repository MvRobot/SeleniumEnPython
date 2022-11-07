from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")
time.sleep(1)
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("HP Pavilon Azul")
time.sleep(1)
driver.find_element(By.ID, "nav-search-submit-button").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[@data-component-id='3']/a[1]").click()
time.sleep(1)
driver.find_element(By.ID, "quantity").send_keys("2")
driver.find_element(By.ID, "add-to-cart-button").click()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Ir al Carrito').click()
time.sleep(1)
driver.close()
print("Prueba completada")


