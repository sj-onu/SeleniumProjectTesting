import time
from selenium import webdriver
import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestReport(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:\\seleniumProject1\\drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(2)

    def test_search_one(self):
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(2)

    def test_search_two(self):
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        self.driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        time.sleep(2)
        self.driver.find_element_by_name("username").send_keys("onu")
        self.driver.find_element_by_name("password").send_keys("onu")
        self.driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        time.sleep(2)

    def test_search_three(self):
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        time.sleep(2)
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        self.driver.find_element_by_name("username").send_keys("onu")
        self.driver.find_element_by_name("password").send_keys("onu7876")

        self.driver.find_element_by_name("submit").send_keys(Keys.ENTER)

    def test_search_four(self):
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        self.driver.find_element_by_name("username").send_keys("onu")
        self.driver.find_element_by_name("password").send_keys("onu")

        self.driver.find_element_by_name("submit").send_keys(Keys.ENTER)

    def test_search_five(self):
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        self.driver.find_element_by_name("username").send_keys("onu")
        self.driver.find_element_by_name("password").send_keys("onu")

        self.driver.find_element_by_name("submit").send_keys(Keys.ENTER)

    def test_search_six(self):
        self.driver.get("http://127.0.0.1:8000/registration/")
        self.driver.find_element_by_name("username").send_keys("onu")
        self.driver.find_element_by_name("password").send_keys("onu")
        self.driver.find_element_by_name("password confirmation").send_keys("onu")

        self.driver.find_element_by_name("submit").send_keys(Keys.ENTER)

        self.driver.find_element(By.LINK_TEXT, "Forgot your password?").click()



    def test_search_seven(self):
        self.driver.get("http://127.0.0.1:8000/registration/")
        self.driver.find_element_by_name("username").send_keys("onu")
        self.driver.find_element_by_name("password1").send_keys("4343")
        self.driver.find_element_by_name("password2").send_keys("4343")

        self.driver.find_element_by_name("submit").send_keys(Keys.ENTER)

    def test_search_eight(self):
        self.driver.get("http://127.0.0.1:8000/member")
        self.driver.find_element(By.LINK_TEXT, "Details").click()
        time.sleep(2)

    def test_search_nine(self):
        self.driver.get("http://127.0.0.1:8000/member/")
        time.sleep(2)

    def test_search_ten(self):
        self.driver.get("http://127.0.0.1:8000/member")
        self.driver.find_element(By.LINK_TEXT, "Details").click()
        time.sleep(2)

    def test_search_eleven(self):
        self.driver.get("http://127.0.0.1:8000/member")
        self.driver.find_element_by_name("search").send_keys("Titu")
        self.driver.find_element_by_name("submit").send_keys(Keys.ENTER)
        time.sleep(2)

    def test_search_twelve(self):
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        self.driver.get("http://127.0.0.1:8000/member/10")
        time.sleep(2)
    def test_search_thirteen(self):
        self.driver.get("http://127.0.0.1:8000/member/")
        time.sleep(2)
        self.driver.get("http://127.0.0.1:8000/insertMember/")
        time.sleep(2)

    def test_search_fourteen(self):
        self.driver.get("http://127.0.0.1:8000/insertMember/")
        self.driver.find_element_by_name("name").send_keys("Aysha")
        self.driver.find_element_by_name("age").send_keys("23")
        self.driver.find_element_by_name("address").send_keys("Dhaka")
        self.driver.find_element_by_name("mobile").send_keys("01234637")
        self.driver.find_element_by_name("email").send_keys("1234@uap.com")
        self.driver.find_element_by_name("interest_in").send_keys("Donor")

        self.driver.find_element_by_name("submit").send_keys(Keys.ENTER)

        time.sleep(2)

    def test_search_fifteen(self):
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        self.driver.get("http://127.0.0.1:8000/requests/")
        time.sleep(2)

    def test_search_sixteen(self):
        self.driver.get("http://127.0.0.1:8000/requests/")
        time.sleep(2)
        self.driver.get("http://127.0.0.1:8000/insertRequest/")

    def test_search_seventeen(self):
        self.driver.get("http://127.0.0.1:8000/requests/")
        time.sleep(2)
        self.driver.get("http://127.0.0.1:8000/insertRequest/")

        self.driver.find_element_by_name("person_name").send_keys("Emon")
        self.driver.find_element_by_name("location").send_keys("Dhaka")
        self.driver.find_element_by_name("mobile").send_keys("0179234637")
        self.driver.find_element_by_name("req_type").send_keys("Need Money")
        self.driver.find_element_by_name("req_statement").send_keys("We need help in our location")

        self.driver.find_element_by_name("submit").send_keys(Keys.ENTER)
        time.sleep(2)

    def test_search_eighteen(self):
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        self.driver.get("http://127.0.0.1:8000/donation/")
        time.sleep(2)

    def test_search_nineteen(self):
        self.driver.get("http://127.0.0.1:8000/donation/")
        time.sleep(2)
        self.driver.get("http://127.0.0.1:8000/insertDonation/")
        time.sleep(2)

    def test_search_twenty(self):
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        self.driver.save_screenshot("image.png")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")




if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:\seleniumProject1\Reports'))
