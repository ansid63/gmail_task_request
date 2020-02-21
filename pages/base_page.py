from .locators import BasePageLocators



class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def mail_login(self):
        fill_mail = self.browser.find_element(*BasePageLocators.MAIL_LOGIN)
        fill_mail.send_keys(*BasePageLocators.LOGIN_NAME)
        submit_mail = self.browser.find_element(*BasePageLocators.MAIL_SUBMIT)
        submit_mail.click()

    def password_login(self):
        fill_password = self.browser.find_element(*BasePageLocators.PASSWORD_LOGIN)
        fill_password.send_keys(*BasePageLocators.PASSWORD)
        submit_password = self.browser.find_element(*BasePageLocators.PASSWORD_SUBMIT)
        submit_password.click()
