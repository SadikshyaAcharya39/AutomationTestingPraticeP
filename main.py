"""
1. Open the browser (Chrome/Firefox/Edge)
2. Open URL (Test Automation Practice)
3. Enter every details

"""
import time
from locale import windows_locale

from requests.hooks import HOOKS
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
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
# body.send_keys(Keys.PAGE_DOWN)
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
# #
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
#
# #  Date Picker: 3 (mm/dd/yyyy)
#
# # date_picker3 = driver.find_element(By.XPATH, "//input[@placeholder='Start Date']")
# # date_picker3.clear()
# # date_picker3.click()
# # time.sleep(5)
# # date_picker3.send_keys("05/02/2025")
# #
# # date_value = date_picker3.get_attribute("value")
# # assert date_value != "", "Date was not picked !!!"
# # assert date_value == "05/02/2025", f"Expected date not picked! Got: {date_value}"

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
#
#
# uploadButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='singleFileInput']")))
# WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@id='singleFileInput']")))
# uploadButton.send_keys("C:\\Users\\Sadikshya_Acharya\\Documents\\Remaining_Sections.txt")
# driver.find_element(By.XPATH, "//button[text()='Upload Single File']").click()


# # Wait until the file input is clickable
# file_input = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@id='singleFileInput']"))
# )
#
# # Send the full file path to the file input element
# file_path = r"C:\Users\Sadikshya_Acharya\Documents\Remaining_Sections.txt"
# file_input.send_keys(file_path)
#
# # Click the "Upload" button
# upload_button = driver.find_element(By.XPATH, "//button[text()='Upload Single File']")
# upload_button.click()

# # Pagination Web Table
#
# for i in range(2):
#     body = driver.find_element(By.TAG_NAME, "body")
#     body.send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)
#
# for i in range(3):
#     driver.execute_script("window.scrollBy(0, window.innerHeight);")
#     time.sleep(1)
#
#
# checkBox1 = driver.find_element(By.XPATH, "//table//tr[1]//input[@type='checkbox'][1]")
# checkBox1.click()
#
# assert checkBox1.is_selected(), "Checkbox was not clicked!"
#
# assert checkBox1.is_displayed(), "Checkbox is not visible on the page."
# print("Checkbox was successfully clicked and is visible.")
#
#
# #  Pagination
# pagination2 = driver.find_element(By.XPATH, "//a[text()='2']")
# pagination2.click()
#
# # assert pagination2.is_selected(), "pagination 2 is not clicked!"
# assert pagination2.is_displayed(), "Pagination 2.... is not displayed"
# print("Pagination 2 is successfully checked and displayed.")
#
#
# checkbox3Page2= driver.find_element(By.XPATH, "//table//tr[3]//input[@type='checkbox'][1]")
# checkbox3Page2.click()
#
# assert checkbox3Page2.is_selected(), "Checkbox2 was not clicked!"
# # driver.quit()
#
# pagination3 = driver.find_element(By.XPATH, "//a[text()=2]/following::a[1]")
# pagination3.click()
# time.sleep(1)
#
# assert pagination3.is_displayed(), "Pagination 3 is not selected!"
# checkbox4Page3 = driver.find_element(By.XPATH, "//table//tr[2]//input[@type='checkbox'][1]")
# checkbox4Page3.click()
# checkbox4Page3.is_selected(), "Checkbox was not selected!"
#
#  # Form Section 1
#
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
#
#  # Form Section 2
#
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
#
#  # Footer Links
# old_url = driver.current_url
#
# homeLink = driver.find_element(By.XPATH, "//div[@id='PageList1']/descendant::a[1]")
# homeLink.click()
#
# #  Wait for the URL to change
# WebDriverWait(driver, 10).until(lambda d:d.current_url != old_url)
# print("Page navigated or refreshed (URL changed).")
#
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
#
#
# #  Hidden Elements and AJAX
#
# old_url = driver.current_url
# heaLink = driver.find_element(By.XPATH, "//div[@id='PageList1']/descendant::a[2]")
# heaLink.click()
#
# time.sleep(2)
# new_url = driver.current_url
#
# assert new_url != old_url, "URL Matches!!!"
#
# for i in range(2):
#   body = driver.find_element("tag name", "body")
#   body.send_keys(Keys.PAGE_DOWN)
#
#  # Dynamic Button
# dynamicButton = driver.find_element(By.XPATH, "//button[starts-with(@name, 'st')]")
# dynamicButton.click()
#
# button = driver.find_element(By.XPATH, "//button[contains(@name, 'start')]")
# original_class = button.get_attribute("id")
# original_name = button.get_attribute("class")
#
# button.click()
#
#
# # After clicking, class and name changes
#
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//button[contains(@name, 'stop')]")))
# updated_button = driver.find_element(By.XPATH, "//button[contains(@class, 'stop')]")
# new_name = button.get_attribute("name")
# new_class = button.get_attribute("class")
#
# # Assertions
# assert original_name != new_name, "Name did not change"
# assert original_class != new_class, "Class did not change"
#
# print("Button transitioned stated: Name and Class all changed as expected")
#
# #  Handling Alerts and Popups
# #  Simple Alert
#
# alert1 = driver.find_element(By.XPATH, "//button[@id='alertBtn']")
# alert1.click()
#
# time.sleep(1)
#
# # Switch to alert
# alert1 = driver.switch_to.alert
#
# print("Alert says: " , alert1.text)
#
# alert1.accept()
#
#  Alert2
#  Confirmation Alert

