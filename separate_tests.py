__author__ = 'spotapov'
import unittest
import string
import random
from selenium import webdriver

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a FF window
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        #go to app HomePage
        cls.driver.get("http://enterprise-demo.user.magentotrial.com//")

    def test_full_cart(self):
        # insert some goods to the cart
        self.driver.get("http://enterprise-demo.user.magentotrial.com/bowery-chino-pants-545.html")

        color = self.driver.find_element_by_xpath("//img[@alt='Charcoal']")
        color.click()
        size = self.driver.find_element_by_xpath("//*[@title='32']")
        size.click()
        add_to_cart = self.driver.find_element_by_class_name("add-to-cart-buttons")
        add_to_cart.click()
        cart = self.driver.find_element_by_css_selector("#header > div > div.skip-links > div > div > a > span.icon")
        # click on cart
        cart.click()
        self.assertTrue("Bowery Chino Pants", self.driver.find_element_by_xpath("//*[@id='cart-sidebar']/li/div/p/a").text)
        self.assertTrue("$140.00", self.driver.find_element_by_class_name("price").text)
