from .base_page import BasePage
from .locators import MainPageLocators



class MainPage(BasePage):
    #def __init__(self, *args, **kwargs):
     #   super(MainPage, self).__init__(*args, **kwargs)

    def check_letters(self):
        letters_from = self.browser.find_element(*MainPageLocators.TARGET_OBJECT)