alert2 = driver.find_element(By.XPATH, "//button[@id='confirmBtn']")
alert2.click()

# Switching to Alert
alert2 = driver.switch_to.alert
# alert2.accept()

alert2.dismiss()
message = driver.find_element(By.XPATH, "//p[@id='demo']")
message.is_displayed()

body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.PAGE_DOWN)

# Alert 3
# Prompt Alert

alert3 = driver.find_element(By.XPATH, "//button[@id='promptBtn']")
alert3.click()

# Switching to Alert
alert = driver.switch_to.alert
alert.send_keys("Sadikshya!")
# alert.accept()
alert.dismiss()

# New Tab

# Storing the number of original tabs
original_tabs = driver.window_handles
original_tab_count = len(original_tabs)

newTab_button = driver.find_element(By.XPATH, "//button[text()='New Tab']")
newTab_button.click()

updated_tabs = driver.window_handles
updated_tab_count = len(updated_tabs)

# Assertions
assert updated_tab_count > original_tab_count, "New tab was not opened!"
print("New tab opened successfully...")

# Switching to a new tab
driver.switch_to.window(updated_tabs[-1])

# Handling Popup Windows

# Selenium treats both tabs and pop up windows in same way

 # Current window handles
original_window = driver.window_handles
original_count = len(original_window)


popUp_window = driver.find_element(By.XPATH, "//div[@class='column']")
popUp_window.click()
time.sleep(2)


new_windows = driver.window_handles
new_count = len(new_windows)
#
# # Assertions
assert new_count > original_count, "Pop-up window did not open"
print("New window opened successfully")

body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.PAGE_DOWN)
body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.PAGE_DOWN)

# Handling Mouse Hover
point_me_button = driver.find_element(By.XPATH, "//div[@class='dropdown']")
driver.execute_script("arguments[0].scrollIntoView(true);", point_me_button)

# Wait until the element is visible
WebDriverWait(driver, 10).until(EC.visibility_of(point_me_button))

# Using ActionChain Object
actions = ActionChains(driver)
actions.move_to_element(point_me_button).perform()

mobiles_button = driver.find_element(By.XPATH, "//a[text()='Mobiles']")
mobiles_button.click()

# Handling Drag and Drop

drag_locator = driver.find_element(By.XPATH, "//p[text()='Drag me to my target']")

droppable_locator = driver.find_element(By.XPATH, "//div[@id='droppable']")

driver.execute_script("arguments[0].scrollIntoView(true);", drag_locator)
driver.execute_script("arguments[0].scrollIntoView(true);", droppable_locator)

# Creating action chain object and perform drag and drop
actions = ActionChains(driver)
actions.drag_and_drop(drag_locator, droppable_locator).perform()

#  Getting the value of Static Web Table

for i in range(2):
 body = driver.find_element(By.TAG_NAME, "body")
 body.send_keys(Keys.PAGE_DOWN)

web_table = driver.find_element(By.XPATH, "//div[@id='HTML1']")
assert web_table.is_displayed(), "Static Web Table is not displayed.."

# Book Name
book_name = driver.find_element(By.XPATH, "//table//tr[4]/td[contains(text(), 'Learn JS')]")
assert book_name.is_displayed(), "Book name is not displayed.."
print(book_name.text)

# Author
author_name = driver.find_element(By.XPATH, "//table//tr[5]/td[contains(text(), 'Mukesh')]")
assert author_name.is_displayed(), "Author name is not displayed.."
print(author_name.text)

# Subject
subject_name = driver.find_element(By.XPATH, "//table//tr[7]/td[contains(text(), 'Javascript')]")
assert subject_name.is_displayed(), "Subject name is not displayed.."
print(subject_name.text)

# Price
price = driver.find_element(By.XPATH, "//table//tr[5]/td[contains(text(), '3000')]")
assert price.is_displayed(), "price is not displayed.."
print(price.text)

#  Verify the number of rows and columns
#  Using Web Table

web_table = driver.find_elements(By.XPATH, "//table[@name='BookTable']")

# Access the first table in the list
first_table = web_table[0]

