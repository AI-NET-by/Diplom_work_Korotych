import os

from Diplom_work_Korotych_Vladislav.page.base_page import WebPage
from Diplom_work_Korotych_Vladislav.page.elements import WebElement
from Diplom_work_Korotych_Vladislav.page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ru.pinterest.com'

        super().__init__(web_driver, url)

    btn_blog = WebElement(xpath='//div[@data-test-id ="header-blog-button"]')
    btn_description = WebElement(xpath='//div[@data-test-id ="header-about-button"]')
    btn_business = WebElement(xpath='//div[@data-test-id ="header-business-button"]')
    btn_login = WebElement(xpath='//div[@data-test-id ="simple-login-button"]')
    btn_sign_up = WebElement(xpath='//div[@data-test-id ="simple-signup-button"]')
    btn_ideas = WebElement(xpath='//div[@data-test-id="unauth-header"]//a[@href="/ideas/"')

    btn_privacy = WebElement(xpath='//div[@data-test-id="privacy-policy"]//a[@href="/ideas/"')
    btn_help= WebElement(xpath='//div[@data-test-id="help-link"]//a[@href="/ideas/"')
    btn_iphone = WebElement(xpath='//div[@data-test-id="iphone-app-link"]//a[@href="/ideas/"')
    btn_android = WebElement(xpath='//div[@data-test-id="android-app-link"]//a[@href="/ideas/"')
    btn_users = WebElement(xpath='//div[@data-test-id="users-sitemap"]//a[@href="/ideas/"')
    btn_collections = WebElement(xpath='//div[@data-test-id="boards-sitemap"]//a[@href="/ideas/"')
    btn_today = WebElement(xpath='//div[@data-test-id="today-link"]//a[@href="/ideas/"')
    btn_ideas_link = WebElement(xpath='//div[@data-test-id="ideas-link"]//a[@href="/ideas/"')
    btn_shopping = WebElement(xpath='//div[@data-test-id="shopping-sitemap"]//a[@href="/ideas/"')


