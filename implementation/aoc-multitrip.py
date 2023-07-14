import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager


class FormTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
		self.driver.get("https://www.aircanada.com/ca/en/aco/home.html")
    
    
	def tearDown(self):
		self.driver.close()


	def _wait_for_element(self, xpath):
		element = WebDriverWait(self.driver, 5).until(
			EC.presence_of_element_located((By.XPATH, xpath))
		)
		return element



	def test_0(self):
		'''0'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("newyork")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("los angeles")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("chicago")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("new york")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("25/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text



	def test_1(self):
		'''1'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("newyork")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("los angeles")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("chicago")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("los angeles")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("25/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text



	def test_2(self):
		'''2'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("new york")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("los angeles")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("chicago")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("new york")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "It is not possible to search for flights which have both an origin and a destination in the United States." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "It is not possible to book a flight segment between two cities in the same country, unless that country is Canada.  Please contact Air Canada ReservationsOpens in a new tab for assistance with this type of booking." in body_text



	def test_3(self):
		'''3'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "We're sorry, we were not able to process your request. Please try again, or contact usOpens in a new tab for assistance.7" in body_text



	def test_4(self):
		'''4'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "We're sorry, we were not able to process your request. Please try again, or contact usOpens in a new tab for assistance.7" in body_text



	def test_5(self):
		'''5'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Searching for flights from Vancouver (YVR) to Paris (All airports) on 20-Dec for 1 adult.




    Loading...















  
          Skip to homepage
        



  
          Skip to main navigation
        



  
          Skip to content
        



  
          Skip to search field
        



  
          Skip to footer links
        



  
          Skip to site map
        



  
          Skip to contact
        























    Air Canada
  
































Customer support














Select your edition and language. You are currently on the Canada English edition.  
			You will be billed in Canadian dollars - CA$





EnglishCA$















|







Sign in





See your profile





































Searching for flights from Vancouver (YVR) to Paris (All airports) on 20-Dec for 1 adult.















            application.iOS.message
        









Customer support





Contact Information



Baggage fees and optional services



Baggage fee changes





Special offers





View special offers



Why book with us



Email Subscriptions



Modify preferences





About Air Canada





Media centre



Travel Agents



Careers


























Air Canada Cargo



Air Canada Foundation



Investor Relations



Site map











Best Airline Staff in Canada and North America
















General Conditions of Carriage & Tariffs

|


Customer service plan

|


Privacy Policy

|


Our cookie policy






© 2023 Air Canada


Indicates an external site which may not meet accessibility guidelines and/or language preferences." in body_text



	def test_6(self):
		'''6'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "The departure and arrival cities/airports you've selected are the same. Please review your selection and try again." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "It is not possible to book a flight segment between two cities in the same country, unless that country is Canada.  Please contact Air Canada ReservationsOpens in a new tab for assistance with this type of booking." in body_text



	def test_7(self):
		'''7'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "You've entered the same point of origin and/or the same destination twice. Please review your selection and try again." in body_text



	def test_8(self):
		'''8'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



	def test_9(self):
		'''9'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("new york")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



	def test_10(self):
		'''10'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("10001")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text



	def test_11(self):
		'''11'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("new york, united states")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text



	def test_12(self):
		'''12'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto, canada")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text



	def test_13(self):
		'''13'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



	def test_14(self):
		'''14'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "The departure and arrival cities/airports you've selected are the same. Please review your selection and try again." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "It is not possible to book a flight segment between two cities in the same country, unless that country is Canada.  Please contact Air Canada ReservationsOpens in a new tab for assistance with this type of booking." in body_text



	def test_15(self):
		'''15'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



	def test_16(self):
		'''16'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "The departure and arrival cities/airports you've selected are the same. Please review your selection and try again." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "It is not possible to book a flight segment between two cities in the same country, unless that country is Canada.  Please contact Air Canada ReservationsOpens in a new tab for assistance with this type of booking." in body_text



	def test_17(self):
		'''17'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



	def test_18(self):
		'''18'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



	def test_19(self):
		'''19'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20-12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Loading...















  
          Skip to homepage
        



  
          Skip to main navigation
        



  
          Skip to content
        



  
          Skip to search field
        



  
          Skip to footer links
        



  
          Skip to site map
        



  
          Skip to contact
        























    Air Canada
  
































