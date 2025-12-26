# SauceDemo Test Automation

### Требования
- Python 3.10.x
- Git

### Установка и запуск

1. **Клонировать проект**
```
git clone <url-репозитория>
cd saucedemo-tests
```

2. **Создать виртуальное окружение**
```
python -m venv venv
.\venv\Scripts\activate  # Windows
```

3. **Установить зависимости**
```
pip install -r requirements.txt
playwright install chromium
```

4. **Запустить тесты**
```
pytest -v
```

5. **Открыть отчет Allure**
```
pytest --alluredir=allure-results
allure serve allure-results
```

### Запуск через Docker (опционально)
```
docker build -t saucedemo-tests .
docker run --rm -v ${PWD}/allure-results:/app/allure-results saucedemo-tests
allure serve allure-results
```

---

## Test Scenarios

1. Успешный логин (standard_user)
2. Логин с неверным паролем
3. Логин заблокированного пользователя (locked_out_user)
4. Логин с пустыми полями
5. Логин пользователем performance_glitch_user (проверить корректный переход и что страница открывается несмотря на возможные задержки)

```