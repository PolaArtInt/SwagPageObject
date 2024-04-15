### test-case: 1.1  
## Авторизация::standard_user  
Авторизация используя корректные данные  
#### Test:  
test_1_login.py::  
test_auth_positive  
#### Предусловие:  
Открыть url: https://www.saucedemo.com/v1    
#### Шаги:  
1. Ввести 'standard_user' в 'Username'  
2. Ввести 'secret_sauce' в 'Password'  
3. Кликнуть 'Login'  
#### Ожидаемый результат:  
Переход на новый url:  
https://www.saucedemo.com/inventory.html  
Заголовок страницы: 'Products'  
#### Постусловие: -  

----------------------------------------------------------------

### test-case: 1.2  
## Авторизация::locked_out_user  
Авторизация заблокированного пользователя  
#### Test:  
test_1_login.py::  
test_auth_positive_locked_out_user  
#### Предусловие:  
Открыть url: https://www.saucedemo.com/v1    
#### Шаги:  
1. Ввести 'locked_out_user' в 'Username'  
2. Ввести 'secret_sauce' в 'Password'  
3. Кликнуть 'Login'  
#### Ожидаемый результат:  
Появление сообщения об ошибке: 'Epic sadface: Sorry, this user has been locked out.'  
Нахождение на том же url: https://www.saucedemo.com/  
#### Постусловие: -  

----------------------------------------------------------------

### test-case: 1.3  
## Авторизация::problem_user  
Авторизация проблемного пользователя  
#### Test:  
test_1_login.py::  
test_auth_positive_problem_user  
#### Предусловие:  
Открыть url: https://www.saucedemo.com/v1  
#### Шаги:  
1. Ввести 'problem_user' в 'Username'  
2. Ввести 'secret_sauce' в 'Password'  
3. Кликнуть 'Login'  
#### Ожидаемый результат:  
Переход на новый url:  
https://www.saucedemo.com/inventory.html  
Заголовок страницы: 'Products'  
#### Постусловие: -  

----------------------------------------------------------------

### test-case: 1.3.1  
## Отображение картинок  
Проверка наличия изображений в каталоге  
#### Test: DEFECT FOUND  
test_1_login.py::  
test_problem_user_negative_inventory_imgs  
#### Предусловие:  
Авторизация problem auth  
#### Шаги:  
1. Найти все картинки товаров в каталоге  
2. Проверить атрибуты 'src' картинок  
#### Ожидаемый результат:  
У всех картинок поломан url  
#### Постусловие: -  

----------------------------------------------------------------

### test-case: 1.4  
## Авторизация::performance_glitch  
Авторизация со сбоем производительности  
#### Test:  
test_1_login.py::  
test_auth_positive_performance_glitch_user  
#### Предусловие:  
Открыть url: https://www.saucedemo.com/v1  
#### Шаги:  
1. Ввести 'performance_glitch_user' в 'Username'  
2. Ввести 'secret_sauce' в 'Password'  
3. Кликнуть 'Login'  
#### Ожидаемый результат:  
Переход с задержкой на новый url:  
https://www.saucedemo.com/inventory.html  
Заголовок страницы: 'Products'  
#### Постусловие: -  

----------------------------------------------------------------

### test-case: 1.5  
## Авторизация::wrong_login  
Авторизация используя некорректные данные  
#### Test:  
test_1_login.py::  
test_auth_negative_wrong_login  
#### Предусловие:  
Открыть url: https://www.saucedemo.com/v1  
#### Шаги:  
1. Ввести 'user' в 'Username'  
2. Ввести 'user' в 'Password'  
3. Кликнуть 'Login'  
#### Ожидаемый результат:  
Появление сообщения об ошибке:  
'Epic sadface: Username and password do not match any user in this service'  
Нахождение на том же url: https://www.saucedemo.com/  
#### Постусловие: -  

----------------------------------------------------------------
