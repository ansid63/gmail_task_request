from .base_page import BasePage

from selenium.webdriver.common.by import By



class MainPage(BasePage):
    def check_letters(self):
        letters_from = self.browser.find_elements(By.CSS_SELECTOR, 'span[title="noreply@moikrug.ru"]')
        #На случай проверки на количество assert (len(letters_from) == 1), "Неее их тутъ больше"
        print("Количество писем от адресата", len(letters_from))

