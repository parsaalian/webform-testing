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
		element.send_keys("23/08")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("24/08")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Skip to book a flight  Skip to main navigation  Skip to content  Skip to search field  Skip to footer links  Air Canada Search Search 



AccessibilitySelect your edition and language. You are currently on the Canada English edition.   You will be billed in  Canadian dollars  - CA$EnglishCA$







 Sign in 



Book



Plan



Fly



Aeroplan



Customer supportSpecial offers Air Canada - Official website - Homepage  Top of page banner 2X THE POINTSKonnichiwa, JapanSay hi to 2X the Aeroplan points on flights between Canada and Japan. Book by July 26 for travel until December 15, 2023.Register and bookLIMITED-TIME SALE15% off flights within Canada, and select flights to the U.S.Until July 20, save on all base fares for travel from August 22 until December 13, 2023.Book nowFlightsPackagesFlight PassesHotelsCarsMy bookingsCheck-inFlight statusAC VacationsBook your AC Vacation package 



We're sorry, we were not able to process your request. Please try again, or contact usOpens in a new tab for assistance.7 Flights  Trip type  Round-trip  One-way  Multi-city/Stopover  Book with points Vancouver YVRFrom Enter the first three characters of the city, airport, province, state or country/region you are starting from, then use your arrow keys to move up or down the list of airports provided to make your selection. Toronto  All airports To Enter the three first characters of the city, airport, province, state or country/region you are flying to, then use your arrow keys to move up or down the list of airports provided to make your selection. Wed Aug 23DepartureThu Aug 24Return



 Enter the date day and month in this format: DD/MM, or use the 'Show Calendar' button to open the calendar and select your date from there. Passenger(s) 1 Adult 1 AdultPress Enter or the space bar to open the passenger selection menu, then use tabs to move through the passenger section and complete your selection. Add promotion code  Search flights  Offers CONTESTAir Canada Rouge’s 10th Birthday ContestAir Canada Rouge’s 10th Birthday ContestTo celebrate 10 years, Aeroplan Members have the chance to win one of two amazing getaways with Air Canada Vacations.Enter now >EARN 5XGet more than groceries with 5X the ptsGet more than groceries with 5X the ptsUntil July 17, earn 5X the points on your first grocery order with Uber Eats.Order now >SALETreat yourself to an upgradeTreat yourself to an upgradeWith minimum bids up to 20% lower on select flights and dates, you can experience the extra comfort of a higher cabin class for less with AC Bid Upgrade.Learn more >DONATE NOWYour points make a differenceYour points make a differenceDonate points to GlobalMedic from July 10 to 16 and Aeroplan will match all member donations up to 500,000 points.Donate now > Travel news and updates COVID-19 UpdatesFlexible rebooking policy due to Western wildfiresRebooking policy due to Nova Scotia wildfiresFlexible rebooking policy for connecting flights via Toronto and MontrealU.S. removes all COVID-19 requirements More News Please wait while content is loading.Please wait while content is loading. Page content has loaded.
Best Airline Staff in Canada and North America















 Air Canada Customer supportContact InformationBaggage fees and optional servicesBaggage fee changesGeneral Conditions of Carriage & TariffsCustomer service planPrivacy PolicyOur cookie policySpecial offersView special offersEmail SubscriptionsModify preferencesAbout Air CanadaMedia centreOfficial LanguagesTravel AgentsCareersAir Canada CargoAir Canada FoundationInvestor RelationsSite mapBest Airline Staff in Canada and North America















© 2023 Air Canada



Indicates an external site which may not meet accessibility guidelines and/or language preferences." in body_text



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
		element.send_keys("")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("23/08")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("24/08")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text



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
		element.send_keys("yvr123")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("23/08")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("24/08")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text



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
		element.send_keys("23/08")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("24/08")


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
		element.send_keys("vancouver airport")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("23/08")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("24/08")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid point of origin for this trip." in body_text


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "Please select a valid destination for this trip." in body_text



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
		element.send_keys("23/08")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("24/08")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "The departure and arrival cities/airports you've selected are the same. Please review your selection and try again." in body_text



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
		element.send_keys("23/08")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("24/08")


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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("23/08")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("24/08")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "The departure and arrival cities/airports you've selected are the same. Please review your selection and try again." in body_text



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
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("24/08")


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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("23/08")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("24/08")


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
		element.send_keys("17-07")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("24/08")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



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
		element.send_keys("25/08")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("24/08")


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
		element.send_keys("23/08")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



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
		element.send_keys("23/08")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("23/08")


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
		element.send_keys("vancouver")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-typeahead[2]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("toronto")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[1]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("23/08")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("17-08")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text



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
		element.send_keys("23/08")


		element = self._wait_for_element("//body/ac-web-app[1]/div[1]/main[1]/div[1]/ac-acohome-page[1]/div[1]/div[1]/ac-booking-magnet[1]/div[1]/div[1]/div[1]/div[2]/ac-bkmg-flights-tab[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/abc-date-picker[1]/div[1]/div[1]/abc-input[2]/abc-form-element-container[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
		element.send_keys("22/08")


		button = self._wait_for_element("//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]//*[@type='submit']")
		driver.execute_script('arguments[0].click()', button)


		time.sleep(1)
		body_text = driver.find_element(By.TAG_NAME, 'body').text
		assert "" in body_text




if __name__ == "__main__":
	unittest.main()