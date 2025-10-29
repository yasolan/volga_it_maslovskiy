# Test Automation Project

Проект автоматизированного тестирования веб-приложений с использованием Selenium, Pytest и Allure Report.

## Описание проекта

Данный проект содержит автоматизированные тесты для проверки функциональности веб-страниц:
- Form Fields - тестирование различных элементов форм
- Click Events - тестирование событий кликов
- Popups - тестирование всплывающих окон и alerts

## Технологический стек

- Python 3.9+
- Selenium WebDriver
- Pytest
- Allure Report
- Page Object Model

## Структура проекта

```
test-automation-practice/
│
├── README.md                          # Главная документация
├── requirements.txt                   # Зависимости проекта
├── pytest.ini                         # Конфигурация pytest
├── conftest.py                       # Общие фикстуры и хуки
│
├── tests/                            # Директория с тестами
│   ├── test_form_fields.py          # Тесты для форм
│   ├── test_click_events.py         # Тесты для событий кликов
│   └── test_popups.py               # Тесты для popup окон
│
├── pages/                            # Page Object Model
│   ├── base_page.py                 # Базовый класс страницы
│   ├── form_page.py                 # Page object для форм
│   ├── click_events_page.py         # Page object для кликов
│   └── popups_page.py               # Page object для popups
│
├── utils/                            # Утилиты
│   └── driver_factory.py            # Фабрика для создания драйверов
│
├── allure-results/                   # Результаты тестов (генерируется)
└── screenshots/                      # Скриншоты (генерируется)
```

## Установка и настройка

### Предварительные требования

1. Python 3.9 или выше
2. Google Chrome или Chromium
3. ChromeDriver (совместимый с версией Chrome)
4. Allure Command Line Tool

### Установка зависимостей

```bash
# Клонирование репозитория
git clone <repository-url>
cd test-automation-practice

# Создание виртуального окружения
python -m venv venv

# Активация виртуального окружения
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt
```

### Установка Allure

**Windows (с использованием Scoop):**
```bash
scoop install allure
```

**macOS (с использованием Homebrew):**
```bash
brew install allure
```

**Linux:**
```bash
# Скачать и распаковать
wget https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.tgz
tar -zxvf allure-2.24.0.tgz
sudo mv allure-2.24.0 /opt/allure
sudo ln -s /opt/allure/bin/allure /usr/bin/allure
```

Проверка установки:
```bash
allure --version
```

## Запуск тестов

### Запуск всех тестов

```bash
pytest tests/ --alluredir=allure-results
```

### Запуск конкретного набора тестов

```bash
# Тесты форм
pytest tests/test_form_fields.py --alluredir=allure-results

# Тесты событий кликов
pytest tests/test_click_events.py --alluredir=allure-results

# Тесты popup окон
pytest tests/test_popups.py --alluredir=allure-results
```

### Запуск с различными опциями

```bash
# Запуск с подробным выводом
pytest tests/ -v --alluredir=allure-results

# Запуск с остановкой на первой ошибке
pytest tests/ -x --alluredir=allure-results

# Запуск конкретного теста
pytest tests/test_form_fields.py::TestFormFields::test_fill_name_field --alluredir=allure-results

# Параллельный запуск (требуется pytest-xdist)
pytest tests/ -n 4 --alluredir=allure-results
```

## Генерация Allure Report

### Просмотр отчета

```bash
# Автоматическое открытие отчета в браузере
allure serve allure-results
```

### Генерация статического отчета

```bash
# Генерация отчета в папку allure-report
allure generate allure-results -o allure-report --clean

# Открытие сгенерированного отчета
allure open allure-report
```

## Тест-кейсы

### 1. Form Fields Testing

| ID | Название | Приоритет | Описание |
|----|----------|-----------|----------|
| TC-001 | Заполнение текстового поля Name | Высокий | Проверка ввода текста в поле Name |
| TC-002 | Заполнение поля Email | Высокий | Проверка ввода валидного email |
| TC-003 | Выбор значения из Dropdown | Средний | Проверка выбора опции из выпадающего списка |
| TC-004 | Выбор Checkbox | Средний | Проверка выбора чекбокса |
| TC-005 | Выбор Radio Button | Средний | Проверка эксклюзивного выбора радиокнопки |
| TC-006 | Заполнение поля Message | Средний | Проверка ввода в textarea |
| TC-007 | Отправка формы | Критический | Проверка отправки формы с валидными данными |

