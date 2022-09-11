#  Ludmila Afanasenko

# На основі попередньої домашки (2 частина) потрібно проапдейтити тести:
# - Додати логування (конфіги та створити і використати сам логгер)
# - Пару тестів (якщо використовуєте мої наброски)
# - Значення мають заповнюватися у вже існуючому обʼєкті, а не при ініціалізації
# А також створити:
# - Фікстуру рівня классу, що буде створювати обʼєкт та передавати його в тест
# - Фікстури рівня функції, що будуть заповнювати поля
# І оновити тести з використанням цих фікстур
import pytest
import logging

log = logging.getLogger(__name__)


class LoginForm:

    def sign_in_enabled(self, login, password):
        return bool(login) and bool(password)


@pytest.fixture(scope="class")
def login_form_object():
    login_form = LoginForm()
    yield login_form


@pytest.fixture(scope="function", autouse=True)
def login_form_login():
    login = "login"
    yield login


@pytest.fixture(scope="function", autouse=True)
def login_form_password():
    password = "password"
    yield password


class TestLoginForm:
    log = logging.getLogger(__name__)

    def test_logging(self):
        self.log.debug("DEBUG")

    def test_all_empty(self, login_form_object):
        all_empty = login_form_object.sign_in_enabled("", "")
        assert not all_empty, self.log.error(f"[{self.test_all_empty.__name__}] expected value: False, "
                                             f"actual value: {all_empty}")
        self.log.info(f"[{self.test_all_empty.__name__}] passed")

    def test_login_empty(self, login_form_object):
        login_empty = login_form_object.sign_in_enabled("", login_form_password)
        assert not login_empty, self.log.error(f"[{self.test_login_empty.__name__}] expected value: False, "
                                               f"actual value: {login_empty}")
        self.log.info(f"[{self.test_login_empty.__name__}] passed")

    def test_password_empty(self, login_form_object):
        password_empty = login_form_object.sign_in_enabled(login_form_login, "")
        assert not password_empty, self.log.error(f"[{self.test_password_empty.__name__}] expected value: False, "
                                                  f"actual value: {password_empty}")
        self.log.info(f"[{self.test_password_empty.__name__}] passed")

    def test_all_filled(self, login_form_object):
        all_filled = login_form_object.sign_in_enabled(login_form_login, login_form_password)
        assert all_filled, self.log.error(f"[{self.test_all_filled.__name__}] expected value: True, "
                                          f"actual value: {all_filled}")
        self.log.info(f"[{self.test_all_filled.__name__}] passed")
