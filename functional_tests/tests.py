from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# User story 1.
# As a user, I want to add a list of tasks that I have not completed so that I can plan my day to do them.
# User story 2.
# As a user, I want to add a task such that it includes a description, due date and an estimated time to complete.
# User story 3.


class NewTasksTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_add_a_task_and_view_it_later(self):
        # Josh goes onto the tasker.com site
        self.browser.get(self.live_server_url)

        # Clicks add a new task.
        add_task_button = self.browser.find_element_by_id('id_new_task_button')
        self.assertIsNotNone(add_task_button)
        add_task_button.click()
        time.sleep(2) # Wait for the page to load.

        # The page is redirected to the add Task page
        self.assertEquals(self.live_server_url + "/tasks/add/", self.browser.current_url)
        add_task_title = self.browser.find_element_by_id('id_add_task_title')
        self.assertEquals("Add Task", add_task_title.text)


        # The page has inputboxes for the title, due date and the estimate of time for the task to be entered.
        # Josh does not have a due date or estimate for the task, so he just adds the task title.
        title_inputbox = self.browser.find_element_by_id('id_task_title_inputbox')
        self.assertEquals(
            title_inputbox.get_attribute('placeholder'),
            'Task name'
        )
        title_inputbox.send_keys('Buy groceries')

        # Josh clicks the submit task button
        submit_task_button = self.browser.find_element_by_id('id_submit_task_button')
        self.assertIsNotNone(submit_task_button)
        submit_task_button.click()

        time.sleep(2)

        # Josh is redirected back to the list page
        my_tasks_title = self.browser.find_element_by_id('id_my_tasks_title')
        self.assertIsNotNone(my_tasks_title)

        # Josh checks if the list item is there.
        task_table = self.browser.find_element_by_id('id_task_table')
        rows = task_table.find_elements_by_tag_name('td')
        self.assertIn("Buy groceries", [row.text for row in rows])
        # Happy with everything josh logs off.






















