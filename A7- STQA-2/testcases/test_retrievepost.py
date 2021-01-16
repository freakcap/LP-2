# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestRetrievepost():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_retrievepost(self):
    self.driver.get("http://localhost:8000/")
    self.driver.set_window_size(1856, 1053)
    self.driver.find_element(By.CSS_SELECTOR, ".fa-home").click()
    self.driver.find_element(By.LINK_TEXT, "test_user_3").click()
    self.driver.find_element(By.LINK_TEXT, "asdasd").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "p").text == "This is Test Post "
  