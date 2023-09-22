from core.button.process import processing
from core.button.click_buy_button import click_buy_button
from config.add_argument import add_argument
from task.operator import process_loop
from time import sleep
from selenium import webdriver
from config import BasicSettings
import chromedriver_autoinstaller


def main():
    duration = 300
    frequency = 0.01
    break_condition = 0
    process_loop_break_condition = 0
    incrementation = 1
    chromedriver_autoinstaller.install()
    chrome_options = add_argument.add_argument_options()
    driver = webdriver.Chrome(options=chrome_options)

    driver.set_page_load_timeout(60)

    process_loop(driver, break_condition, incrementation, duration, frequency, process_loop_break_condition)
    click_buy_button(driver, duration, frequency)
    processing.auto_fill(driver, BasicSettings.NAME, BasicSettings.EMAIL, BasicSettings.TEL, BasicSettings.ADRESS_1, BasicSettings.ADRESS_2, BasicSettings.VILLE, BasicSettings.POSTAL, BasicSettings.PAYS, BasicSettings.CARD_NUMBER, BasicSettings.EXP_MONTH, BasicSettings.EXP_YEAR, BasicSettings.CVV)
    processing.click_submit_button(driver, duration, frequency)
    sleep(200)


if __name__ == '__main__':
    main()