import pytest
from pages.base_page import BasePage
from locators.auth_module import AuthLocs, AuthData


@pytest.fixture()
def login(log_page):
    log_page.open()
    log_page.fill_input_user(AuthData.user)
    log_page.fill_pass_user(AuthData.pass_word)
    log_page.click_login_btn()
    return login


@pytest.fixture()
def locked_out_log(log_page):
    log_page.open()
    log_page.fill_input_user(AuthData.locked_user)
    log_page.fill_pass_user(AuthData.pass_word)
    log_page.click_login_btn()
    return locked_out_log


@pytest.fixture()
def problem_log(log_page):
    log_page.open()
    log_page.fill_input_user(AuthData.problem_user)
    log_page.fill_pass_user(AuthData.pass_word)
    log_page.click_login_btn()
    return problem_log


@pytest.fixture()
def glitch_log(log_page):
    log_page.open()
    log_page.fill_input_user(AuthData.glitch_user)
    log_page.input_pass().send_keys(AuthData.pass_word)
    log_page.click_login_btn()
    return glitch_log


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

    @staticmethod
    def locked_msg():
        return AuthLocs.locked_msg

    @staticmethod
    def login_err_msg():
        return AuthLocs.login_err_msg
