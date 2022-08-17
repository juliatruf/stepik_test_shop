from selenium.webdriver.common.by import By
import time

def is_element_present(browser):
    try:
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        #time.sleep(30)
        browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        return True
    except:
        return False

def test_user_should_see_bin_button(browser):
    assert is_element_present(browser)==True, "There is no 'Bin' button"