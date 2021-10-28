import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from folder import createFolder, goMainFolder


def downloadImages(name):
    # os.chdir(name.split('-')[0])
    domain = 'https://dangtoon56.com'
    if (os.path.exists('{}.html'.format(name))):
        # createFolder(name)
        with open('{}.html'.format(name), 'r') as f:
            f_read = f.read()
            soup = BeautifulSoup(f_read, 'html.parser')
            imagesUrl = soup.select('div#toon_img > p > img[data-src]')
            # print(len(imagesUrl)) // 131
            digit_to_list = [int(0) for x in str(len(imagesUrl))]
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
                idx_to_list = [int(x) for x in str(idx)]
                pageNo_to_list = ([sum(i) for i in zip(digit_to_list[::-1], idx_to_list[::-1])] + digit_to_list[::-1][len(idx_to_list):])[::-1]
                pageNo_to_listStr = [str(x) for x in pageNo_to_list]

                img_data = requests.get(imageUrl['data-src']).content
                with open('{}.jpg'.format(''.join(pageNo_to_listStr)), 'wb') as f:
                    f.write(img_data)
        goMainFolder()


# downloadImages('결혼하는-남자-연재-8화-8-화')