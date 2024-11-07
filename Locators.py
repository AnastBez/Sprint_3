
class TestLocatorsReg:
    INPUT_REGISTRATION_NAME = "//label[text()='Имя']//parent::*/input[@type='text' and @name='name']"
# Поле ввода имени в регистрации
    INPUT_REGISTRATION_EMAIL = ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']" # Поле ввода почты в регитрации
    INPUT_REGISTRATION_PSWD = ".//label[text()='Пароль']//parent::*/input[@type='password' and @name='Пароль']" # Поде ввода пароля в регистрации
    REG_BUTTON = ".//button[text()='Зарегистрироваться']" # Кнопка Зарегистрироваться
    ERROR_PSWD = ".//p[contains(@class, 'input__error')]" # Элемент Некоректный пароль


class TestLocatorsLogin:
    LOGIN_BUTTON_ON_MAIN_PAGE = ".//button[text()='Войти в аккаунт']" # кнопка «Войти в аккаунт» на главной
    PERSONAL_ACCOUNT_BUTTON = ".//p[text()='Личный Кабинет']" # кнопка «Личный кабинет»
    LOGIN_BUTTON_ON_REG = ".//a[text()='Войти']" # Кнопка Войти на экране регистрации
    LOGIN_BUTTON_ON_RETURN = './/a[@href="/login"]' # Кнопка Войти на экране восставновления пароля


class TestLocatorsLoginInput:
    INPUT_LOGIN_EMAIL = ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']" # Поле ввода емэйла
    INPUT_LOGIN_PSWD = ".//input[@type='password']"  # Поле ввода пароля
    LOGIN_BUTTON = ".//button[text()='Войти']" # Кнопка Войти


class TestLocatorsOnAuthAcc:
    CONSTRUCTOR_BUTTON = ".//p[text()='Конструктор']" # Кнопка Конструктор
    LOGO_BANNER = ".//div[@class='AppHeader_header__logo__2D0X2']" # Логотип сайта
    LOGOUT_BUTTON = ".//button[text()='Выход']" # Кнопка Выход
    HEADER_OF_BLOCK = ".//h1[text()='Соберите бургер']" # Заголовок блока "Соберите бургер"

class TestLocatorsElementsConstruct:
    BULK_TAB = ".//span[text()='Булки']" # Таб Булки
    SAUCE_TAB = ".//span[text()='Соусы']" # Таб Соусы
    TOPPING_TAB = ".//span[text()='Начинки']" # Таб Начинки
    HEADER_SAUCE = ".//h2[text()='Соусы']" # Заголовок Соусов
    HEADER_BULK = ".//h2[text()='Булки']" # Заголовок Булок
    HEADER_TOPPING = ".//h2[text()='Начинки']" # Заголовок Начинок