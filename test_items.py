from selenium import webdriver
import pytest
import math
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.set_page_load_timeout(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, url):
    link = f"https://stepik.org/lesson/{url}/step/1"
    browser.get(link)
    answer = str(math.log(int(time.time())))
    browser.find_element_by_css_selector(".quiz-component textarea").send_keys(answer)
    browser.find_element_by_css_selector("button.submit-submission").click()
    time.sleep(3)
    assert browser.find_element_by_css_selector(".smart-hints__hint").text == "Correct!", "Test failed"
