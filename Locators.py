
class TestLocatorsReg:
    INPUT_REGISTRATION_NAME = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input' # Поле ввода имени в регистрации
    INPUT_REGISTRATION_EMAIL = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input' # Поле ввода почты в регитрации
    INPUT_REGISTRATION_PSWD = '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input' # Поде ввода пароля в регистрации
    REG_BUTTON = ".//button[text()='Зарегистрироваться']" # Кнопка Зарегистрироваться
    ERROR_PSWD = "/html/body/div/div/main/div/form/fieldset[3]/div/p" # Элемент Некоректный пароль


class TestLocatorsLogin:
    LOGIN_BUTTON_ON_MAIN_PAGE = ".//button[text()='Войти в аккаунт']" # кнопка «Войти в аккаунт» на главной
    PERSONAL_ACCOUNT_BUTTON = "/html/body/div/div/header/nav/a/p" # кнопка «Личный кабинет» '//*[@id="root"]/div/header/nav/a/svg'
    LOGIN_BUTTON_ON_REG = '//*[@class="Auth_link__1fOlj"]' # Кнопка Войти на экране регистрации
    LOGIN_BUTTON_ON_RETURN = '/html/body/div/div/main/div/div/p/a' # Кнопка Войти на экране восставновления пароля


class TestLocatorsLoginInput:
    INPUT_LOGIN_EMAIL = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input' # Поле ввода емэйла
    INPUT_LOGIN_PSWD = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'  # Поле ввода пароля
    LOGIN_BUTTON = ".//button[text()='Войти']" # Кнопка Войти


class TestLocatorsOnAuthAcc:
    CONSTRUCTOR_BUTTON = "/html/body/div/div/header/nav/ul/li[1]/a" # Кнопка Конструктор
    LOGO_BANNER = "/html/body/div/div/header/nav/div/a" # Логотип сайта
    LOGOUT_BUTTON = ".//button[text()='Выход']" # Кнопка Выход

class TestLocatorsElementsConstruct:
    BULK_TAB = "/html/body/div/div/main/section[1]/div[1]/div[1]/span"
    SAUCE_TAB = '/html/body/div/div/main/section[1]/div[1]/div[2]/span'
    TOPPING_TAB = "/html/body/div/div/main/section[1]/div[1]/div[3]/span"
