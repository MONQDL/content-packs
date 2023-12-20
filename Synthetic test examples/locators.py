from selenium.webdriver.common.by import By

class LocatorsHttpbin:
    # Заголовок страницы
    TITLE = (By.XPATH, "//*[@class='title']")
    # Кнопка "Try it out"
    BUTTON_TRY_IT_OUT = (By.XPATH, "//*[@id='operations-Auth-get_basic_auth__user___passwd_']"
                                   "//button[@class='btn try-out__btn']")
    # Название параметра "user"
    PARAMETER_NAME_USER = (By.XPATH, "//*[@id='operations-Auth-get_basic_auth__user___passwd_']"
                                     "//*[@class='parameter__name'][contains(text(),'user')]")
    # Название параметра "passwd"
    PARAMETER_NAME_PASSWD = (By.XPATH, "//*[@id='operations-Auth-get_basic_auth__user___passwd_']"
                                       "//*[@class='parameter__name'][contains(text(),'passwd')]")
    # Поле для ввода значения параметра "user"
    INPUT_PARAMETER_USER = (By.XPATH, "//*[@id='operations-Auth-get_basic_auth__user___passwd_']"
                                      "//input[@placeholder='user']")
    # Поле для ввода значения параметра "passwd"
    INPUT_PARAMETER_PASSWD = (By.XPATH, "//*[@id='operations-Auth-get_basic_auth__user___passwd_']"
                                        "//input[@placeholder='passwd']")
    # Кнопка "Execute"
    BUTTON_EXECUTE = (By.XPATH, "//*[@id='operations-Auth-get_basic_auth__user___passwd_']"
                                "//button[contains(text(),'Execute')]")
