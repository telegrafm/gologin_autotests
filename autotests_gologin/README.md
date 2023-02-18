Что делают тесты? 

- авторизуются по Barer токену
- выполняют precondition где сохраняют user_id для дальнейшего переиспользования
- запрашивают инфо по юзеру, по профилю
- создают новый профиль
- сохранют id профиля
- удаляют созадный профиль по его id

- Как быстро развернуть тесты и построить отчет о тестировании ? 

pip ставится с python

pip install virtualenv

virtualenv env - создает виртуальное окружение

. env/bin/activate - активируем venv

where python - проверяем активацию

pip3 install -r requirements.txt

Запустить тесты локально на macOS:

Склонировать проект на локальную машину
Установить Pycharm
Установка плагинов(открыть в pycharm Terminal), запустить команду:
pip install allure-pytest
pip install pytest
pip install pytest-ordering
pip install pytest-random-order
Либо все плагины можно установить напрямую из файла: requirements.txt

Pytest - фреймворк для управления запуском автотестов, аналог TestNG:

- Команда для запуска smoke теста:
ex:  pytest -q autotests_gologin/tests/api_tests_smoke.py 

  
Настройка и запуска отчета allure:

$ pip install allure-pytest

$ py.test --alluredir=autotests_gologin/tests/allure_reports autotests_gologin/tests/api_tests_smoke.py

$  allure serve autotests_gologin/tests/allure_reports
allure generate (папка reports_allure) -o /tmp/allure/ --clean Генерация отчета
allure open /tmp/allure - #открыть отчет Если на локальной машине есть проблемы с запуском теста тот попробовать напрямую передать host и port ex: allure serve reports_allure --host localhost --port 9999


