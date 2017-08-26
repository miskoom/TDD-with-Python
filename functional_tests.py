from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #checking out the new to-do app online
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


        # A friend is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                    'Enter a to-do item'
        )

        #When she hits enter, the page updates, and now the page lists
        #"1: Buy peacock feathers" as an item in a to-do lists
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
			"New to-do item did not appear in table"
            )

        #There is still a text box inviting her to add another item. She enters
        # "Use peacock feathers to make a fly" (Shes very methodical)
        self.self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

# She types "Buy peacock feathers" into a text box



#The page updates again, and now shows both items on her lists

# She wonders wether the site will remember her list. Then she sees that the
# site has Generated a unique URL for her -- there is some explanatory text to that effect

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep
