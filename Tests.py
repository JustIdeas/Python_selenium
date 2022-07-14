import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

import setup



# surucucu = "lucas bauduco"


class testing_all (unittest.TestCase):

    def setUp(self) -> None:

        self.driver = webdriver.Firefox(executable_path=str(setup.location))
        self.driver.implicitly_wait(3)


    def test_terra(self):
        self.driver.get(setup.default_url) # Open the browser
        self.driver.find_element(By.XPATH, "(//a[normalize-space()='Economia'])[1]").click() # Open the page of the sports"
        economy_list = self.driver.find_elements(By.XPATH, "//div[@id='app-1325498']//div[@class='content']//ul[@class='list list--stockexchange']//li")
        economy_list_names = []
        economy_list_values = []
        for el in economy_list:
            for i in el.find_elements(By.CLASS_NAME, "list__text"):
                if not i.text == "":
                    if not i.get_attribute('id'):
                        economy_list_names.append(i.text)
                    else:
                        economy_list_values.append((i.text).strip("R$ ").strip("%").strip("-"))
        print(economy_list_names," OUTRA LISTA /n", economy_list_values)
                

if __name__ == '__main__':
    unittest.main()

