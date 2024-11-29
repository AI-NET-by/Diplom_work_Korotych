import os

from Diplom_work_Korotych_Vladislav.page.base_page import WebPage
from Diplom_work_Korotych_Vladislav.page.elements import WebElement
from Diplom_work_Korotych_Vladislav.page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ru.pinterest.com/'

        super().__init__(web_driver, url)

        registration_button = ManyWebElements(xpath='//div[@class="X8m tg7 tBJ dyH iFc sAJ H2s"]')
