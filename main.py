"""
1. Open the browser (Chrome/Firefox/Edge)
2. Open URL (Test Automation Practice)
3. Enter every details

"""
import time

from requests.hooks import HOOKS
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core.driver import Driver

driver = webdriver.Firefox()

# For maximizing the window
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
# driver.find_element(By.XPATH, "//input[@id='email']/preceding::input").send_keys("Sadikshya")
# driver.find_element(By.XPATH, "//input[@id='name']/following::input[1]").send_keys("acharya.sadikshya33@gmail.com")
# driver.find_element(By.XPATH, "//input[@id='email']/following::input[1]").send_keys("9876543210")
# driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("Lalitpur")
# driver.find_element(By.XPATH, "//textarea[@id='textarea']/following::input[2]").click()
#
# body = driver.find_element("tag name", "body")
# # body.send_keys(Keys.PAGE_DOWN)
#
# # Locator of Male Radio Button
# # //textarea[@id='textarea']/following::input[1]
#
# # Checking all the checkboxes at once
# # checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# #
# # # Using Loop
# # for checkbox in checkboxes:
# #     if not checkbox.is_selected():
# #         checkbox.click()
#
#
# checkbox = driver.find_element(By.XPATH, "//div[@class='form-check form-check-inline' and input[@id='friday']]").click()
#
# # body = driver.find_element("tag name","body")
# # body.send_keys(Keys.PAGE_DOWN)
#
# # Scroll down multiple times
# for _ in range(1):  # Change 3 to however many times you want to scroll
#     body.send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)  # Wait a bit to let content load
#
# #  Creating a select object
# dropdown_element = driver.find_element(By.XPATH, "//select[@id='country']")
# dropdown_element.click()
# select = Select(dropdown_element)
#
# # 1. Select by visible text
# select.select_by_visible_text("Canada")
#
# # Select by value attribute
# # select.select_by_value("canada")
#
# # Select by index ( 0 based)
# # select.select_by_index(1)
#
# # body = driver.find_element(By.TAG_NAME, "body")
# #
# # for _ in range(1):
# #     body.send_keys(Keys.PAGE_DOWN)
# #     time.sleep(1)
#
# scroll_bar_color = driver.find_element(By.XPATH, "//select[@id='colors']")
#
# select = Select(scroll_bar_color)
# select.select_by_value("white")
#
# # select.select_by_visible_text("Green")
# # select.select_by_index(6)
#
# scroll_bar_sortedList = driver.find_element(By.XPATH, "//select[@id='animals']")
# select = Select(scroll_bar_sortedList)
# select.select_by_value("elephant")
#
# # Date Picker: 1
# date_picker1 = driver.find_element(By.XPATH, "//input[@id='txtDate']/preceding::input[1]")
# date_picker1.click()
# date_chosen = driver.find_element(By.XPATH, "//a[@data-date='3']")
# date_chosen.click()
# time.sleep(1)
#
# date_value = date_picker1.get_attribute("value")
#
# # #  Assertions to confirm if date has been picked
# # assert date_value !="", "Date was not picked!!!"
#
# expectedDate= "05/03/2025"
# assert date_value == expectedDate, f"Expected Date {expectedDate}, but got {date_value}"
#
#
# # Date Picker: 2
# date_picker2 =driver.find_element(By.XPATH,"//input[@id='datepicker']/following::input[1]")
# date_picker2.click()
# time.sleep(1)
# date_picker_month = driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']")
# date_picker_month.click()
# select = Select(date_picker_month)
# time.sleep(1)
# select.select_by_value("0")
# select_year = driver.find_element(By.XPATH, "//select[@data-handler='selectYear']")
# select = Select(select_year)
# time.sleep(1)
# select.select_by_value("2018")
# time.sleep(1)
# date_picker_day = driver.find_element(By.XPATH, " //a[@data-date='13']")
# date_picker_day.click()
#
# date_value = date_picker2.get_attribute("value")
# assert date_value != "", "Date was not picked !!!"

#  Date Picker: 3 (mm/dd/yyyy)

# date_picker3 = driver.find_element(By.XPATH, "//input[@placeholder='Start Date']")
# date_picker3.clear()
# date_picker3.click()
# time.sleep(5)
# date_picker3.send_keys("05/02/2025")


#
# date_value = date_picker3.get_attribute("value")
# # assert date_value != "", "Date was not picked !!!"
# assert date_value == "05/02/2025", f"Expected date not picked! Got: {date_value}"

#  Upload File
# 1. Single File

# singleFile_upload = driver.find_element(By.XPATH, "//input[@id='singleFileInput']")
# singleFile_upload.click()
#
# file_name = "Remaining Sections"
# singleFile_upload.send_keys(file_name)
#
# uploadSingleFileButton = driver.find_element(By.XPATH, "//button[text()='Upload Single File']")
# uploadSingleFileButton.click()


# uploadButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='singleFileInput']")))
# WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@id='singleFileInput']")))
# uploadButton.send_keys("C:\\Users\\Sadikshya_Acharya\\Documents\\Remaining_Sections.txt")
# driver.find_element(By.XPATH, "//button[text()='Upload Single File']").click()

