
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

from base.base_class import Base


class catalog_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    filter_volume = '(//div[@class="a403-a5"])[5]'
    filter_form = '(//div[@class="a403-a5"])[9]'
    filter_type = '(//div[@class="a403-a5"])[15]'
    scroll_place = '(//span[@class="ej_10 tsBodyControl500Medium"])[6]'
    product = '(//button[@class="e7 b214-a0 b214-b5 b214-a4"])[1]'
    basket = '//a[@data-widget="headerIcon"]'
    catalog_word = '(//div[@class="ga14-a2 tsBodyControl400Small"])[4]'
    #getters
    def get_filter_volume(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_volume)))
    def get_filter_form(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_form)))
    def get_filter_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_type)))
    def get_scroll_place(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.scroll_place)))
    def get_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product)))
    def get_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket)))
    def get_catalog_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_word)))

    #actoions

    def scroll(self):
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(self.get_scroll_place()).perform()
        print('scroll to filters')
    def scroll_to_product(self):
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(self.get_product()).perform()
        print('scroll to product')

    def click_filter_volume(self):
        self.get_filter_volume().click()
        print('click filter volume')
    def click_filter_form(self):
        self.get_filter_form().click()
        print('click filter form')
    def click_filter_type(self):
        self.get_filter_type().click()
        print('click filter type')
    def click_product(self):
        self.get_product().click()
        print('add product')
    def click_basket(self):
        self.get_basket().click()
        print('click basket')

    #methods

    def filters(self):
        self.get_cur_url()
        time.sleep(5)
        self.scroll()
        self.click_filter_volume()
        time.sleep(5)
        self.click_filter_form()
        time.sleep(5)
        self.click_filter_type()
        time.sleep(5)
        self.scroll_to_product()
        time.sleep(5)
        self.click_product()
        time.sleep(5)
        self.click_basket()
        time.sleep(5)
        self.assert_word(self.get_catalog_word(), 'Удалить выбранные')