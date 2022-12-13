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

# GO TO https://qatest.schoox.com/6/steps
driver.find_element(By.CSS_SELECTOR, "a[href='/training']").click()
driver.find_element(By.CSS_SELECTOR, "a[href='/6/steps']").click()

# ENROLL TO THE COURSE
driver.find_element(By.CSS_SELECTOR, ".enroll").click()

# COMPLETE ALL THE STEPS
step_list = ["1", "2", "3", "4"]
for step in step_list:
    driver.find_element(By.XPATH, "(//b[text()='Complete'])["+step+"]").click()
    alert = driver.switch_to.alert
    alert.accept()

# VALIDATE PROGRESS IS 100%
progress = driver.find_element(By.XPATH, "//div[@class='top_course_progress']").text
assert progress == 'Course Progress: 100.00%'