# Pagination Web Table
#
# for i in range(2):
#     body = driver.find_element(By.TAG_NAME, "body")
#     body.send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)

for i in range(3):
    driver.execute_script("window.scrollBy(0, window.innerHeight);")
    time.sleep(1)


checkBox1 = driver.find_element(By.XPATH, "//table//tr[1]//input[@type='checkbox'][1]")
checkBox1.click()

assert checkBox1.is_selected(), "Checkbox was not clicked!"

assert checkBox1.is_displayed(), "Checkbox is not visible on the page."
print("Checkbox was successfully clicked and is visible.")


#  Pagination
pagination2 = driver.find_element(By.XPATH, "//a[text()='2']")
pagination2.click()

# assert pagination2.is_selected(), "pagination 2 is not clicked!"
assert pagination2.is_displayed(), "Pagination 2.... is not displayed"
print("Pagination 2 is successfully checked and displayed.")


checkbox3Page2= driver.find_element(By.XPATH, "//table//tr[3]//input[@type='checkbox'][1]")
checkbox3Page2.click()

assert checkbox3Page2.is_selected(), "Checkbox2 was not clicked!"
# driver.quit()

pagination3 = driver.find_element(By.XPATH, "//a[text()=2]/following::a[1]")
pagination3.click()
time.sleep(1)

assert pagination3.is_displayed(), "Pagination 3 is not selected!"
checkbox4Page3 = driver.find_element(By.XPATH, "//table//tr[2]//input[@type='checkbox'][1]")
checkbox4Page3.click()
checkbox4Page3.is_selected(), "Checkbox was not selected!"

#  Form Section 1

# section1form = driver.find_element(By.XPATH, "//div[@id='section1']/descendant::input")
# section1form.send_keys("Nepal is a small, landlocked country located in South Asia, nestled between China and India. "
#                        "Known for its stunning natural beauty, it is home to eight of the world’s ten highest mountains, including Mount Everest, the tallest peak on Earth. "
#                        "Nepal is rich in cultural heritage, with diverse ethnic groups, languages, and religions coexisting peacefully. "
#                        "The capital city, Kathmandu, is famous for its historic temples and vibrant traditions. "
#                        "Despite being a developing nation, Nepal draws global attention for its breathtaking landscapes and deep-rooted spiritual culture.")
#
# # Submit Button
# submitButton = driver.find_element(By.XPATH, "//div[@id='section1']/descendant::button")
# submitButton.click()
# section1form.is_displayed(), "Paragraph is not displayed"

#  Form Section 2

# section2form = driver.find_element(By.XPATH, "//div[@id='section1']/following::input[1]")
# section2form.send_keys("Nepal is a small, landlocked country located in South Asia, nestled between China and India. "
#                        "Known for its stunning natural beauty, it is home to eight of the world’s ten highest mountains, including Mount Everest, the tallest peak on Earth. "
#                        "Nepal is rich in cultural heritage, with diverse ethnic groups, languages, and religions coexisting peacefully. "
#                        "The capital city, Kathmandu, is famous for its historic temples and vibrant traditions. "
#                        "Despite being a developing nation, Nepal draws global attention for its breathtaking landscapes and deep-rooted spiritual culture.")
#
# # Submit Button
# submitButton = driver.find_element(By.XPATH, "//div[@id='section1']/following::button[1]")
# submitButton.click()
# section2form.is_displayed(), "Paragraph is not displayed"

#  Footer Links
# old_url = driver.current_url
#
# homeLink = driver.find_element(By.XPATH, "//div[@id='PageList1']/descendant::a[1]")
# homeLink.click()
#
# #  Wait for the URL to change
# WebDriverWait(driver, 10).until(lambda d:d.current_url != old_url)
# print("Page navigated or refreshed (URL changed).")

#
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.support.ui import WebDriverWait
#
# def is_stale(element):
#     try:
#         element.is_displayed()
#         return False
#     except StaleElementReferenceException:
#         return True
#
# # Store a known element before the click
# body = driver.find_element(By.TAG_NAME, "body")
#
# # Click the Home link
# homeLink = driver.find_element(By.XPATH, "//div[@id='PageList1']/descendant::a[1]")
# homeLink.click()
#
# # Wait until the DOM element goes stale (which means the page reloaded)
# WebDriverWait(driver, 10).until(lambda d: is_stale(body))
#
# print("Page was refreshed (DOM was reloaded).")


#  Hidden Elements and AJAX

# old_url = driver.current_url
# heaLink = driver.find_element(By.XPATH, "//div[@id='PageList1']/descendant::a[2]")
# heaLink.click()
#
# time.sleep(2)
# new_url = driver.current_url
#
# assert new_url != old_url, "URL Matches!!!"

for i in range(2):
  body = driver.find_element("tag name", "body")
  body.send_keys(Keys.PAGE_DOWN)

#  Dynamic Button
# dynamicButton = driver.find_element(By.XPATH, "//button[starts-with(@name, 'st')]")
# dynamicButton.click()

button = driver.find_element(By.XPATH, "//button[contains(@name, 'start')]")


# After clicking, class and name changes

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(@name, 'stop')]")))
stop_button = driver.find_element(By.XPATH, "//button[contains(@class, 'stop')]")
stop_button.click()

