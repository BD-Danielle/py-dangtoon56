
# -*- coding:utf-8 -*-

# self defined function as below
from requestsGet import getRequests
from headerSet import setHeader
from parse import parseUrl, parseName
from webdriverOpen import openBrowser, scrollPage, downloadHTML, closeBrowser
from imagesDownload import downloadImages

# public function or module as below
import re, time, bs4
import requests

if __name__ == '__main__':
    print('They may not be copied for commercial purposes or passed on or changed and used on other websites.')
    while True:
        print('URL for contents or episode:')
        # examples:
        # https://dangtoon56.com/결혼하는-남자(contents)
        # https://dangtoon56.com/결혼하는-남자-연재-8화-8-화.html(episode)
        # https://dangtoon56.com/파애(contents)
        # https://dangtoon56.com/파애-1화.html(episode)

        domain = 'https://dangtoon56.com'
        url = parseUrl(input(), encoding='utf-8', errors='replace')
        episode = True if re.findall('.html$', url) else False
        contents = not episode

        # prompt
        print('Do you want to download {} Y/n ?'.format('episode' if episode else 'contents'))
        feedback = input()
        if not feedback == 'Y':
            break

        try:
            res = None
            res = getRequests(url, headers=setHeader())
            res.raise_for_status()
            break
        except requests.exceptions.HTTPError as e:
            print(e)

    # open browser
    openBrowser(url)
    scrollPage()

    name = parseName(url, encoding='utf-8', errors='replace')

    # distinguish contents or episode
    downloadHTML(contents, name) if contents else downloadHTML(episode, name)
    downloadImages(name)
    closeBrowser()
