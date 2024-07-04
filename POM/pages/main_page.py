
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_class import Base



class main_page(Base):

    url = 'https://www.ozon.ru/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    field_request = '//input[@class="aa9c_32 tsBody500Medium"]'
    btn_search = '//button[@class="ac9a_32 ag05-a0 ag05-a6"]'
    main_word = '(//a[@class="d3y_10 tsBody500Medium"])[1]'

    #getters
    def get_request(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_request)))
    def get_btn_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_search)))
    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    #actoins
    def input_request(self, title):
        self.get_request().send_keys(title)
        print('input request')

    def click_btn_search(self):
        self.get_btn_search().click()
        print('click button search')

    #methods
    def search(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.refresh()
        self.get_cur_url()
        time.sleep(5)
        self.input_request('ssd')
        time.sleep(5)
        self.click_btn_search()
        time.sleep(5)
        self.assert_word(self.get_main_word(), 'Все категории')

