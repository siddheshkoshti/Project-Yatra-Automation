import time

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pythonProject1.pages.search_flights_results_page import SearchFlightResults
from pythonProject1.pages.yatra_launch_page import LaunchPage
from pythonProject1.utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():
    def test_Search_Flights(self):

        # provide depart location
        lp = LaunchPage(self.driver, self.wait)
        # lp.departfrom("New Delhi")
        lp.enterDepartFromLocation("New Delhi")
        # provide going to location
        lp.goingto("New York")

        # click on flight search button
        lp.clicksearch()

        # date = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_date']")))
        # date.click()

        # all_dates = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[not(contains(@class, 'inActiveTD'))]")))
        #
        # for date in all_dates:
        #     if date.get_attribute("data-date") =="23/08/2021":
        #         date.click()
        #         break



        # this is for page scroll till end

        lp.page_scroll()

        sf = SearchFlightResults(self.driver,self.wait)
        sf.filter_flights()



        # driver.find_element(By.XPATH,"/html[1]/body[1]/section[2]/section[1]/section[1]/div[1]/div[1]/div[1]/div[2]/div[2]/label[2]/p[1]").click()
        # time.sleep(2)

        # self.driver.find_element(By.XPATH, "//p[normalize-space()='1']").click()

        # allstops1 = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
        #                                                                  "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")))

        # instead of above allstop we created a method and using this method here
        allstops1 = lp.wait_for_presence_of_all_elments(By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")
        print(print(len(allstops1)))

        ut = Utils()
        ut.assertlistItemtext(allstops1, "1 Stop")


        # for stop in allstops1:
        #     print("The trxt is :" + stop.text)
        #     assert stop.text == "1 Stop"
        #     print("assert pass")

        # extra code this also works for filtering stops
        # all_stops_info = wait.until(EC.presence_of_all_elements_located(
        #     (By.XPATH, "//div[contains(@class, 'stops-details')]//div[@class='fs-12']")))
        # print(f"Number of flights found with 1 stop: {len(all_stops_info)}")
        #
        # for stop in all_stops_info:
        #     print(f"The text is: {stop.text}")
        #     assert stop.text == "1 Stop"
        #     print("Assertion passed for stop check")
