# -*- coding: utf-8 -*-
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@allure.feature('Click Events')
@pytest.mark.clicks
class TestClickEvents:
    
    URL = "https://practice-automation.com/click-events/"
    
    @allure.title("TC-011: Single Click Event")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_single_click(self, driver):
        with allure.step("Открыть страницу событий кликов"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Найти элемент для single click"):
            buttons = driver.find_elements(By.TAG_NAME, "button")
            assert len(buttons) > 0, "Кнопки не найдены"
        
        with allure.step("Выполнить одиночный клик"):
            element = buttons[0]
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.5)
            element.click()
            time.sleep(1)
        
        allure.attach(driver.get_screenshot_as_png(), name="single_click",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-012: Double Click Event")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_double_click(self, driver):
        with allure.step("Открыть страницу событий кликов"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Найти элемент для double click"):
            buttons = driver.find_elements(By.TAG_NAME, "button")
            element = buttons[1] if len(buttons) > 1 else buttons[0]
        
        with allure.step("Выполнить двойной клик"):
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.5)
            actions = ActionChains(driver)
            actions.double_click(element).perform()
            time.sleep(1)
        
        allure.attach(driver.get_screenshot_as_png(), name="double_click",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-013: Right Click Event")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_right_click(self, driver):
        with allure.step("Открыть страницу событий кликов"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Найти элемент для right click"):
            buttons = driver.find_elements(By.TAG_NAME, "button")
            element = buttons[2] if len(buttons) > 2 else buttons[0]
        
        with allure.step("Выполнить правый клик"):
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.5)
            actions = ActionChains(driver)
            actions.context_click(element).perform()
            time.sleep(1)
        
        allure.attach(driver.get_screenshot_as_png(), name="right_click",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-014: Click Counter")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_click_counter(self, driver):
        with allure.step("Открыть страницу событий кликов"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Кликнуть на элемент несколько раз"):
            buttons = driver.find_elements(By.TAG_NAME, "button")
            if buttons:
                element = buttons[0]
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(0.5)
                
                for i in range(5):
                    element.click()
                    time.sleep(0.3)
        
        with allure.step("Проверить счетчик кликов"):
            allure.attach(driver.get_screenshot_as_png(), name="click_counter",
                         attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-015: Click and Hold")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_click_and_hold(self, driver):
        with allure.step("Открыть страницу событий кликов"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Найти элемент и выполнить click and hold"):
            buttons = driver.find_elements(By.TAG_NAME, "button")
            if buttons:
                element = buttons[0]
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(0.5)
                
                actions = ActionChains(driver)
                actions.click_and_hold(element).perform()
                time.sleep(2)
                actions.release(element).perform()
                time.sleep(1)
        
        allure.attach(driver.get_screenshot_as_png(), name="click_hold",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-016: Видимость кликабельных элементов")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_elements_visibility(self, driver):
        with allure.step("Открыть страницу событий кликов"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Найти все кликабельные элементы"):
            buttons = driver.find_elements(By.TAG_NAME, "button")
            links = driver.find_elements(By.TAG_NAME, "a")
            clickable = buttons + links
        
        with allure.step("Проверить видимость элементов"):
            visible_count = sum(1 for elem in clickable if elem.is_displayed())
            
            allure.attach(
                f"Всего кликабельных: {len(clickable)}\nВидимых: {visible_count}",
                name="visibility_info",
                attachment_type=allure.attachment_type.TEXT
            )
            
            assert visible_count > 0, "Нет видимых элементов"
        
        allure.attach(driver.get_screenshot_as_png(), name="elements_visible",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-017: Disabled элемент")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_disabled_element(self, driver):
        with allure.step("Открыть страницу событий кликов"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Найти disabled элемент"):
            disabled_elements = driver.find_elements(
                By.CSS_SELECTOR, "button[disabled], input[disabled]"
            )
        
        with allure.step("Проверить невозможность клика"):
            if disabled_elements:
                element = disabled_elements[0]
                is_disabled = element.get_attribute("disabled")
                assert is_disabled is not None, "Элемент не disabled"
                
                allure.attach(
                    f"Найдено disabled элементов: {len(disabled_elements)}",
                    name="disabled_count",
                    attachment_type=allure.attachment_type.TEXT
                )
        
        allure.attach(driver.get_screenshot_as_png(), name="disabled_element",
                     attachment_type=allure.attachment_type.PNG)
    
    @allure.title("TC-018: Hover эффект")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_hover_effect(self, driver):
        with allure.step("Открыть страницу событий кликов"):
            driver.get(self.URL)
            time.sleep(2)
        
        with allure.step("Найти элемент с hover эффектом"):
            buttons = driver.find_elements(By.TAG_NAME, "button")
            if not buttons:
                buttons = driver.find_elements(By.TAG_NAME, "a")
        
        with allure.step("Навести курсор на элемент"):
            if buttons:
                element = buttons[0]
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(0.5)
                
                actions = ActionChains(driver)
                actions.move_to_element(element).perform()
                time.sleep(2)
        
        with allure.step("Проверить изменение стиля"):
            allure.attach(driver.get_screenshot_as_png(), name="hover_effect",
                         attachment_type=allure.attachment_type.PNG)
