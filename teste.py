from playwright.sync_api import sync_playwright
import time
from utils.amb import url_access 

i = 0
###Login Sagres####
def executa_teste( usuario: str, senha: str):
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=False)#headless=False
            context = browser.new_context()
            context.set_default_timeout(5000)
            page = context.new_page()
            page.goto(url_access)
            #pagina.locator('xpath=//*[@id="ctl00_PageContent_LoginPanel_UserName"]').click()
            page.fill('xpath=//*[@id="ctl00_PageContent_LoginPanel_UserName"]', usuario)
            page.fill('xpath=//*[@id="ctl00_PageContent_LoginPanel_Password"]', str(senha))
            page.locator('xpath=//*[@id="ctl00_PageContent_LoginPanel_LoginButton"]').click()
            time.sleep(5)
            page.locator('xpath=//*[@id="wrap"]/div[1]/div[1]/div[2]/div[3]/a').click()
            time.sleep(2)
            page.locator('xpath=//*[@id="wrap"]/div[1]/div[1]/div[2]/div[3]/a').click()
            time.sleep(2)
        except Exception as e:
            print("Erro: ", e)
            return e
    return (i++1)
