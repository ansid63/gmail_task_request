from selenium.webdriver.common.by import By


class BasePageLocators():
    MAIL_LOGIN = (By.CSS_SELECTOR, "input#passp-field-login")
    MAIL_SUBMIT = (By.CSS_SELECTOR, ".button2_type_submit")
    PASSWORD_LOGIN = (By.CSS_SELECTOR, "input#passp-field-passwd")
    PASSWORD_SUBMIT = (By.CSS_SELECTOR, ".button2_type_submit")

    LOGIN_NAME = ""
    PASSWORD = ""




