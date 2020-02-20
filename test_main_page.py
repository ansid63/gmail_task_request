from .pages.main_page import MainPage

def user_login_and_check_letters(browser):
    link = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
    user_login1 = MainPage(browser, link)
    user_login1.open()
    user_login1.mail_login()
    user_login2 = MainPage(browser, browser.current_url)
    user_login2.password_login()
    main_page = MainPage(browser, browser.current_url)
    main_page.check_letters()

