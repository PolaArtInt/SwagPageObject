## Autotests for Swag Labs site  
  
# Site URL: https://www.saucedemo.com/v1  
Функционал, который необходимо покрыть автотестами:  
## Авторизация:  
test-cases_1_auth.md  
test_1_auth.py  
1.Авторизация используя корректные данные (standard_user, secret_sauce): case 1.1  
2.Авторизация используя корректные данные (locked_out_user, secret_sauce): case 1.2  
3.Авторизация используя корректные данные (problem_user, secret_sauce): case 1.3  
4.Авторизация используя корректные данные (performance_glitch_user, secret_sauce): case 1.4  
5.Авторизация используя некорректные данные (user, user): case 1.5  
  
## Корзина:  
test-cases_2_cart.md  
test_2_cart.py  
1.Добавление товара в корзину через каталог: case 2.1  
2.Удаление товара из корзины через корзину: case 2.2  
3.Добавление товара в корзину из карточки товара: case 2.3  
4.Удаление товара из корзины через карточку товара: case 2.4  
  
## Карточка товара:  
test-cases_3_item_card.md  
test_3_item_card.py  
1.Успешный переход к карточке товара после клика на картинку товара: case 3.1  
2.Успешный переход к карточке товара после клика на название товара: case 3.2  
  
## Оформление заказа:  
test-cases_4_order.md  
test_4_order.py  
1.Оформление заказа используя корректные данные: case 4.1  
  
## Фильтр:  
test-cases_5_filter.md  
test_5_filter.py  
1.Проверка работоспособности фильтра (A to Z): case 5.1  
2.Проверка работоспособности фильтра (Z to A): case 5.2  
3.Проверка работоспособности фильтра (low to high): case 5.3  
4.Проверка работоспособности фильтра (high to low): case 5.4  
  
## Бургер меню:  
test-cases_6_menu.md  
test_6_menu.py  
1.Выход из системы: case 6.1  
2.Проверка работоспособности кнопки "About" в меню: case 6.2  
3.Проверка работоспособности кнопки "Reset App State": case 6.3  
4.Негативная проверка кнопки: case 6.4 DEFECT FOUND  
  
## Повторяющиеся картинки в инвентаре problem_user:  
test_7_problem_user.py  
1.Негативная проверка картинок в инвентаре: case 7.1 DEFECT FOUND  
  
