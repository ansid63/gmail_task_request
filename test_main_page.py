from .pages.main_page import MainPage
import time


def test_user_login_and_check_letters(browser):
    link = "https://passport.yandex.ru/auth?from=mail&origin=hostroot_homer_auth_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1"
    user_login1 = MainPage(browser, link)
    user_login1.open()
    time.sleep(5)
    #input email account
    user_login1.mail_login()

    user_login2 = MainPage(browser, browser.current_url)
    time.sleep(5)
    #input password for account
    user_login2.password_login()

    main_page = MainPage(browser, browser.current_url)
    #main login find quantity of letters
    main_page.check_letters()
    time.sleep(5)

