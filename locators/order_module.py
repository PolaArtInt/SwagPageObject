class OrderLocs:
    input_fname = ('xpath', '//input[@id="first-name"]')
    input_lname = ('xpath', '//input[@id="last-name"]')
    input_zipcode = ('xpath', '//input[@id="postal-code"]')

    checkout_btn = ('xpath', '//a[@class="btn_action checkout_button"]')
    continue_btn = ('xpath', '//input[@class="btn_primary cart_button"]')
    finish_btn = ('xpath', '//a[@class="btn_action cart_button"]')
    cancel_btn = ('xpath', '//a[@class="cart_cancel_link btn_secondary"]')

    complete_msg = 'THANK YOU FOR YOUR ORDER'
