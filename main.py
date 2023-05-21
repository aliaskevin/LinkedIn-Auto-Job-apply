from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

email_id = os.environ.get("email")
password = os.environ.get("password")

driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102713980&"
           "keywords=environmental%20engineer&location=India&refresh=true")
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Sign in").click()
time.sleep(3)
user = driver.switch_to.active_element
user.send_keys(email_id)
user.send_keys(Keys.TAB)
pass_entry = driver.switch_to.active_element
pass_entry.send_keys(password)
pass_entry.send_keys(Keys.ENTER)
time.sleep(7)

job_list = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container .job-card-list__entity-lockup")
for job in job_list:
    job.click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button").click()
    time.sleep(3)
    # phone = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
    # phone.send_keys("9446024365")
    # driver.find_element(By.CSS_SELECTOR, "footer button").click()
    # time.sleep(3)
    try:
        driver.find_element(By.LINK_TEXT, "Submit application").click()
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
    except NoSuchElementException:
        driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
        driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn").click()
