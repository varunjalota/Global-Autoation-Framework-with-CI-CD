from selenium.common import NoSuchElementException
from Locators.LocatorSignIn import SignInPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class SignInPom:
    def __init__(self, driver):
        self.driver = driver
        self.loc = SignInPageLocators

    def hower_sign_in(self):
        try:
            a = ActionChains(self.driver)
            m = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.loc.HOWER_SIGN_IN_XPATH))
            a.move_to_element(m).perform()
        except NoSuchElementException:
            return False
        return True
