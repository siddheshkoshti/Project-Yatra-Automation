import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class BaseDriver():
    def __init__(self, driver, wait):
        self.wait = wait
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)


    def page_scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)

    def wait_for_presence_of_all_elments(self,locator_type, locator):
        # wait = WebDriverWait(driver, 20)

        list_of_elements = self.wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        return list_of_elements

    def wait_element_is_clickble(self, locator_type, locator):
        # wait = WebDriverWait(driver, 20)

        element = self.wait.until(EC.element_to_be_clickable((locator_type,locator)))
        return element



