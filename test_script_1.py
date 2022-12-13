from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("https://github.com/EllieZacharelou/SchooxProject/blob/master/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("http://qatest.schoox.com/login")

# LOGIN
driver.find_element(By.CSS_SELECTOR, "div input[type='email']").send_keys("admin@schoox.com")
driver.find_element(By.CSS_SELECTOR, "div input[type='password']").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "button").click()

# GO TO TRAINING
driver.find_element(By.CSS_SELECTOR, "a[href='/training']").click()

# CHOOSE QA CATEGORY
driver.find_element(By.XPATH, "//div[@class='category_item'][1]").click()

# VALIDATE LISTS CONTENTS
items = driver.find_elements(By.XPATH, "//tr")
courses = []
for item in items:
    courses.append(item.find_element(By.XPATH, "td/a").text)
assert courses == ["QA course", "ΒΑ course", "Μάθημα για τους Devs", "Μάθημα για automation"]

