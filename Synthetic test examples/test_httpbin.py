import allure
import pytest
from allure_commons.types import AttachmentType

from locators import LocatorsHttpbin
from page_basic_auth import PageHttpbin
from settings import *


@allure.feature('httpbin-basic-auth')
@allure.story('Проверка ввода логина и пароля')
def test_httpbin(browser):
    """
        Шаг 1. Проверка доступности ресурса.
            Выполнить переход к httpbin по прямой ссылке.

            ОР: Отображается заголовок "httpbin.org".

        Шаг 2. Проверка доступности перехода к методу "basic_auth" по прямой ссылке.
            Выполнить переход к методу "basic_auth" по прямой ссылке.

            ОР: В блоке Параметры имеются элементы с ключами "user" и "passwd".

        Шаг 3. Проверка возможности указания значений для "user" и "passwd".
            Нажать "Try it out";
            Заполнить поля значений для "user" и "passwd".

            ОР: Поля заполнены успешно

        Шаг 4. Проверка кликабельности кнопки Execute.
            Кликнуть на "Execute".

            ОР: Кнопка кликабельна."""

    with allure.step('Шаг 1. Проверка доступности ресурса.'):
        try:
            page = PageHttpbin(browser)
            browser.get(BASE_URL)
            assert "httpbin.org" in page.find_element(locator=LocatorsHttpbin.TITLE).text
            allure.attach(browser.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name='error_screen', attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 2. Проверка доступности перехода к методу "basic_auth" по прямой ссылке.'):
        try:
            page.go_to_basic_auth(BASE_URL)
            assert page.element_is_visible(LocatorsHttpbin.PARAMETER_NAME_USER)
            assert page.element_is_visible(LocatorsHttpbin.PARAMETER_NAME_PASSWD)
            allure.attach(browser.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name='error_screen', attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 3. Проверка возможности указания значений для "user" и "passwd"'):
        try:
            page.element_is_clickable(LocatorsHttpbin.BUTTON_TRY_IT_OUT).click()
            page.fill_fields_user_passwd(login=USER_LOGIN, password=USER_PASSWORD)
            assert page.check_field_values_user_passwd(login=USER_LOGIN, password=USER_PASSWORD)
            allure.attach(browser.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name='error_screen', attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 4. Проверка кликабельности кнопки Execute.'):
        try:
            page.element_is_clickable(LocatorsHttpbin.BUTTON_EXECUTE).click()
            allure.attach(browser.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name='error_screen', attachment_type=AttachmentType.PNG)
            pytest.fail("Не удалось нажать на кнопку 'Execute'")
            raise

