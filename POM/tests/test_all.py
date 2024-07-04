from selenium import webdriver
from pages.catalog_page import catalog_page
from pages.main_page import main_page


def test_buy_product():
    driver = webdriver.Chrome()
    print('start test')

    main = main_page(driver)
    main.search()

    catalog = catalog_page(driver)
    catalog.filters()
    print('test finish')
