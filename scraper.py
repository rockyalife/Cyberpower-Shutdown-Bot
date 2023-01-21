import configparser
import os
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

class MainBot:

    def __init__(self):
        self.initSelenium()

    def initSelenium(self):

        # Read the path to the ChromeDriver executable from an environment variable
        driver_path = os.environ['CHROME_DRIVER_PATH']

        # Read the URL and form element IDs from a configuration file
        configFile = configparser.ConfigParser()
        configFile.read('config.ini')

        self.config = configFile['DEFAULT']
        config = self.config

        # Set options to start the browser in headless mode
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')

        # Create a webdriver instance
        self.driver = webdriver.Chrome(executable_path=driver_path, options=options)
        driver = self.driver

        homeurl = config['HOME_URL']
        shutdown_url = config['SHUTDOWNMENU_URL']

        # Navigate to the webpage
        driver.get(homeurl)

        driver.implicitly_wait(10)

        time.sleep(2)

        # Find the form elements and fill in the form
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(config['USERNAME'])

        pass_field = driver.find_element(By.ID, "password")
        pass_field.send_keys(config['PASSWORD'])

        # Submit the form
        submit_button = driver.find_element(By.CSS_SELECTOR, '[data-target=".login_modal"]')
        submit_button.click()

        # Wait for the form to be submitted
        driver.implicitly_wait(10)
        time.sleep(2)

        # Go to Schedule Shutdown page
        driver.get(shutdown_url)

        ADD_button = driver.find_element(By.XPATH, '//button[text()="ADD"]')
        ADD_button.click()

        self.driver.minimize_window()

    def check_restore_option(self, restore_hours):
        driver = self.driver
        print(restore_hours)

        if restore_hours == "":
            restore_checkbox = driver.find_element(By.XPATH,
                                                   '//div[contains(text(), "Restore")]/following-sibling::div/p-checkbox/div')
            restore_checkbox.click()
        else:

            self.set_restore_date()
            self.click_outside()
            self.set_restore_time(restore_hours)

            print("cenas")

        self.confirm_scheduling()

    def set_restore_date(self):

        restore_date_input = self.driver.find_element(By.XPATH,
                                                      '//div[contains(text(), "Restore Date")]/following-sibling::div/p-calendar/span/input')
        # Get the current date and add one day to it

        restore_date = datetime.today()

        # Get the lower and upper bounds as datetime objects
        lower_bound = datetime.strptime('12:00', '%H:%M')
        upper_bound = datetime.strptime('23:59', '%H:%M')

        if lower_bound.time() <= datetime.now().time() <= upper_bound.time():
            restore_date += timedelta(days=1)

        # Format the date as a string in the DD/MM/YYYY format
        date_string = restore_date.strftime('%m/%d/%Y')

        # Clear the input field ( clear function wasn't working)
        self.driver.execute_script('arguments[0].value = ""', restore_date_input)

        restore_date_input.send_keys(date_string)

    def set_restore_time(self, chosen_time):

        restore_time_input = self.driver.find_element(By.XPATH,
                                                      '//div[contains(text(), "Restore Time")]/following-sibling::div/p-calendar/span/input')

        restore_time_input.click()

        time = datetime.strptime(chosen_time, '%H:%M')

        time_string = time.strftime('%H:%M')

        # print(time_string)

        # Clear the input field ( clear function wasn't working)
        self.driver.execute_script('arguments[0].value = ""', restore_time_input)

        restore_time_input.send_keys(time_string)

    def click_outside(self):

        clear_space = self.driver.find_element(By.XPATH,
                                               '//div[contains(text(), "Restore Time")]')

        clear_space.click()

    def confirm_scheduling(self):
        driver = self.driver

        ok_button = driver.find_element(By.XPATH, '//button[text()="OK"]')
        ok_button.click()

        # Close the browser
        driver.quit()
