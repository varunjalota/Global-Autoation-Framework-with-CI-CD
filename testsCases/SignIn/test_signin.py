import time
from datetime import date

import allure
from allure_commons.types import AttachmentType
from utilities.readProperties import ReadConfig
from Logger.customLogger import LogGen
from PageObject.Signin import SignInPom


class TestSignIn:
    baseURL = ReadConfig.getapplicationurl()
    logger = LogGen.loggen()
    day = date.today()
    today = day.strftime("%B %d, %Y")

    def test_hover_sign_in(self, setup):
        """ Check for Email Field available """
        self.logger.info("**** Test for Checking Email Field available ****")
        self.logger.info("**** Verifying Email Field available test started ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(f"**** Acessing URL {self.baseURL} ****")
        self.sign_in = SignInPom
        self.sign_in = SignInPom(self.driver)
        self.logger.info("**** Checking for Email Field available ****")
        self.driver.save_screenshot(".\\Screenshot\\" +
                                    f'test_tr_srmg_id_03_01_email{" " + str(self.today)}.png')
        assert self.sign_in.hower_sign_in(), "**** Email Field Available Verified  ****"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=f'test_tr_srmg_id_03_01_email{" " + str(self.today)}.png',
                      attachment_type=AttachmentType.PNG)
        self.driver.close()
        self.logger.info("**** Email Element Verified \U0001F44D ****")
        self.logger.info("**** Email Element Available test Passed ****")