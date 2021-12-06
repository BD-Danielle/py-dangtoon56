from PIL import Image
from PIL import ImageFile
import os
from os import listdir
from os.path import isfile, join
from folder import createFolder, goMainFolder


# jpg to png
def convertPNG(name):
    # os.chdir(fldrName)
    # createFolder(name)
    cwd = os.getcwd()
    # print(cwd)
    # print(listdir(cwd))
    # max_pixels = Image.MAX_IMAGE_PIXELS
    # imagesList = [f for f in listdir(cwd) if not f.startswith('.') and not f.endswith(".html") and isfile(join(cwd, f))]
    imagesList = [f for f in listdir(cwd) if f.endswith(".jpg") and isfile(join(cwd, f))]
    imageListAry = []
    if imagesList:
        # print(imagesList)
        imagesList.sort(key=lambda x: int(x[:-4]))
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

        createFolder('PNG')
        newImage.save('{}.png'.format(name))
        goMainFolder()
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

# chapters = [
#   '사슴과-마주친-눈-28화',
#   '사슴과-마주친-눈-27화',
#   '사슴과-마주친-눈-26화',
#   '사슴과-마주친-눈-25화',
#   '사슴과-마주친-눈-24화',
#   '사슴과-마주친-눈-23화',
#   '사슴과-마주친-눈-22화',
#   '사슴과-마주친-눈-21화',
#   '사슴과-마주친-눈-20화',
#   '사슴과-마주친-눈-19화',
#   '사슴과-마주친-눈-18화',
#   '사슴과-마주친-눈-17화',
#   '사슴과-마주친-눈-16화',
#   '사슴과-마주친-눈-15화',
#   '사슴과-마주친-눈-14화',
#   '사슴과-마주친-눈-13화',
#   '사슴과-마주친-눈-12화',
#   '사슴과-마주친-눈-11화',
#   '사슴과-마주친-눈-10화',
#   '사슴과-마주친-눈-9화',
#   '사슴과-마주친-눈-8화',
#   '사슴과-마주친-눈-7화',
#   '사슴과-마주친-눈-6화',
#   '사슴과-마주친-눈-5화',
#   '사슴과-마주친-눈-4화',
#   '사슴과-마주친-눈-3화',
#   '사슴과-마주친-눈-2화',
#   '사슴과-마주친-눈-1화'
# ]
# for chapter in chapters:
#     convertPNG(chapter, '사슴과-마주친-눈')
#     os.chdir('../../../')