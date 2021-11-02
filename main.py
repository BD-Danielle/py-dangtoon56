
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
    print('URL for contents or episode:')
    url = parseUrl(input(), encoding='utf-8', errors='replace')

    while url:
        if not url:
            print('sorry to see you go!')
            break
        judge = True if re.findall('.html$', url) else False
        episode = True
        contents = False

        # prompt
        print('Do you want to download {} y/n ?'.format('episode' if judge else 'contents'))
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
            if judge:
                downloadHTML(episode, manga_name)
                downloadImages(manga_name)
                closeBrowser()
                break

            else:
                downloadHTML(contents, manga_name)
                closeBrowser()
                break
