import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC, wait

from selenium.webdriver.common.by import By

from pythonProject1.base.base_driver import BaseDriver
from selenium.webdriver.support.ui import WebDriverWait


class LaunchPage(BaseDriver ):
    def __init__(self,driver,wait):
        super().__init__(driver,wait)
        self.driver = driver
        self.wait = wait

    # locator
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOINT_TO_RESULT_LIST = "/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/input[1]"
    SEARCH_BUTTON = "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']"
    def getDepartFromField(self,):
        return self.wait_element_is_clickble(By.XPATH, self.DEPART_FROM_FIELD)

    def enterDepartFromLocation(self,departlocation ):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        # self.getDepartFromField().send_keys(Keys.ENTER)

    # def departfrom(self,departlocation):
    #      # depart_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
    #
    #     depart_from = self.wait_element_is_clickble(By.XPATH, "//input[@id='BE_flight_origin_city']")
    #     depart_from.click()  # Click on the input field to activate it
    #     depart_from.send_keys(departlocation)  # Send the desired keys

     # new part******
    def GoingToField(self):
        return self.wait_element_is_clickble(By.XPATH, self.GOING_TO_FIELD)

    def GoingToResults(self):
        self.driver.execute_script("document.querySelector('.opaque-layer').style.display='none';")

        return self.wait_for_presence_of_all_elments(By.XPATH, self.GOINT_TO_RESULT_LIST)

    def GetSearchButton(self):
        return self.wait_element_is_clickble(By.XPATH,self.SEARCH_BUTTON)

    def goingto(self, goingtolocation):
        # going_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        going_to = self.wait_element_is_clickble(By.XPATH, "//input[@id='BE_flight_arrival_city']")

        going_to.click()
        # time.sleep(2)
        going_to.send_keys(goingtolocation)

        self.driver.execute_script("document.querySelector('.opaque-layer').style.display='none';")

        # search_result = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
        #                                                                  "/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/input[1]")))

        search_results = self.wait_for_presence_of_all_elments(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/input[1]")

        for results in search_results:
            if "New York (JFK)" in results.text:
                results.click()
                break

    def clicksearch(self):
        # search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,
        #                                                         "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']")))

        search_button = self.wait_element_is_clickble(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']")
        self.driver.execute_script("arguments[0].click();", search_button)




