from six import reraise
from sys import exc_info
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class processing:
    """
    Auto fill and click to the submit button, to process the paiment.
    """
    def auto_fill(driver, name, email, tel, adress_1, adress_2, ville, postal, pays, card_number, exp_month, exp_year, cvv):
        """
        auto_fill : driver * Str * Str * Str * Str * Str * Str * Str * Str * Str * Str -> None
        auto_fill(driver) click on payment option and auto fill. Return None.
        """
        driver.find_element_by_xpath("//input[@name='order[billing_name]']").send_keys(name)
        driver.find_element_by_xpath("//input[@name='order[email]']").send_keys(email)
        driver.find_element_by_xpath("//input[@name='order[tel]']").send_keys(tel)
        driver.find_element_by_xpath("//input[@name='order[billing_address]']").send_keys(adress_1)
        driver.find_element_by_xpath("//input[@name='order[billing_address_2]']").send_keys(adress_2)
        driver.find_element_by_xpath("//input[@name='order[billing_city]']").send_keys(ville)
        driver.find_element_by_xpath("//input[@name='order[billing_zip]']").send_keys(postal)
        driver.find_element_by_xpath("//option[@value='FR']").click()
        driver.find_element_by_xpath("//input[@name='credit_card[cnb]']").send_keys(card_number)
        driver.find_element_by_xpath("//option[@value='{}']".format(exp_month)).click()
        driver.find_element_by_xpath("//option[@value='{}']".format(exp_year)).click()
        driver.find_element_by_xpath("//input[@name='credit_card[ovv]']").send_keys(cvv)

        return None

    def click_submit_button(driver, duration, frequency):
        """
        click_submit_button : driver * Int * Float -> None
        click_submit_button(driver) click on submit button. Return None.
        """
        try:
            WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='icheckbox_minimal checked']")))
            driver.find_element_by_xpath("//input[@name='commit']").click()

        except Exception as e:
            reraise(Exception, e, exc_info()[2])

        return None