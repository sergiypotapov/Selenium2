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

    def test_search_text_field_max(self):
        self.driver.get("http://enterprise-demo.user.magentotrial.com//")
        # get search text box
        search_field = self.driver.find_element_by_id("search")
        # check that max attribute is 128
        self.assertEqual("128", search_field.get_attribute("maxlength"))

    def test_search_text_really_128_max(self):
        self.driver.get("http://enterprise-demo.user.magentotrial.com//")
        # get search text box
        search_field = self.driver.find_element_by_id("search")


        text = ''
        for i in range(0,129):
            text +=random.choice(string.ascii_letters)

        search_field.send_keys(text)
        entered_text = search_field.get_attribute("value")
        self.assertNotEqual(text,entered_text)

    def test_search_button_enabled(self):
        self.driver.get("http://enterprise-demo.user.magentotrial.com//")
        # get search button
        search_button = self.driver.find_element_by_class_name("button")
        self.assertTrue(search_button.is_enabled())

    def test_account_link_is_visible(self):
        self.driver.get("http://enterprise-demo.user.magentotrial.com//")
        # get link ACCOUNT
        account_link = self.driver.find_element_by_link_text("ACCOUNT")
        self.assertTrue(account_link.is_displayed())

    def test_number_of_links_with_account(self):
        self.driver.get("http://enterprise-demo.user.magentotrial.com//")
        # get all links which have Account text
        account_links = self.driver.find_elements_by_partial_link_text("ACCO")
        print(account_links)
        self.assertEqual(2, len(account_links))
        for i in account_links:
            self.assertTrue(i.is_displayed())

    def test_if_there_are_3_banners(self):
        self.driver.get("http://enterprise-demo.user.magentotrial.com//")
        # get promo banners
        banner_list = self.driver.find_element_by_class_name("promos")
        print(banner_list)
        banners = banner_list.find_elements_by_tag_name("img")
        self.assertEqual(3, len(banners))

    def test_gift_promo(self):
        self.driver.get("http://enterprise-demo.user.magentotrial.com//")
        gift_promo = self.driver.find_element_by_xpath("//img[@alt='Physical & Virtual Gift Cards']")
        self.assertTrue(gift_promo.is_displayed())
        gift_promo.click()
        # check vip promo is displayed
        self.assertEqual("Gift Card", self.driver.title)

    def test_shopping_cart_status(self):
        self.driver.get("http://enterprise-demo.user.magentotrial.com//")
        # get shopping cart
        cart = self.driver.find_element_by_css_selector("div.header-minicart span.icon")
        cart.click()
        # get message
        message = self.driver.find_element_by_css_selector("p.empty").text
        self.assertEqual(message, "You have no items in your shopping cart.")
        close = self.driver.find_element_by_css_selector("div.minicart-wrapper a.close.skip-link-close")
        close.click()

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

    @classmethod
    def tearDownClass(cls):
        #close bro
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main(verbosity=2)



