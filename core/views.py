from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import undetected_chromedriver as uc
import time
from .management.commands.runserver import Command


driver = Command().driver_start()
handles = [i for i in driver.window_handles]
print(driver)
def out_blaze():
    driver.switch_to.window(handles[1])
    
    WebDriverWait(driver,200).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'/html/body/div/main/div[1]/div[4]/div/div[1]/div/div[1]/div[1]/div/iframe')))
    elem = WebDriverWait(driver,200).until(EC.presence_of_element_located((By.XPATH,'/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[3]/div')))
    elem.click()
    while True:
        elemnt = driver.find_element(By.XPATH,'/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/app-stats-dropdown/div/div[2]')
        ext1= elemnt.text.split('\n')
        if len(ext1) < 4:
            pass
        else:
            return ['Blaze',ext1]


def out_bet():
    driver.switch_to.window(handles[2])

    WebDriverWait(driver,200).until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME,'iframe')))
    WebDriverWait(driver,200).until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME,'game-client-iframe')))
    WebDriverWait(driver,200).until(EC.frame_to_be_available_and_switch_to_it((By.ID,'game')))
    WebDriverWait(driver,200).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'/html/body/app-root/iframe')))
    elem = WebDriverWait(driver,200).until(EC.presence_of_element_located((By.XPATH,'/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[3]/div')))
    elem.click()
    while True:
        elemnt = driver.find_element(By.XPATH,'/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/app-stats-dropdown/div/div[2]')
        ext = elemnt.text.split('\n')
        if len(ext) < 4:
            pass
        else:
            return ['Betfair',ext]

def out_es():
    driver.switch_to.window(handles[0])

    WebDriverWait(driver,200).until(EC.frame_to_be_available_and_switch_to_it('gm-frm'))
    elem = WebDriverWait(driver,200).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[3]/div/div')))
    elem.click()
    while True:
        elemnt = driver.find_element(By.XPATH,'/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/app-stats-dropdown/div/div[2]')
        ext2= elemnt.text.split('\n')
        if len(ext2) < 4:
            pass
        else:
            return ['Estrela',ext2]


def index(request):
    return render(request,'index.html',{})

def index_estrela(request):
    return render(request,'index_estrela.html',{})

def index_betfair(request):
    return render(request,'index_betfair.html',{})

def aviatorsblaze(request):
    x = out_blaze()
    print(x)
    return render(request,'aviators_blaze.html',{'title_':x[0],'vals':[float(v.split('x')[0]) for v in x[1]]})

def aviatorsbetfair(request):
    x = out_bet()
    print(x)
    return render(request,'aviators_betfair.html',{'title_':x[0],'vals':[float(v.split('x')[0]) for v in x[1]]})

def aviatorsestrela(request):
    x = out_es()
    print(x)
    return render(request,'aviators_estrela.html',{'title_':x[0],'vals':[float(v.split('x')[0]) for v in x[1]]})
