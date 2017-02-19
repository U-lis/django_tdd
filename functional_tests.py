import unittest2 as unittest

from selenium import webdriver

TEST_HOST = "http://localhost:8000"


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retreive_it_later(self):
        self.browser.get(TEST_HOST)
        self.assertIn("To-Do", self.browser.title)
