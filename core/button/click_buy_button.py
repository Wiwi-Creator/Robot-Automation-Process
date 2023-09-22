from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class click_buy_button:
    
    def click_buy_button(driver, duration, frequency):
        """
        click_buy_button : driver * Int * Float -> None
        click_buy_button(driver) click on buy button. Return None.
        """
        WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='ajouter']")))
        driver.find_elements_by_xpath("//input[@value='ajouter']")[0].click()
        WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='commander']")))
        driver.find_elements_by_xpath("//a[text()='commander']")[0].click()

        return None
