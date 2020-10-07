import unittest

from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
    # test cases -> func's name that started with "test"

    # Setup will run every time the test cases is run
    def setUp(self):
        print("setUp")
        PATH = r"C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("http://www.python.org")


    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    # def test_title(self):
    #     mainPage = page.MainPage()
    #     assert mainPage.is_title_matches()
    #
    # def test_example(self):
    #     print("test")
    #     assert True
    #
    # def test_example_1(self):
    #     print("test1")
    #     assert True
    #
    # def not_a_test(self):
    #     print("thie wont print")

    # run after tescases is finished
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
