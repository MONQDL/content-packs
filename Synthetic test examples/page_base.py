from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        """Ищет один элемент и возвращает его, используя явное ожидание"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def element_is_visible(self, locator, time=20):
        """Ищет отображаемый элемент и возвращает его, используя явное ожидание"""
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Element is not visible {locator}")

    def element_is_clickable(self, locator, time=60):
        """Проверяет кликабельность элемента и возвращает его, используя явное ожидание"""
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((locator)))
