from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.soldout import soldout_color_testing


def process_loop(driver, break_condition, incrementation, duration, frequency, process_loop_break_condition):
    """
    process_loop : Full data -> None
    process_loop(...) initiates the selection process, in an iterable version of the program. Return None.
    """
    driver.get("https://www.supremenewyork.com/shop/all")

    WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='add-remove-buttons']/a")))

    break_condition = soldout_color_testing.select_color(driver, break_condition, incrementation, process_loop_break_condition)

    if break_condition == 1:
        break_condition = 0
        process_loop(driver, break_condition, incrementation, duration, frequency, process_loop_break_condition)

    return None
