from pages.base_page import BasePage
from locators.auth_module import AuthLocs


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
