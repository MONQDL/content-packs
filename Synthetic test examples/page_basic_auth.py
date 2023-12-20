import pytest

from locators import LocatorsHttpbin
from page_base import BasePage


class PageHttpbin(BasePage):
    def go_to_basic_auth(self, base_url):
        """Выполняет переход к методу базовой аутентификации по прямой ссылке и обновление страницы"""
        self.driver.get((f"{base_url}/#/Auth/get_basic_auth__user___passwd_"))
        return self.driver.refresh()

    def fill_fields_user_passwd(self, login, password):
        """Заполняет поля user и passwd значениями, переданными в качестве аргументов"""
        try:
            self.find_element(LocatorsHttpbin.INPUT_PARAMETER_USER).send_keys(login)
            self.find_element(LocatorsHttpbin.INPUT_PARAMETER_PASSWD).send_keys(password)
        except Exception as err:
            pytest.fail("Не удалось заполнить поля user и passwd:" + str(err))

    def check_field_values_user_passwd(self, login, password):
        """Сравнивает значения в полях user и passwd с переданными в качестве аргументов"""
        try:
            failures = []
            user_value = self.find_element(LocatorsHttpbin.INPUT_PARAMETER_USER).get_attribute("value")
            passwd_value = self.find_element(LocatorsHttpbin.INPUT_PARAMETER_PASSWD).get_attribute("value")
            if not user_value == login:
                failures.append(f'Неверное значение в поле "user": {user_value} != {login}')
            if not passwd_value == password:
                failures.append(f'Неверное значение в поле "passwd": {passwd_value} != {password}')
            if not failures:
                return True
            else:
                pytest.fail(f"{failures}")
        except Exception as err:
            pytest.fail("Не удалось выполнить проверку значений:" + str(err))

