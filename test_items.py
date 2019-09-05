from selenium import webdriver
import pytest
import time

def test_should_see_basket_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(10)
    browser.get(link)
    # time.sleep(30)
    assert browser.find_elements_by_css_selector("button.btn-add-to-basket"), "Add to basket button is absent"