Customer support














Select your edition and language. You are currently on the Canada English edition.  
			You will be billed in Canadian dollars - CA$





EnglishCA$















|







Sign in





See your profile





































Searching for flights from East London (ELS) to Paris (All airports) on 20-Dec for 1 adult.















            application.iOS.message
        









Customer support





Contact Information



Baggage fees and optional services



Baggage fee changes





Special offers





View special offers



Why book with us



Email Subscriptions



Modify preferences





About Air Canada





Media centre



Travel Agents



Careers


























Air Canada Cargo



Air Canada Foundation



Investor Relations



Site map











Best Airline Staff in Canada and North America
















General Conditions of Carriage & Tariffs

|


Customer service plan

|


Privacy Policy

|


Our cookie policy






© 2023 Air Canada


Indicates an external site which may not meet accessibility guidelines and/or language preferences." in body_text



	def test_20(self):
		'''20'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("22/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "We're sorry, we were not able to process your request. Please try again, or contact usOpens in a new tab for assistance.7" in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text



	def test_21(self):
		'''21'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Searching for flights from East London (ELS) to Paris (All airports) on 20-Dec for 1 adult.




    Loading...















  
          Skip to homepage
        



  
          Skip to main navigation
        



  
          Skip to content
        



  
          Skip to search field
        



  
          Skip to footer links
        



  
          Skip to site map
        



  
          Skip to contact
        























    Air Canada
  
































Customer support














Select your edition and language. You are currently on the Canada English edition.  
			You will be billed in Canadian dollars - CA$





EnglishCA$















|







Sign in





See your profile





































Searching for flights from East London (ELS) to Paris (All airports) on 20-Dec for 1 adult.















            application.iOS.message
        









Customer support





Contact Information



Baggage fees and optional services



Baggage fee changes





Special offers





View special offers



Why book with us



Email Subscriptions



Modify preferences





About Air Canada





Media centre



Travel Agents



Careers


























Air Canada Cargo



Air Canada Foundation



Investor Relations



Site map











Best Airline Staff in Canada and North America
















General Conditions of Carriage & Tariffs

|


Customer service plan

|


Privacy Policy

|


Our cookie policy






© 2023 Air Canada


Indicates an external site which may not meet accessibility guidelines and/or language preferences." in body_text



	def test_22(self):
		'''22'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("ord")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



	def test_23(self):
		'''23'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "You've entered the same point of origin and/or the same destination twice. Please review your selection and try again." in body_text



	def test_24(self):
		'''24'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text



	def test_25(self):
		'''25'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "The departure and arrival cities/airports you've selected are the same. Please review your selection and try again." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "It is not possible to book a flight segment between two cities in the same country, unless that country is Canada.  Please contact Air Canada ReservationsOpens in a new tab for assistance with this type of booking." in body_text



	def test_26(self):
		'''26'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



	def test_27(self):
		'''27'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



	def test_28(self):
		'''28'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "The departure and arrival cities/airports you've selected are the same. Please review your selection and try again." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "It is not possible to book a flight segment between two cities in the same country, unless that country is Canada.  Please contact Air Canada ReservationsOpens in a new tab for assistance with this type of booking." in body_text



	def test_29(self):
		'''29'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



	def test_30(self):
		'''30'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "You've entered the same point of origin and/or the same destination twice. Please review your selection and try again." in body_text



	def test_31(self):
		'''31'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



	def test_32(self):
		'''32'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



	def test_33(self):
		'''33'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "We're sorry, we were not able to process your request. Please try again, or contact usOpens in a new tab for assistance.7" in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text



	def test_34(self):
		'''34'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21-12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



	def test_35(self):
		'''35'''
		driver = self.driver

		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]")
		element.send_keys("r")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]")
		element.send_keys("o")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]")
		element.send_keys("m")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]")
		element.send_keys("true")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("london")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("paris")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/12")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("tokyo")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("berlin")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[2]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("19/12")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "The travel dates for your flight segments are not in chronological order. Please review the dates for flight 2 and try again. Click here to correct the date." in body_text




if __name__ == "__main__":
	unittest.main()