from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3446096519&f_AL=true&f_E=1%2C2&f_WT=2&geoId=103644278&keywords=jr%20python%20developer&location=United%20States&refresh=true"

options = Options()
options.add_experimental_option("detach", True)
chrome_driver_path = r"YOUR CHROME DRIVER PATH"
driver = webdriver.Chrome(options=options)
driver.get(URL)
driver.implicitly_wait(3)
sign_in = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
username = driver.find_element(By.ID, value="username")
username.send_keys("jacobb135@gmail.com")
password = driver.find_element(By.ID, value="password")
password.send_keys("Rincon1!")
sign_in_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()
time.sleep(2)
first_job = driver.find_element(By.CSS_SELECTOR, value="div .job-card-container")
time.sleep(2)
first_job.click()
easy_apply = driver.find_element(By.CSS_SELECTOR, value="div .jobs-s-apply")
time.sleep(2)
easy_apply.click()
choose_button = driver.find_element(By.CSS_SELECTOR, value="footer button")
if choose_button.text == "Next":
    skip = driver.find_element(By.CSS_SELECTOR, value="button")
    skip.click()
    time.sleep(1)
    discard = driver.find_element(By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")
    discard.click()


