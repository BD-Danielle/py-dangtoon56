import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from requestsGet import getRequests
from headerSet import setHeader
from folderCreate import createFolder


def downloadImages(name):
    # os.chdir(name.split('-')[0])
    domain = 'https://dangtoon56.com'
    if (os.path.exists('{}.html'.format(name))):
        with open('{}.html'.format(name), 'r') as f:
            createFolder(name)
            toon_img = f.read()
            soup = BeautifulSoup(toon_img, 'html.parser')
            imagesUrl = soup.select('div#toon_img > p > img[data-src]')
            # digit = [int(0) for x in str(len(imagesUrl))]

            for idx, imageUrl in enumerate(imagesUrl):
                print(imageUrl['data-src'])
                if not (urlparse(imageUrl['data-src']).netloc):
                    imageUrl['data-src'] = domain + imageUrl['data-src']
                # try:
                #     res = None
                #     res = getRequests(imageUrl['data-src'], headers=setHeader())
                #     res.raise_for_status()
                #     break
                # except requests.exceptions.HTTPError as e:
                #     print(e)
                
                img_data = requests.get(imageUrl['data-src']).content
                with open('{}.jpg'.format(idx), 'wb') as f:
                    f.write(img_data)


# downloadImages('파애-18화')