### 2. Click Events Testing

| ID | Название | Приоритет | Описание |
|----|----------|-----------|----------|
| TC-008 | Single Click Event | Высокий | Проверка обработки одиночного клика |
| TC-009 | Double Click Event | Высокий | Проверка обработки двойного клика |
| TC-010 | Right Click Event | Средний | Проверка обработки правого клика мыши |

### 3. Popups Testing

| ID | Название | Приоритет | Описание |
|----|----------|-----------|----------|
| TC-011 | Alert Popup | Высокий | Проверка обработки alert окна |
| TC-012 | Confirm Popup (Accept) | Высокий | Проверка принятия confirm окна |
| TC-013 | Confirm Popup (Dismiss) | Средний | Проверка отклонения confirm окна |
| TC-014 | Prompt Popup | Средний | Проверка ввода данных в prompt |
| TC-015 | Tooltip | Низкий | Проверка отображения tooltip |

## Особенности реализации

### Page Object Model

Проект использует паттерн Page Object Model для улучшения поддерживаемости тестов:

```python
# Пример использования
from pages.form_page import FormPage

def test_submit_form(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_name("Test User")
    form_page.fill_email("test@example.com")
    form_page.submit_form()
    assert form_page.is_success_message_displayed()
```

### Автоматические скриншоты при падении тестов

Проект автоматически создает скриншоты при падении тестов. Скриншоты прикрепляются к Allure Report.

```python
# В conftest.py
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
```

### Явные ожидания

Все тесты используют явные ожидания вместо time.sleep():

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "element-id"))
)
```

### Обработка всплывающих окон

```python
# Alert
alert = driver.switch_to.alert
alert_text = alert.text
alert.accept()

# Confirm
confirm = driver.switch_to.alert
confirm.dismiss()

# Prompt
prompt = driver.switch_to.alert
prompt.send_keys("Input text")
prompt.accept()
```

## Конфигурация

### pytest.ini

```ini
[pytest]
addopts = -v --alluredir=allure-results --clean-alluredir
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
markers =
    smoke: Smoke tests
    regression: Regression tests
    form: Form testing
    clicks: Click events testing
    popups: Popup testing
```

### requirements.txt

```
selenium==4.15.0
pytest==7.4.3
allure-pytest==2.13.2
pytest-xdist==3.5.0
webdriver-manager==4.0.1
```

## CI/CD Integration

### GitHub Actions

```yaml
name: Automated Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest tests/ --alluredir=allure-results
    - name: Generate Allure Report
      if: always()
      run: |
        allure generate allure-results -o allure-report
    - name: Upload Allure Report
      if: always()
      uses: actions/upload-artifact@v3
      with:
        name: allure-report
        path: allure-report
```

## Troubleshooting

### ChromeDriver не найден

```bash
# Установка webdriver-manager для автоматического управления драйверами
pip install webdriver-manager

# Использование в коде
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
```

### Элемент не найден

```python
# Использование множественных локаторов
locators = [
    (By.ID, "element-id"),
    (By.CSS_SELECTOR, ".element-class"),
    (By.XPATH, "//div[@class='element']")
]

for by_type, locator in locators:
    try:
        element = driver.find_element(by_type, locator)
        break
    except NoSuchElementException:
        continue
```

### Element Click Intercepted

```python
# Использование JavaScript click
driver.execute_script("arguments[0].click();", element)

# Или прокрутка к элементу
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(0.5)
element.click()
```

## Лучшие практики

1. Использовать Page Object Model для организации кода
2. Применять явные ожидания вместо time.sleep()
3. Создавать независимые тесты (один тест - одна проверка)
4. Использовать понятные названия тестов
5. Добавлять подробные сообщения об ошибках
6. Делать скриншоты при падении тестов
7. Использовать фикстуры для подготовки данных
8. Группировать тесты с помощью маркеров pytest
9. Документировать тесты и добавлять описания в Allure
10. Регулярно обновлять зависимости

## Дополнительные ресурсы

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Report Documentation](https://docs.qameta.io/allure/)
- [Page Object Model Pattern](https://selenium-python.readthedocs.io/page-objects.html)

## Контакты

Для вопросов и предложений:
- Email: artem.maslik2007@gmail.com
- GitHub: [Your GitHub Profile]

## Лицензия

MIT License
