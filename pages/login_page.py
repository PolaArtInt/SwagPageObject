import pytest
from pages.base_page import BasePage
from locators.auth_module import AuthLocs, AuthData


@pytest.fixture()
def login(log_page):
    log_page.open()
    log_page.input_user().send_keys(AuthData.user)
    log_page.input_pass().send_keys(AuthData.pass_word)
    log_page.login_btn().click()
    return login


@pytest.fixture()
def locked_out_log(log_page):
    log_page.open()
    log_page.input_user().send_keys(AuthData.locked_user)
    log_page.input_pass().send_keys(AuthData.pass_word)
    log_page.login_btn().click()
    return locked_out_log


@pytest.fixture()
def problem_log(log_page):
    log_page.open()
    log_page.input_user().send_keys(AuthData.problem_user)
    log_page.input_pass().send_keys(AuthData.pass_word)
    log_page.login_btn().click()
    return problem_log


@pytest.fixture()
def glitch_log(log_page):
    log_page.open()
    log_page.input_user().send_keys(AuthData.glitch_user)
    log_page.input_pass().send_keys(AuthData.pass_word)
    log_page.login_btn().click()
    return glitch_log


class LoginPage(BasePage):
    def input_user(self):
        return self.is_visible(AuthLocs.input_user)

    def input_pass(self):
        return self.is_visible(AuthLocs.input_pass)

    def login_btn(self):
        return self.is_clickable(AuthLocs.login_btn)

    @staticmethod
    def locked_msg():
        return AuthLocs.locked_msg

    @staticmethod
    def login_err_msg():
        return AuthLocs.login_err_msg
