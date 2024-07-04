class Base():
    def __init__(self, driver):
        self.driver = driver

    def get_cur_url(self):
        get_url = self.driver.current_url

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')
