import time
import random
import os

from folderCreate import createFolder
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


# open chrome browser
def openBrowser(url):
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(random.randrange(10))
    driver.implicitly_wait(30)


# scroll down page
def scrollPage():
    try:
        html = driver.find_element_by_tag_name('html')
        # scroll down 6 times
        for x in range(6):
            html.send_keys(Keys.END)
            time.sleep(random.randrange(24))
        print("Finally finished!")
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")


# download contents or episodes
def downloadHTML(bool, name):
    # contents = driver.find_element_by_css_selector('form#fboardlist > div > table > tbody > tr > td > a[href]')
    # episode = driver.find_element_by_css_selector('div#toon_img > p > img[data-src]')
    print(bool)
    selector = 'form#fboardlist' if not bool else 'div#toon_img'
    element = driver.find_element_by_css_selector(selector)

    if (element.is_displayed()):
        # contents is False
        if not bool:
            createFolder(name)
            if not (os.path.exists('{}.html'.format(name))):
                with open('{}.html'.format(name), 'w') as f:
                    f.write(driver.page_source)
        # episode is True
        else:
            title = name.split('-')[0]
            print(title)
            createFolder(title)
            if not (os.path.exists('{}.html'.format(name))):
                with open('{}.html'.format(name), 'w') as f:
                    f.write(driver.page_source)
    else:
        print('element display none')


# close chrome browser
def closeBrowser():
    driver.quit()
