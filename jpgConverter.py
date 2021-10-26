from PIL import Image
from PIL import ImageFile
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
    # max_pixels = Image.MAX_IMAGE_PIXELS
    imagesList = [f for f in listdir(cwd) if not f.startswith('.') and isfile(join(cwd, f))]
    imagesList.sort(key=lambda x: int(x[:-4]))
    
    print(imagesList)
    imageListAry = []
    imagesOpened = [Image.open(x) for x in imagesList]
    widths, heights = zip(*(i.size for i in imagesOpened))

    max_width = max(widths)
    total_height = sum(heights)
    width_resize = 600
    width_ratio = float(width_resize / max_width)
    total_height_resize = int(total_height * float(width_ratio))
    # wpercent = (basewidth/float(img.size[0]))
    # hsize = int((float(img.size[1])*float(wpercent)))
    # total_height_resize = int(width_resize * (sum(heights) / max_width))
    # print(total_height_resize)
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    
    newImage = Image.new('RGB', (width_resize, total_height_resize))
    y_offset = 0
    for idx, image in enumerate(imagesOpened):
        height_resize = int(image.size[1] * width_ratio)
        image_resize = image.resize((width_resize, height_resize), Image.ANTIALIAS)
        newImage.paste(image_resize, (0, y_offset))
        # y_offset += image.size[1]
        y_offset += height_resize

    createFolder('JPG')
    newImage.save('{}.jpg'.format(name))
    # createFolder('JPG')
    # newImage.save('{}.jpg'.format(name))
    #     if image != '.DS_Store':
    #         try:
    #             globals()['imageOpened%s' % idx] = Image.open(image)
    #             globals()['imageConverted%s' % idx] = globals()['imageOpened%s' % idx].convert('RGB')
    #             imageListAry.append(globals()['imageOpened%s' % idx])
    #             print('Valid image')
    #         except Exception:
    #             print('Invalid image')

    # imageOpened0.save('{}.pdf'.format(name), save_all=True, append_images=imageListAry[1:])

# titles = [
#     '파애-1화',
#     '파애-2화',
#     '파애-3화',
#     '파애-4화',
#     '파애-5화',
#     '파애-6화',
#     '파애-7화',
#     '파애-8화',
#     '파애-9화',
#     '파애-10화',
#     '파애-11화',
#     '파애-12화',
#     '파애-13화',
#     '파애-14화',
#     '파애-15화',
#     '파애-16화',
#     '파애-17화',
#     '파애-18화',
#     '파애-19화',
#     '파애-20화',
#     '파애-21화-1부-최종화',
#     '파애-22화-2부-1화',
#     '파애-23화',
#     '파애-24화',
#     '파애-25화',
#     '파애-26화',
#     '파애-27화',
#     '파애-28화',
#     '파애-29화',
#     '파애-30화',
#     '파애-31화',
#     '파애-32화',
#     '파애-33화',
#     '파애-34화',
#     '파애-35화',
#     '파애-36화',
#     '파애-37화',
#     '파애-38화',
#     '파애-39화',
#     '파애-40화',
#     '파애-41화',
#     '파애-42화',
#     '파애-43화',
#     '파애-44화',
#     '파애-45화',
#     '파애-46화',
#     '파애-47화',
#     '파애-48화-최종화'
# ]
# for title in titles:
#     converPDF(title)
#     os.chdir('../../../')