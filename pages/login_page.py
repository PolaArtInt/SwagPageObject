import pytest
from pages.base_page import BasePage
from locators.auth_module import AuthLocs, AuthData


@pytest.fixture()
def login(log_page):
    log_page.auth(AuthData.user, AuthData.pass_word)


@pytest.fixture()
def locked_out_log(log_page):
    log_page.auth(AuthData.locked_user, AuthData.pass_word)


@pytest.fixture()
def problem_log(log_page):
    log_page.auth(AuthData.problem_user, AuthData.pass_word)


@pytest.fixture()
def glitch_log(log_page):
    log_page.auth(AuthData.glitch_user, AuthData.pass_word)


class LoginPage(BasePage):
    def input_user(self):
        return self.is_visible(AuthLocs.input_user)

    def fill_input_user(self, username):
        return self.is_visible(AuthLocs.input_user).send_keys(username)

    def input_pass(self):
        return self.is_visible(AuthLocs.input_pass)

    def fill_pass_user(self, password):
        return self.is_visible(AuthLocs.input_pass).send_keys(password)

    def login_btn(self):
        return self.is_clickable(AuthLocs.login_btn)

    def click_login_btn(self):
        return self.is_clickable(AuthLocs.login_btn).click()

    def auth(self, username, password):
        self.open()
        self.fill_input_user(username)
        self.fill_pass_user(password)
        self.click_login_btn()
        return self

    @staticmethod
    def locked_msg():
        return AuthLocs.locked_msg

    @staticmethod
    def login_err_msg():
        return AuthLocs.login_err_msg
