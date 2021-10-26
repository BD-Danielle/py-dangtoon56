import time
import random
import os
import re

from withOpen import with_open_write, with_open_read
from folderCreate import createFolder
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

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
    selector = 'div#toon_img' if bool else 'form#fboardlist'
    element = driver.find_element_by_css_selector(selector)

    # always check file is existed or not
    while (element.is_displayed()):
        fldrName = name.split('-')[0] if bool else name
        createFolder(fldrName)
        if not (os.path.exists('{}.html'.format(name))):
            with_open_write(name, 'html', driver.page_source)
        else:
            print('Do you wanna download {}.html again Y/n ?'.format(name))
            feedback = input()
            if not feedback == 'Y':
                break
            else:
                with_open_write(name, 'html', driver.page_source)
    
    # extract episodes from contents
    while not bool:
        episodes = listEpisodes(name)
        # prompt as following
        print('-' * 50)
        print('Do you want to download episodes as following ? \n')
        print(f"{'No.' : <5}{'Episode' : <10}")
        for idx, episode in enumerate(episodes):
            reg_episode = re.findall(r"[^/]*[a-zA-Z0-9]*[^.html$]", episode)[1]
            print(f"{len(episodes) - idx : <5}{reg_episode : <10}")
        print('-' * 50)

        # input as following
        feedback = input()


def listEpisodes(contents):
    createFolder(contents)
    if (os.path.exists('{}.html'.format(contents))):
        f_read = with_open_read('html', contents)
        soup = BeautifulSoup(f_read, 'html.parser')
        links = soup.select('form#fboardlist table > tbody > tr > td > a[href]')
        links_to_list = [link['href'] for link in links]
        return links_to_list


# close chrome browser
def closeBrowser():
    driver.quit()