class AuthLocs:
    input_user = ('xpath', '//input[@id="user-name"]')
    input_pass = ('xpath', '//input[@id="password"]')
    login_btn = ('xpath', '//input[@id="login-button"]')

    locked_msg = 'Epic sadface: Sorry, this user has been locked out.'
    login_err_msg = 'Epic sadface: Username and password do not match any user in this service'


class AuthData:
    standard_user = 'standard_user'
    locked_user = 'locked_out_user'
    problem_user = 'problem_user'
    glitch_user = 'performance_glitch_user'

    pass_word = 'secret_sauce'

    wrong_user = 'user'
    wrong_password = 'user'

