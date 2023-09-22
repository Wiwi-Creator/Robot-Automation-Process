from selenium.webdriver.chrome.options import Options


class add_argument:
    """
    Disable Blink features and automation indicator to imitate human interaction with navigator. Return Options.
    """
    def add_argument_options():
        """
        add_argument_options : None -> Options()
        add_argument_options() Disable Blink features and automation indicator to imitate human interaction with navigator. Return Options.
        """
        chrome_options = Options()
        chrome_options.add_argument("--kiosk")
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-blink-features")
        chrome_options.add_argument('--profile-directory=Default')
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        return chrome_options