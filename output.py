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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/07")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text



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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/07")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



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
		element.send_keys("yvr")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/07")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



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
		element.send_keys("yvr-vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/07")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text



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
		element.send_keys("vancouver yvr")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/07")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text



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
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/07")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/07")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("ny")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/07")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("12345")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/07")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text



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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/07")


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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/07")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text



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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/07")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("12-05")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/07")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text



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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("21/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("20/07")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text



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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text



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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/09")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text



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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("25-06")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text



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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("15/07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("14/07")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text




if __name__ == "__main__":
	unittest.main()