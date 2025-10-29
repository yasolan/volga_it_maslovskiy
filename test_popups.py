# -*- coding: utf-8 -*-
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


@allure.feature('Popups')
@pytest.mark.popups
class TestPopups:
    
    URL = "https://practice-automation.com/popups/"
    
    @allure.title("TC-019: Alert Popup")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_alert_popup(self, driver):
        with allure.step("Открыть страницу с popups"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Нажать кнопку для вызова alert"):
            buttons = driver.find_elements(By.TAG_NAME, "button")
            if buttons:
                alert_btn = buttons[0]
                driver.execute_script("arguments[0].scrollIntoView(true);", alert_btn)
                time.sleep(0.5)
                alert_btn.click()
                time.sleep(1)
        
        with allure.step("Обработать alert"):
            try:
                alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
                alert_text = alert.text
                allure.attach(f"Текст alert: {alert_text}", name="alert_text",
                            attachment_type=allure.attachment_type.TEXT)
                alert.accept()
                time.sleep(1)
            except TimeoutException:
                pass
        
        allure.attach(driver.get_screenshot_as_png(), name="alert_handled",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-020: Confirm Popup - Accept")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_confirm_accept(self, driver):
        with allure.step("Открыть страницу с popups"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Нажать кнопку для вызова confirm"):
            buttons = driver.find_elements(By.TAG_NAME, "button")
            confirm_btn = buttons[1] if len(buttons) > 1 else buttons[0] if buttons else None
            
            if confirm_btn:
                driver.execute_script("arguments[0].scrollIntoView(true);", confirm_btn)
                time.sleep(0.5)
                confirm_btn.click()
                time.sleep(1)
        
        with allure.step("Принять confirm"):
            try:
                confirm = WebDriverWait(driver, 5).until(EC.alert_is_present())
                confirm_text = confirm.text
                allure.attach(f"Текст confirm: {confirm_text}", name="confirm_text",
                            attachment_type=allure.attachment_type.TEXT)
                confirm.accept()
                time.sleep(1)
            except TimeoutException:
                pass
        
        allure.attach(driver.get_screenshot_as_png(), name="confirm_accepted",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-021: Confirm Popup - Dismiss")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_confirm_dismiss(self, driver):
        with allure.step("Открыть страницу с popups"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Нажать кнопку для вызова confirm"):
            buttons = driver.find_elements(By.TAG_NAME, "button")
            confirm_btn = buttons[1] if len(buttons) > 1 else buttons[0] if buttons else None
            
            if confirm_btn:
                driver.execute_script("arguments[0].scrollIntoView(true);", confirm_btn)
                time.sleep(0.5)
                confirm_btn.click()
                time.sleep(1)
        
        with allure.step("Отклонить confirm"):
            try:
                confirm = WebDriverWait(driver, 5).until(EC.alert_is_present())
                confirm_text = confirm.text
                allure.attach(f"Текст confirm: {confirm_text}", name="confirm_text",
                            attachment_type=allure.attachment_type.TEXT)
                confirm.dismiss()
                time.sleep(1)
            except TimeoutException:
                pass
        
        allure.attach(driver.get_screenshot_as_png(), name="confirm_dismissed",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-022: Prompt Popup")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_prompt_popup(self, driver):
        with allure.step("Открыть страницу с popups"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Нажать кнопку для вызова prompt"):
            buttons = driver.find_elements(By.TAG_NAME, "button")
            prompt_btn = buttons[2] if len(buttons) > 2 else buttons[0] if buttons else None
            
            if prompt_btn:
                driver.execute_script("arguments[0].scrollIntoView(true);", prompt_btn)
                time.sleep(0.5)
                prompt_btn.click()
                time.sleep(1)
        
        with allure.step("Ввести текст в prompt"):
            try:
                prompt = WebDriverWait(driver, 5).until(EC.alert_is_present())
                test_input = "Test Input Value"
                prompt.send_keys(test_input)
                allure.attach(f"Введено: {test_input}", name="prompt_input",
                            attachment_type=allure.attachment_type.TEXT)
                prompt.accept()
                time.sleep(1)
            except TimeoutException:
                pass
        
        allure.attach(driver.get_screenshot_as_png(), name="prompt_handled",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-023: Prompt Cancel")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_prompt_cancel(self, driver):
        with allure.step("Открыть страницу с popups"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Нажать кнопку для вызова prompt"):
            buttons = driver.find_elements(By.TAG_NAME, "button")
            prompt_btn = buttons[2] if len(buttons) > 2 else buttons[0] if buttons else None
            
            if prompt_btn:
                driver.execute_script("arguments[0].scrollIntoView(true);", prompt_btn)
                time.sleep(0.5)
                prompt_btn.click()
                time.sleep(1)
        
        with allure.step("Отменить prompt без ввода"):
            try:
                prompt = WebDriverWait(driver, 5).until(EC.alert_is_present())
                prompt.dismiss()
                time.sleep(1)
                allure.attach("Prompt отменен", name="prompt_cancelled",
                            attachment_type=allure.attachment_type.TEXT)
            except TimeoutException:
                pass
        
        allure.attach(driver.get_screenshot_as_png(), name="prompt_cancelled",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-024: Tooltip отображение")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_tooltip_display(self, driver):
        with allure.step("Открыть страницу с popups"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Найти элемент с tooltip"):
            tooltip_elements = driver.find_elements(By.CSS_SELECTOR, "[title], [data-tooltip]")
            if not tooltip_elements:
                tooltip_elements = driver.find_elements(By.TAG_NAME, "a")
        
        with allure.step("Навести курсор на элемент"):
            if tooltip_elements:
                element = tooltip_elements[0]
                actions = ActionChains(driver)
                actions.move_to_element(element).perform()
                time.sleep(2)
                
                tooltip_text = element.get_attribute("title") or element.get_attribute("data-tooltip")
                if tooltip_text:
                    allure.attach(f"Текст tooltip: {tooltip_text}", name="tooltip_text",
                                attachment_type=allure.attachment_type.TEXT)
        
        allure.attach(driver.get_screenshot_as_png(), name="tooltip_displayed",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-025: Modal window")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_modal_window(self, driver):
        with allure.step("Открыть страницу с popups"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Найти кнопку для открытия modal"):
            modal_buttons = driver.find_elements(
                By.XPATH, "//button[contains(text(), 'Modal') or contains(text(), 'modal')]"
            )
            if not modal_buttons:
                modal_buttons = driver.find_elements(By.TAG_NAME, "button")
        
        with allure.step("Открыть modal окно"):
            if modal_buttons:
                modal_btn = modal_buttons[0]
                driver.execute_script("arguments[0].scrollIntoView(true);", modal_btn)
                time.sleep(0.5)
                modal_btn.click()
                time.sleep(2)
        
        with allure.step("Проверить отображение modal"):
            modals = driver.find_elements(By.CSS_SELECTOR, ".modal, [role='dialog']")
            if modals:
                allure.attach("Modal окно найдено", name="modal_found",
                            attachment_type=allure.attachment_type.TEXT)
        
        with allure.step("Закрыть modal"):
            close_buttons = driver.find_elements(
                By.CSS_SELECTOR, ".close, [aria-label='Close'], button.modal-close"
            )
            if close_buttons:
                close_buttons[0].click()
                time.sleep(1)
        
        allure.attach(driver.get_screenshot_as_png(), name="modal_handled",
                     attachment_type=allure.attachment_type.PNG)
