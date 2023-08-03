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
    
    

	def test_0(self):
		'''0'''
		driver = self.driver

		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]"))
		)
		element.send_keys("True")


		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]"))
		)
		element.send_keys("False")


		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]"))
		)
		element.send_keys("True")


		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]"))
		)
		element.send_keys("False")


		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"))
		)
		element.send_keys("")


		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"))
		)
		element.send_keys("hu7glqygaj")


		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"))
		)
		element.send_keys("c9ujlio4ce")


		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"))
		)
		element.send_keys("drvemuivcp")


		button = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']"))
		)
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select valid travel dates for this trip." in body_text



	def test_1(self):
		'''1'''
		driver = self.driver

		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[1]/div[1]/input[1]"))
		)
		element.send_keys("True")


		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[2]/div[1]/input[1]"))
		)
		element.send_keys("False")


		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/fieldset[1]/abc-radio-group[1]/div[1]/div[1]/abc-radio-button[3]/div[1]/input[1]"))
		)
		element.send_keys("True")


		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/ac-search-type-toggle[1]/div[1]/abc-checkbox[1]/div[1]/div[1]/input[1]"))
		)
		element.send_keys("False")


		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"))
		)
		element.send_keys("5w2y2hwg4n")


		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"))
		)
		element.send_keys("")


		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"))
		)
		element.send_keys("c9ujlio4ce")


		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"))
		)
		element.send_keys("drvemuivcp")


		button = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']"))
		)
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select valid travel dates for this trip." in body_text




if __name__ == "__main__":
	unittest.main()