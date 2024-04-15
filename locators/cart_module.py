class CartLocs:
    # cart icon:
    cart_header = ('xpath', '//div[@class="subheader"]')
    cart_btn = ('xpath', '//a[@class="shopping_cart_link fa-layers fa-fw"]')
    cart_tag = ('xpath', '//a[@class="shopping_cart_link fa-layers fa-fw"]/span')

    # item details:
    cart = ('xpath', '//div[@id="cart_contents_container"]')
    cart_quantity_num = ('xpath', '//div[@class="cart_quantity"]')
    cart_remove_btn = ('xpath', '//button[@class="btn_secondary cart_button"]')
