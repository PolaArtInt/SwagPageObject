### test-case: 0.1  
## Разблокирование кнопки  
Проверка разблокировки кнопки регистрации после заполнения чекбокса 
#### Test:  
test_0_form.py::  
test_register_btn_unblocked  
#### Предусловие:  
Открыть url: https://victoretc.github.io/webelements_information/  
Пустые поля формы  
#### Шаги:  
1. Ввести 'John Doe' в 'Name'  
2. Ввести '@pass12345*!' в 'Password'  
3. Отметить чекбокс  
#### Ожидаемый результат:   
Кнопка 'Register' разблокирована  
#### Постусловие:  
Вернуться на страницу:  
https://victoretc.github.io/webelements_information/  

----------------------------------------------------------------

### test-case: 0.2  
## Корректное поведение формы  
Проверка заполнения всех полей и формы и нажатие на кнопку 'Register'  
#### Test:  
test_0_form.py::  
test_positive_fill_form_fields  
#### Предусловие:  
Открыть url: https://victoretc.github.io/webelements_information/  
Пустые поля формы  
#### Шаги:  
1. Ввести 'John Doe' в 'Name'  
2. Ввести '@pass12345*!' в 'Password'  
3. Отметить чекбокс  
4. Нажать на кнопку 'Register'  
#### Ожидаемый результат:   
Url меняется на какой-то другой  
#### Постусловие:  
Вернуться на страницу:  
https://victoretc.github.io/webelements_information/  

----------------------------------------------------------------

### test-case: 0.3  
## Ввод некорректных данных в поле 'Name'  
Попытка зарегестрироваться с некорректным именем  
#### Test: DEFECT FOUND  
test_0_form.py::  
test_negative_fill_name_with_spaces  
#### Предусловие:  
Открыть url: https://victoretc.github.io/webelements_information/  
Пустые поля формы  
#### Шаги:  
1. Ввести '  ' в 'Name'  
2. Ввести '@pass12345*!' в 'Password'  
3. Отметить чекбокс    
#### Ожидаемый результат:  
Кнопка не активна  
Сообщение о некорректном значении поля 'Name'  
#### Постусловие:  
Вернуться на страницу:  
https://victoretc.github.io/webelements_information/  

----------------------------------------------------------------

### test-case: 0.4  
## Отсутствие ввода в поле 'Name' и 'Password'  
Попытка зарегестрироваться с пустыми полями формы  
#### Test: DEFECT FOUND  
test_0_form.py::  
test_btn_blocked_with_empty_fields  
#### Предусловие:  
Открыть url: https://victoretc.github.io/webelements_information/  
Пустые поля формы  
#### Шаги:  
1. Оставить поля 'Name' и 'Password' пустыми  
2. Отметить чекбокс  
#### Ожидаемый результат:   
Кнопка 'Register' заблокирована  
#### Постусловие:  
Вернуться на страницу:  
https://victoretc.github.io/webelements_information/  

----------------------------------------------------------------
