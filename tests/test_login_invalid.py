from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome()  

try:
    driver.get("https://the-internet.herokuapp.com/login")

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    username.send_keys("yanlisKullanici")
    password.send_keys("yanlisSifre")
    password.send_keys(Keys.RETURN)

    time.sleep(2)

    error_message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in error_message.strip()

    screenshot_path = os.path.join(os.getcwd(), "test-sonucu.png")
    driver.save_screenshot(screenshot_path)

    print(" Test başarılı, ekran görüntüsü alındı.")

except AssertionError:
    print(" Test başarısız: Hata mesajı beklenildiği gibi değil.")

except Exception as e:
    print(f" Bir hata oluştu: {e}")

input(" İncelemek için ENTER'a bas...")

