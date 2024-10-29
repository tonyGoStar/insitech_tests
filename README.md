# insitech_tests

-----------------------------------------------------------------------------
Для запуска автотестов необходимо:

1. Проверить, что установлен интерпритатор Python (python --version)
2. Установить зависимости командой pip install -r requirements.txt
3. Запустить тесты из необходимой директории (api_tests или selenium_tests) командой
    pytest или pytest [путь к файлу тестов] 

-----------------------------------------------------------------------------
Тест-кейсы:
-----------------------------------------------------------------------------

1. Отображение главной страницы. (так как тест-кейсов всего 5, один будет общий Health-check)
    1) Перейти на страницу https://opm-website.iot-asm-test1.insitech.live/ .
    2) Убедиться, что загружена главная страница и на ней корректно отрисованы
    все элементы.

    Ожидаемый результат: на главной странице все элементы отрисованы корректно,
    все кликабельные элементы по клику открывают соответствующие страницы и модальные окна.
-----------------------------------------------------------------------------
2. Добавление в избранное.
    1) Перейти на страницу https://opm-website.iot-asm-test1.insitech.live/ .
    2) Кликнуть на иконку девайса планшет.
    3) Убедиться, что произошел переход на странницу конструктора по планшетам.
    4) Выбрать любую модель.
    5) Убедиться, что перешли на этап настройки параметров товара.
    6) Кликнуть на кнопку "В избранное".

    Ожидаемый результат: Появилось зеленое всплывающее уведомление "Добавлено в избранное"
    и при переходе на страницу избранного товар корректно отображается в избранном.

-----------------------------------------------------------------------------
3. Добавление товара в корзину.
    Предусловия: Необходимо находиться на странице настройки параметров товара.
    1) Выставить все обязательные параметры товара.
    2) Нажать на кнопку "В корзину".
    3) Перейти на страницу "Корзина".

    Ожидаемый результат: на странице "Корзина" корректно отображается необходимый товар.

-----------------------------------------------------------------------------
4. Оформление заказа.
    Предусловия: Необходимо находиться на странице Корзина" с товаром для заказа.
    1) Кликнуть на поле ввода "Выберите пункт".
    2) В открывшемся модальном окне выбрать пункт.
    3) Нажать кнопку "Подтвердить".
    4) Нажать кнопку "Заказать".

    Ожидаемый результат: Отображено модальное окно "Заказ сохранен" с номером заказа,
    на странице заказов корректно отображен заказ с актуальным статусом и возможностью 
    отменить его.

-----------------------------------------------------------------------------
5. Поиск по сайту.
    1) Перейти на страницу https://opm-website.iot-asm-test1.insitech.live/ .
    2) Кликнуть в поле ввода поиска "Найти".
    3) Ввести текст "iphone 15 pro max".
    4) Нажать на необходимую модель смартфона в выпавшем списке.

    Ожидаемый результат: Перешли на странницу конструктора заказа по выбранной модели. 

-----------------------------------------------------------------------------
