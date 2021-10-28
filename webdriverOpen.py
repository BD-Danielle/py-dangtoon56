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
from folder import createFolder
from withOpen import with_open_write, with_open_read

driver = webdriver.Chrome(ChromeDriverManager().install())


# open chrome browser
def openBrowser(manga_name, url):
    if createFolder(manga_name):
        driver.get(url)
        driver.implicitly_wait(10)
        time.sleep(random.randrange(10))
        driver.implicitly_wait(30)
    else:
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
    domain = 'https://dangtoon56.com'

    # always check file is existed or not
    while (element.is_displayed()):
        if not (os.path.exists('{}.html'.format(name))):
            with_open_write(name, 'html', driver.page_source)
        else:
            print('Do you wanna download {}.html again y/n ?'.format(name))
            feedback = input()
            if not feedback == 'y':
                break
            else:
                with_open_write(name, 'html', driver.page_source)
    
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
        input 1-5 will download 1 to 5.....................
        input 1, 2, 5 will download 1, 2 and 5 so on.......
        input 1, 2, 5, 7-10 will download 1, 2, 5, 7 to 10.
        ''')
        print('-' * 70)

        # input as following
        choose = input()
        if choose:
            choose_to_list = re.findall(r'[0-9]+\-?[0-9]*', choose)
            print(choose_to_list)
            choices_to_list = []
            for choice in choose_to_list:
                try:
                    begin, end = choice.split('-')
                    choice_to_list = list(range(int(begin), int(end) + 1))
                    choices_to_list.extend(choice_to_list)
                    print(choices_to_list)
                except ValueError as ve:
                    choices_to_list.extend(choice)
                    print(ve)
                    continue
            print(choices_to_list)
        
            for choice in choices_to_list:
                idx = len(reg_episodes) - int(choice)
                if idx < 0:
                    break
                url = domain + episodes[idx]
                openBrowser(reg_episodes[idx], url)
                downloadHTML(True, reg_episodes[idx])
                downloadImages(reg_episodes[idx])
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