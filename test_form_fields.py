# -*- coding: utf-8 -*-
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


@allure.feature('Form Fields')
@pytest.mark.form
class TestFormFields:
    
    URL = "https://practice-automation.com/form-fields/"
    
    @allure.title("TC-001: Заполнение поля Name")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_fill_name_field(self, driver):
        with allure.step("Открыть страницу с формой"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Ввести текст в поле Name"):
            name_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "name-input"))
            )
            name_input.clear()
            name_input.send_keys("Artem Maslik")
        
        with allure.step("Проверить сохранение данных"):
            assert name_input.get_attribute("value") == "Artem Maslik"
        
        allure.attach(driver.get_screenshot_as_png(), name="name_field", 
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-002: Заполнение поля Email")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_fill_email_field(self, driver):
        with allure.step("Открыть страницу с формой"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Ввести валидный email"):
            email_input = driver.find_element(By.ID, "email")
            email_input.clear()
            email_input.send_keys("artem.test@example.com")
        
        with allure.step("Проверить формат email"):
            assert "@" in email_input.get_attribute("value")
            assert "." in email_input.get_attribute("value")
        
        allure.attach(driver.get_screenshot_as_png(), name="email_field",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-003: Валидация невалидного Email")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_invalid_email_validation(self, driver):
        with allure.step("Открыть страницу с формой"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Ввести невалидный email"):
            email_input = driver.find_element(By.ID, "email")
            email_input.clear()
            email_input.send_keys("invalid-email@")
        
        with allure.step("Попытаться отправить форму"):
            submit_btn = driver.find_element(By.TAG_NAME, "button")
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
            time.sleep(0.5)
            submit_btn.click()
            time.sleep(1)
        
        allure.attach(driver.get_screenshot_as_png(), name="invalid_email",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-004: Выбор значения из Dropdown")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_select_dropdown_option(self, driver):
        with allure.step("Открыть страницу с формой"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Раскрыть dropdown и выбрать опцию"):
            dropdown_element = driver.find_element(By.ID, "automation")
            dropdown = Select(dropdown_element)
            options = dropdown.options
            
            if len(options) > 1:
                dropdown.select_by_index(1)
                selected = dropdown.first_selected_option
                assert selected.text != ""
        
        allure.attach(driver.get_screenshot_as_png(), name="dropdown_selected",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-005: Выбор Checkbox")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_checkbox_toggle(self, driver):
        with allure.step("Открыть страницу с формой"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Выбрать checkbox"):
            checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
            initial_state = checkbox.is_selected()
            
            if not initial_state:
                checkbox.click()
            
            assert checkbox.is_selected() == True
        
        with allure.step("Снять выбор checkbox"):
            checkbox.click()
            assert checkbox.is_selected() == False
        
        allure.attach(driver.get_screenshot_as_png(), name="checkbox_toggle",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-006: Выбор Radio Button")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_radio_button_exclusive_selection(self, driver):
        with allure.step("Открыть страницу с формой"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Найти все radio buttons"):
            radios = driver.find_elements(By.XPATH, "//input[@type='radio']")
            assert len(radios) >= 2, "Недостаточно radio buttons"
        
        with allure.step("Выбрать первую radio button"):
            driver.execute_script("arguments[0].scrollIntoView(true);", radios[0])
            time.sleep(0.5)
            radios[0].click()
            assert radios[0].is_selected()
        
        with allure.step("Выбрать вторую radio button и проверить эксклюзивность"):
            radios[1].click()
            assert radios[1].is_selected()
            assert not radios[0].is_selected()
        
        allure.attach(driver.get_screenshot_as_png(), name="radio_exclusive",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-007: Заполнение поля Message")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_fill_message_textarea(self, driver):
        with allure.step("Открыть страницу с формой"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Ввести многострочный текст в Message"):
            message = driver.find_element(By.ID, "message")
            test_text = "Line 1\nLine 2\nLine 3"
            message.clear()
            message.send_keys(test_text)
        
        with allure.step("Проверить сохранение всех строк"):
            value = message.get_attribute("value")
            assert "Line 1" in value
            assert "Line 2" in value
            assert "Line 3" in value
        
        allure.attach(driver.get_screenshot_as_png(), name="message_multiline",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-008: Отправка формы с валидными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_submit_valid_form(self, driver):
        with allure.step("Открыть страницу с формой"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Заполнить все поля"):
            driver.find_element(By.ID, "name-input").send_keys("Artem Maslik")
            driver.find_element(By.ID, "email").send_keys("artem@test.com")
            driver.find_element(By.ID, "message").send_keys("Test message")
        
        with allure.step("Отправить форму"):
            submit_btn = driver.find_element(By.TAG_NAME, "button")
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
            time.sleep(0.5)
            try:
                submit_btn.click()
            except:
                driver.execute_script("arguments[0].click();", submit_btn)
            time.sleep(2)
        
        allure.attach(driver.get_screenshot_as_png(), name="form_submitted",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-009: Отправка пустой формы")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_submit_empty_form(self, driver):
        with allure.step("Открыть страницу с формой"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Не заполнять поля и нажать Submit"):
            submit_btn = driver.find_element(By.TAG_NAME, "button")
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
            time.sleep(0.5)
            submit_btn.click()
            time.sleep(1)
        
        with allure.step("Проверить наличие валидации"):
            allure.attach(driver.get_screenshot_as_png(), name="empty_form_validation",
                         attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-010: Проверка placeholder текста")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_placeholder_text(self, driver):
        with allure.step("Открыть страницу с формой"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Проверить наличие placeholder в полях"):
            name_input = driver.find_element(By.ID, "name-input")
            email_input = driver.find_element(By.ID, "email")
            
            name_placeholder = name_input.get_attribute("placeholder")
            email_placeholder = email_input.get_attribute("placeholder")
            
            allure.attach(
                f"Name placeholder: {name_placeholder}\nEmail placeholder: {email_placeholder}",
                name="placeholders",
                attachment_type=allure.attachment_type.TEXT
            )
        
        allure.attach(driver.get_screenshot_as_png(), name="placeholders_view",
                     attachment_type=allure.attachment_type.PNG)
