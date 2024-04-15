class InventoryLocs:
    prod_header = ('xpath', '//div[@class="product_label"]')

    item_cards = ('xpath', '//div[@class="inventory_item"]')
    item_imgs = ('xpath', '//img[@class="inventory_item_img"]')
    item_names = ('xpath', '//div[@class="inventory_item_name"]')
    item_descs = ('xpath', '//div[@class="inventory_item_desc"]')
    item_prices = ('xpath', '//div[@class="inventory_item_price"]')

    add_btns = ('xpath', '//button[@class="btn_primary btn_inventory"]')
    remove_btns = ('xpath', '//button[@class="btn_secondary btn_inventory"]')


