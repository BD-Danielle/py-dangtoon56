
# -*- coding:utf-8 -*-

# self defined function as below
from requestsGet import getRequests
from headerSet import setHeader
from parse import parseUrl, parseName
from webdriverOpen import openBrowser, scrollPage, downloadHTML, closeBrowser
# from webdriverOpen import downloadHTML, closeBrowser
from imagesDownload import downloadImages
from folder import createFolder

# from jpgConverter import converPDF

# public function or module as below
import re, time, bs4
import requests

if __name__ == '__main__':
    print('They may not be copied for commercial purposes or passed on or changed and used on other websites.')
    while True:
        print('URL for contents or episode:')
        # examples:
        # https://dangtoon56.com/결혼하는-남자(contents)
        # https://dangtoon56.com/결혼하는-남자-연재-9화-9-화.html(episode)
        # https://dangtoon56.com/%EA%B2%B0%ED%98%BC%ED%95%98%EB%8A%94-%EB%82%A8%EC%9E%90-10%ED%99%94.html
        # https://dangtoon56.com/파애(contents)
        # https://dangtoon56.com/파애-1화.html(episode)
        # https://dangtoon56.com/사슴과-마주친-눈
        # https://dangtoon56.com//사슴과-마주친-눈-35화.html
        # https://dangtoon56.com/반칙
        # https://dangtoon56.com/반칙-9화.html
        # https://dangtoon56.com/그래도-좋아해

        url = parseUrl(input(), encoding='utf-8', errors='replace')
        if not url:
            break
        episode = True if re.findall('.html$', url) else False
        contents = False

        # prompt
        print('Do you want to download {} y/n ?'.format('episode' if episode else 'contents'))
        feedback = input()
        if not feedback == 'y':
            closeBrowser()
            break
        else:
            try:
                res = None
                res = getRequests(url, headers=setHeader())
                res.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print(e)
                closeBrowser()
                # break
            
            manga_name = parseName(url, encoding='utf-8', errors='replace')
            # open browser
            openBrowser(manga_name, url)
            scrollPage()

            
            # distinguish contents or episode
            # fldrName = manga_name.split('-')[0] if contents else manga_name
            if episode:
                downloadHTML(episode, manga_name)
                downloadImages(manga_name)
            else:
                downloadHTML(contents, manga_name)
                

            # downloadHTML(episode, manga_name) if episode else downloadHTML(contents, manga_name)
            # downloadImages(manga_name)
            closeBrowser()
