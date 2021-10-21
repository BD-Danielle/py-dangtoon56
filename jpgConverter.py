from PIL import Image
import os
from os import listdir
from os.path import isfile, join
from folderCreate import createFolder


# jpg to pdf
def converPDF(name):
    os.chdir(name.split('-')[0])
    createFolder(name)
    cwd = os.getcwd()
    # print(cwd)
    # print(listdir(cwd))
    imagesList = [f for f in listdir(cwd) if not f.startswith('.') and isfile(join(cwd, f))]
    imagesList.sort()
    # print(imagesList)
    imageListAry = []
    imagesOpened = [Image.open(x) for x in imagesList][0:9]
    widths, heights = zip(*(i.size for i in imagesOpened))
    max_width = max(widths)
    total_height = sum(heights)
    newImage = Image.new('RGB', (max_width, total_height))
    y_offset = 0
    print(imagesOpened)
    for idx, image in enumerate(imagesOpened):
        # print(image)
        print(y_offset)
        newImage.paste(image, (0, y_offset))
        y_offset += image.size[1]
    
    createFolder('JPG')
    newImage.save('{}.jpg'.format(name))
    #     if image != '.DS_Store':
    #         try:
    #             globals()['imageOpened%s' % idx] = Image.open(image)
    #             globals()['imageConverted%s' % idx] = globals()['imageOpened%s' % idx].convert('RGB')
    #             imageListAry.append(globals()['imageOpened%s' % idx])
    #             print('Valid image')
    #         except Exception:
    #             print('Invalid image')

    # imageOpened0.save('{}.pdf'.format(name), save_all=True, append_images=imageListAry[1:])


converPDF('결혼하는-남자-연재-8화-8-화')