rows = first_table.find_elements(By.TAG_NAME, "tr")
print("Total number of rows: " , len(rows))

header_column = rows[0].find_elements(By.TAG_NAME, "th")
print("Total number of columns: " , len(header_column))

# Using Loop
# web_tables = driver.find_elements(By.XPATH, "//table[@name='BookTable']")
# for table in web_tables:
#     rows = table.find_elements(By.TAG_NAME, "tr")
#     print("Rows in table:", len(rows))

#  Scrolling Drop Down
scrolling_dropdown = driver.find_element(By.XPATH, "//input[@id='comboBox']")
scrolling_dropdown.click()

items = driver.find_elements(By.XPATH, "//div[@id='dropdown']/div")
 # Can't use select because dropdown is not using Select tag.

select = Select(items)

#  By visible text
select.select_by_visible_text("Item 97")
scrolling_dropdown.is_displayed(), "Selected Item is not displayed.."
#

#  Using Loop
for item in items:
    if(item.text == 'Item 97'):
       item.click()
       break

# Verify that the item is selected
assert scrolling_dropdown.is_displayed(), "Dropdown is not displayed."


# SVG Elements

svg_container = driver.find_element(By.XPATH, "//div[@class='svg-container']")

circle = driver.find_element(By.XPATH, "//*[local-name()='svg']//*[local-name()='circle']")
circle.is_displayed(), "Circle is not displayed.."

assert circle.get_attribute("cx") == 15  # is incorrect
assert circle.get_attribute("cy") == 15
assert circle.get_attribute("r") == 7

rectangle = driver.find_element(By.XPATH, "//*[local-name()='svg']//*[local-name()='rect']")
rectangle.is_displayed(), "Rectangle is not displayed.."

assert int(rectangle.get_attribute("x")) == 3
assert int(rectangle.get_attribute("y")) == 5
assert int(rectangle.get_attribute("width")) == 24
assert int(rectangle.get_attribute("height")) == 5  # is incorrect

# Slider
# Price Range

# Original Range

original_price_range = driver.find_element(By.XPATH, "//input[@id='amount']").get_attribute("value")

# price_range = driver.find_element(By.XPATH, "//div[@class='ui-slider-range ui-corner-all ui-widget-header']")

slider1 = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default'][1]")


slider2 = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default'][2]")

 # Using action chain object
actions = ActionChains(driver)
actions.click_and_hold(slider1).move_by_offset(50,0).release().perform()
actions.click_and_hold(slider2).move_by_offset(0, 50).release().perform()

changed_price = driver.find_element(By.XPATH, "//input[@id='amount']").get_attribute("value")
assert original_price_range != changed_price, "Original price range is equal to changed price"


 # Double Click

textfield1 = driver.find_element(By.XPATH, "//input[@id='field1']")
value1 = textfield1.get_attribute("value")

# copy_text_button = driver.find_element(By.XPATH, "//button[text()='Copy Text']")

copy_text_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Copy Text']"))
)

# Scroll the button into view
driver.execute_script("arguments[0].scrollIntoView(true);", copy_text_button)

actions = ActionChains(driver)
actions.double_click(copy_text_button).perform()


# Wait or sleep briefly if DOM updates asynchronously
WebDriverWait(driver, 5).until(
    lambda d: d.find_element(By.XPATH, "//input[@id='field2']").get_attribute("value") != ""
)


textfield2 = driver.find_element(By.XPATH, "//input[@id='field2']")
assert textfield1.get_attribute("value") == textfield2.get_attribute("value"), "Text was not copied!!!"

textfield1 = driver.find_element(By.XPATH, "//input[@id='field1']")
full_text = textfield1.get_attribute("value")

trimmed_text = full_text.split(" ")[0]
print(trimmed_text)

textfield1.clear()
textfield1.send_keys(trimmed_text , " Sadikshya ")


 # Hidden Elements and AJAX
original_url = driver.current_url

link_text = driver.find_element(By.XPATH, "//a[text()='Hidden Elements & AJAX']")
link_text.click()

changed_url = driver.current_url

assert original_url != changed_url, "Original URL should not be same as Changed URL.."
time.sleep(5)


input_box2 = driver.find_element(By.XPATH, "//button[@id='toggleInput']")
input_box2.is_enabled(), "Input box2 is not enabled!"

input_box2.click()
time.sleep(3)

input2box = driver.find_element( By.XPATH , "//input[@id='input2']")
input2box.is_displayed(), "Is not displayed!!!"

# Toogle CheckBox button
checkbox_button = driver.find_element(By.XPATH, "//button[@id='toggleCheckbox']")
checkbox_button.click()

checkbox = driver.find_element(By.XPATH, "//input[@id='checkbox2']")
assert checkbox.is_displayed(), "Is not displayed.."










