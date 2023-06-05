import os
from PIL import Image

imagePath = 'C:/learning code/vscode/Web dev stuff/crashblog/media/uploads'
files_Wanted = ('.jpeg','png', '.jpg')

def resizeImages(imagePath, files_Wanted):
    for items in os.listdir(imagePath):
        if items.endswith(files_Wanted):
            if os.path.isfile(imagePath + items):
                im = Image.open(imagePath + items)
                desireSize =(600, 800)
                im.convert('RGB')
                im = im.resize(desireSize, resample = 0)
                im.save(imagePath + items, 'png', quality =100)
resizeImages(imagePath, files_Wanted)
