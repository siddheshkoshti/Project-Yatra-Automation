from selenium.webdriver.common.by import By

from pythonProject1.base.base_driver import BaseDriver
from selenium.webdriver.support import expected_conditions as EC


class SearchFlightResults(BaseDriver):
    def __init__(self,driver,wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait


    def filter_flights(self):
        # allstops = self.wait.until(EC.presence_of_all_elements_located(
        #     (By.XPATH, "//*[@id='Flight-APP']/section/section[1]/div/div[1]/div/div[2]/div[2]")))
        self.driver.find_element(By.XPATH, "//p[normalize-space()='1']").click()

        allstops = self.wait_for_presence_of_all_elments(By.XPATH, "//*[@id='Flight-APP']/section/section[1]/div/div[1]/div/div[2]/div[2]")
        print((len(allstops)))
