from playwright.sync_api import sync_playwright
import time
from amb import url_access 

###Login Sagres####
with sync_playwright() as p:
    browser = p.chromium.launch()#headless=False
    context = browser.new_context()
    page = context.new_page()
    page.goto(url_access)
    #pagina.locator('xpath=//*[@id="ctl00_PageContent_LoginPanel_UserName"]').click()
    page.fill('xpath=//*[@id="ctl00_PageContent_LoginPanel_UserName"]', "jsambarreto")
    page.fill('xpath=//*[@id="ctl00_PageContent_LoginPanel_Password"]', '123456')
    page.locator('xpath=//*[@id="ctl00_PageContent_LoginPanel_LoginButton"]').click()
    time.sleep(10)
    page.locator('xpath=//*[@id="wrap"]/div[1]/div[1]/div[2]/div[3]/a').click()
    time.sleep(2)
    page.locator('xpath=//*[@id="wrap"]/div[1]/div[1]/div[2]/div[3]/a').click()
    time.sleep(2)
    

    
    
    #page.goto("https://www.google.com")
    #page.screenshot()