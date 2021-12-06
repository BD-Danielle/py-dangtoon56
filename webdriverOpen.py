import time
import random
import os
import re

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from imagesDownload import downloadImages
from folder import createFolder, goMainFolder
from withOpen import with_open_write, with_open_read
from jpgConverter import convertPNG
from inputClosed import closeInput

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# driver = webdriver.Chrome(ChromeDriverManager().install())


# get the driver
def getDriver(url):
    # print('24: ', url)
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(random.randrange(10))
    driver.implicitly_wait(30)


# open chrome browser
def openBrowser(manga_name, url):
    sec = 10
    reminder = 'Do you wanna download {}.html AGAIN y/n ?'.format(manga_name)
    lda_getDriver = lambda: getDriver(url)
    lda_wow = lambda: with_open_write(manga_name, 'html', 'w', driver.page_source)
    if createFolder(manga_name):
        if not (os.path.exists('{}.html'.format(manga_name))):
            getDriver(url)
            with_open_write(manga_name, 'html', 'w', driver.page_source)
    else:
        if not (os.path.exists('{}.html'.format(manga_name))):
            getDriver(url)
            with_open_write(manga_name, 'html', 'w', driver.page_source)
        else:
            closeInput(reminder, sec, lda_getDriver, lda_wow)
            driver.get('file://' + os.getcwd() + '/' + manga_name + '.html')


# scroll down page
def scrollPage():
    scroll_pause_time = 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print('Page loaded')
            break
        last_height = new_height


# download contents or episodes
def downloadHTML(bool, name):
    selector = 'div#toon_img' if bool else 'form#fboardlist'
    element = driver.find_element_by_css_selector(selector)
    domain = 'https://dangtoon15.com'

    isDisplay = element.is_displayed()
    if not isDisplay:
        print('element is not display')
        return
    # always check file is existed or not
    sec = 10
    callback = lambda: with_open_write(name, 'html', 'w', driver.page_source)
    entry = True
    while entry:
        if not (os.path.exists('{}.html'.format(name))):
            callback()
            entry = False
            break
        else:
            reminder = 'Do you wanna download {}.html y/n ?'.format(name)
            closeInput(reminder, sec, callback)
            entry = False
            break
    
      
    # extract episodes from contents
    if not bool:
        episodes = listEpisodes(name)
        reg_episodes = []
        # prompt as following
        print('-' * 70)
        print('Do you want to download episodes as following ? \n')
        print(f"{'No.' : <5}{'Episode' : <10}")
        for idx, episode in enumerate(episodes):
            reg_episode = re.findall(r"[^/]+[a-zA-Z0-9]*[^.html$]", episode)[0]
            reg_episodes.append(reg_episode)
            print(f"{len(episodes) - idx : <5}{reg_episode : <10}")
        print('''Please input episode number as preceding, e.g.,
        1) use dash to download serial number
        input 1-5 to download the range of numbers.......................
        2) use dot or space to download non consecutive numbers.
        input 1, 2, 5 will download 1, 2 and 5 so on.....................
        input 1 2, 5 will download 1 2 and 5 so on.......................
        ''')
        print('-' * 70)

        # input as following
        choose = input()
        if choose:
            choose_to_list = re.findall(r'[0-9]+\-?[0-9]*', str(choose))
            choices_to_list = []
            for choice in choose_to_list:
                try:
                    begin, end = choice.split('-')
                    choice_to_list = list(range(int(begin), int(end) + 1))
                    choices_to_list.extend(choice_to_list)
                except ValueError as ve:
                    print('126: ', choice)
                    choices_to_list.insert(len(choices_to_list), choice)
                    print(ve)
                    continue
            print('131: ', choices_to_list)
        
            for choice in choices_to_list:
                idx = len(reg_episodes) - int(choice)
                if idx < 0:
                    break
                url = domain + episodes[idx]
                openBrowser(reg_episodes[idx], url)
                downloadHTML(True, reg_episodes[idx])
                downloadImages(reg_episodes[idx])
                convertPNG(reg_episodes[idx])
                goMainFolder()
        else:
            print('you didnt choose any episodes, sorry to see you go')


def listEpisodes(manga_name):
    if (os.path.exists('{}.html'.format(manga_name))):
        f_read = with_open_read(manga_name, 'html')
        soup = BeautifulSoup(f_read, 'html.parser')
        links = soup.select('form#fboardlist table > tbody > tr > td > a[href]')
        links_to_list = [link['href'] for link in links]
        return links_to_list


# close chrome browser
def closeBrowser():
    driver.quit()

# listEpisodes('파애')