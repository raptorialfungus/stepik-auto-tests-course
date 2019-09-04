from selenium import webdriver
import time

try: 
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link1)

    browser.find_element_by_css_selector(".first_block input.first").send_keys("FirstName")
    browser.find_element_by_css_selector(".first_block input.second").send_keys("LastName")
    browser.find_element_by_css_selector(".first_block input.third").send_keys("Email")
    browser.find_element_by_css_selector(".second_block input.first").send_keys("Phone")
    browser.find_element_by_css_selector(".second_block input.second").send_keys("Address")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
