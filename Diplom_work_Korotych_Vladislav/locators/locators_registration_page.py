import os

from Diplom_work_Korotych_Vladislav.page.base_page import WebPage
from Diplom_work_Korotych_Vladislav.page.elements import WebElement
from Diplom_work_Korotych_Vladislav.page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("REGISTRATION_URL") or 'https://ru.pinterest.com/ideas/'

        super().__init__(web_driver, url)

    btn_registration = WebElement(xpath='//div[@data-test-id="emailSignUpButton"]')
    btn_enter_google = WebElement(xpath='//div[@data-test-id="google-connect-button"]')
    btn_terms_of_service = WebElement(xpath='//div[@data-test-id="tos"]')
    btn_privacy = WebElement(xpath='//div[@data-test-id="privacy"')
    btn_notice = WebElement(xpath='//div[@data-test-id="noticeAtCollection"]')
    btn_your_Enter = WebElement(xpath='//div[@data-test-id="login-signup-toggle"]')

