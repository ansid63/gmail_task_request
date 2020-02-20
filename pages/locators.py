from selenium.webdriver.common.by import By


class BasePageLocators():
    MAIL_LOGIN = (By.CSS_SELECTOR, "#identifierId")
    MAIL_SUBMIT = (By.XPATH, '//span[text()="Далее"]')
    PASSWORD_LOGIN = (By.CSS_SELECTOR, "[name="password"]")
    PASSWORD_SUBMIT = MAIL_SUBMIT = (By.XPATH, '//span[text()="Далее"]')

class MainPageLocators():
    TARGET OBJECT = (By.CSS_SELECTOR, "[email="andrey.sidorov@simbirsoft.com"]")


