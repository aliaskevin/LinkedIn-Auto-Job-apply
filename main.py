from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
# Linked credentials
email_id = os.environ.get("email")
password = os.environ.get("password")
# Setting up Selenium
driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102713980&"
           "keywords=environmental%20engineer&location=India&refresh=true")
# Use sleep time to give time for browser to load elements
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Sign in").click()
time.sleep(3)
# Signing in to LinkedIn
user = driver.switch_to.active_element
user.send_keys(email_id)
user.send_keys(Keys.TAB)
pass_entry = driver.switch_to.active_element
pass_entry.send_keys(password)
pass_entry.send_keys(Keys.ENTER)
time.sleep(7)
# Finding all elemnts of all job listed on the page
job_list = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container .job-card-list__entity-lockup")
# Clicking apply to all single step job application
for job in job_list:
    job.click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button").click()
    time.sleep(3)
    # Below commented stepts are to add contact number if not filled
    # phone = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
    # phone.send_keys("9446024365")
    # driver.find_element(By.CSS_SELECTOR, "footer button").click()
    # time.sleep(3)
    try:
        driver.find_element(By.LINK_TEXT, "Submit application").click()
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
    # below steps are to close the application if there are multiple steps
    except NoSuchElementException:
        driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
        driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn").click()
