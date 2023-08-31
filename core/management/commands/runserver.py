from django.contrib.staticfiles.management.commands.runserver import Command as RunServer
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import undetected_chromedriver as uc
import time
import asyncio


class Command(RunServer):
    driver = None

    @classmethod
    def driver_change(cls,recv):
        cls.driver = recv

    def driver_start(cls):
        return cls.driver

    def inner_run(self, *args, **options):
        self.pre_start(self=self)
        super().inner_run(*args, **options)
        self.pre_quit()

    def pre_start(cls, self):
        # ___ESTRELA BET___#

        cls.driver = uc.Chrome(driver_executable_path='./chromedriver',headless=True)

        cls.driver.get('https://estrelabet.com/ptb/bet/main')
        #time.sleep(10)
        elem = WebDriverWait(cls.driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="username"]')))
        elem = cls.driver.find_element(By.XPATH,'//*[@id="username"]')
        elem.send_keys('vcalango1')
        elem = cls.driver.find_element(By.XPATH,'//*[@id="password-login"]')
        #elem = WebDriverWait(cls.driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="login-password"]')))
        elem.send_keys('Cassino@2487')
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        cls.driver.get('https://estrelabet.com/ptb/games/detail/casino/normal/7787')
        try:
            element = WebDriverWait(cls.driver,20).until(EC.presence_of_element_located((By.CLASS_NAME,'modal-overlay')))
            cls.driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, element)
        except selenium.common.exceptions.TimeoutException:
            pass
        #WebDriverWait(cls.driver,200).until(EC.frame_to_be_available_and_switch_to_it('gm-frm'))
        #elem = WebDriverWait(cls.driver,200).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[3]/div/div')))
        #elem.click()

        ######## FIM DO ESTRELABET #########

        #_____BLAZE______#

        cls.driver.switch_to.new_window('tab')

        cls.driver.get('https://blaze.com/en/?modal=auth&tab=login')
        elem = cls.driver.find_element(By.XPATH,'/html/body/div[1]/main/div[3]/div/div[2]/div/form/div[1]/div/input')
        elem.send_keys('vanderlinocalango@gmail.com')
        elem = cls.driver.find_element(By.XPATH,'/html/body/div[1]/main/div[3]/div/div[2]/div/form/div[2]/div/input')
        elem.send_keys('Cassino2487')
        elem = cls.driver.find_element(By.XPATH,'/html/body/div[1]/main/div[3]/div/div[2]/div/form/div[4]/button')
        elem.click()
        time.sleep(5)
        cls.driver.get('https://blaze.com/en/games/aviator')
        #elem = cls.driver.find_element(By.ID,'close-chat')
        #elem.click()
        #WebDriverWait(cls.driver,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'/html/body/div/main/div[1]/div[4]/div/div[1]/div/div[1]/div[1]/div/iframe')))
        #elem = WebDriverWait(cls.driver,40).until(EC.presence_of_element_located((By.XPATH,'/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[3]/div')))
        #elem.click()

        ######## FIM DA BLAZE #########

        #______BETFAIR______#

        cls.driver.switch_to.new_window('tab')

        cls.driver.get('https://www.betfair.com/exchange/plus/')
        WebDriverWait(cls.driver,200).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="onetrust-accept-btn-handler"]'))).click()
        elem = cls.driver.find_element(By.XPATH,'//*[@id="ssc-liu"]')
        elem.send_keys('vanderlinocalango@gmail.com')
        elem = cls.driver.find_element(By.XPATH,'//*[@id="ssc-lipw"]')
        elem.send_keys('Cassino@2487')
        elem = cls.driver.find_element(By.XPATH,'//*[@id="ssc-lis"]')
        elem.click()
        time.sleep(5)
        cls.driver.get('https://casino.betfair.com/pt-br/c/crash-games')
        cls.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div/div[2]/div/div[1]/div/a').click()

        #WebDriverWait(cls.driver,20).until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME,'iframe')))
        #WebDriverWait(cls.driver,20).until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME,'game-client-iframe')))
        #WebDriverWait(cls.driver,20).until(EC.frame_to_be_available_and_switch_to_it((By.ID,'game')))
        #WebDriverWait(cls.driver,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'/html/body/app-root/iframe')))
        #elem = WebDriverWait(cls.driver,40).until(EC.presence_of_element_located((By.XPATH,'/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[3]/div')))
        #elem.click()

        ####### FIM DA BETFAIR #######
        self.driver_change(cls.driver)
        print(cls.driver)

    def pre_quit(cls):
        cls.driver.quit()
