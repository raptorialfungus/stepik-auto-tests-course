from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("input:nth-child(2)").send_keys("FirstName")
    browser.find_element_by_css_selector("input:nth-child(4)").send_keys("LastName")
    browser.find_element_by_css_selector("input:nth-child(6)").send_keys("Email")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element_by_css_selector("input[type='file']").send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    #    browser.quit()

