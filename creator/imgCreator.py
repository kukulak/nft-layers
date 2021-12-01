from PIL import Image, ImageColor, ImageEnhance, ImageFilter, ImageOps

from django.conf import settings

# generate random integer values
from numpy.random import seed
from numpy.random import randint
# seed random number generator
seed(1)

import numpy as np
# import cv2
 

# get th names of the layers
# get the compounds of the layers
# get the groups of the compound
# get the list of the images




class FullImage(object):
    pass

fi = FullImage()
# >>> class Foo(object):
# ...     pass
# ... 
# >>> foo = Foo()
# >>> foo.a = 3
# >>> Foo.b = property(lambda self: self.a + 1)
# >>> foo.b
# 4

FileSize = (2001, 2001)
position = (0, 0)
theImage = Image.new('RGBA', (FileSize))

path = 'http://127.0.0.1:8000'

def loadImage(image):
        imageSL = Image.open(image)
        fSize = imageSL.resize(FileSize)
        print(fSize)
        return fSize
  
def createCompoundLayer(x, y): 
    compoundImage = Image.new('RGBA', (FileSize))
    layerX = loadImage(x)   
    layerY = loadImage(y)   
    compoundImage.paste(layerX, position, layerX)
    compoundImage.paste(layerY, position, layerY)
    # compoundImage.show()  
    return compoundImage



def createSimpleLayer(maskanfile, x, y):
    layerImage = Image.new('RGBA', (FileSize))
    layerMasked = Image.new('RGBA', (FileSize))

    q = createCompoundLayer(x, y)   
    z = loadImage(maskanfile)
    z1 = loadImage(maskanfile)   
    z2 = loadImage(maskanfile)

    datas = z.getdata()
    newData = []
    for item in datas:
        if item[0] == 13 and item[1] == 255 and item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item) 
    z.putdata(newData)  
 
    blur = z.filter(ImageFilter.GaussianBlur(20 / 2))

    layerImage.paste(q, (0, 0), z1)
    # layerImage.paste(blur, (10, 10), blur)
    layerImage.paste(z, (0, 0), z)

 
    theImage.paste(layerImage, (0, 0), layerImage)
    theImage.show()



def creatorNFT(layers, compound, group):
    fullLayers = []
    compounds = []
    groups = [] 
    img = []
    # pass
    for comp in compound:
        # --------------
        # --------------
        print('compounds', comp.compound_name)
        for c in comp.group_images.all():
            print('combinations', c.groupImage_name)
            for nurl in c.layer_images.all():
                # createSimpleLayer(path + nurl.upload_img.url, path + nurl.upload_img.url, path + nurl.upload_img.url)
                print ('URL', nurl.upload_img.url)



    for lay in layers:        
        # setattr(fi, str(lay), str(lay.compound.all()))
        # layers.append('{')
        # stringed = str(lay)
        # layers.append(stringed)
        
        fullLayers.append(lay.layer_name )



        # lay = layers
        # print('layers:', layers, '|||||||')
        for la in lay.compound.all():
            fullLayers.append(la.compound_name )
            # setattr(fi, str(la), str(la.group_images.all()))
            # print(' compound:', la, '|||')
            for l in la.group_images.all():
                fullLayers.append(l.groupImage_name )
                # print('     group:', l, '|||')
                for i in l.layer_images.all():
                    fullLayers.append(i.upload_img.url)

                    # print('         img:', i.upload_img.url)
                    # print('         img:', i.rarity)
                # leparate = layers.index(l)
                # print('0003:', '\n', layers[leparate:])

            # laparate = layers.index(la)
            # img.append(layers[laparate:])
            # img.append('|')
            
            # print('0004:', '\n', layers[laparate:], '\n')

        separate = fullLayers.index(lay.layer_name)
        img.append(fullLayers[separate:])

        # layers.append('}')
        # print('layers:', '\n', layers)

    
    # print('separate', separate)
    # print('0001:', '\n', layers[:separate])
    # print('0002:', '\n', layers[separate:])

    # print(layers)
    # a = img[0][0]
    print('\n', img, '\n', len(img))
    # print('\n', img.index('cuerpo'), '\n')
    # print('\n', a, type(a), '\n')
    fullList = []
    for im in img:
        temp1=[]
        temp2=[]
        temp3=[]
        temp4=[]
        for i, jey in enumerate(im[:-1]):
            # if jey == im[i+1]:
            # temp1=[]   

            if jey.find('/') and im[i+1].find('/') and im[i+2].find('/'):
                temp1.append(im[i])
                fullList.append(temp1) 
            # else:
            #     temp1=[]   
            if jey.find('/') and im[i+1].find('/') and im[i-1].find('/'):
                temp2.append(im[i])
                temp1.append(temp2) 

            # else:
            #     temp1.append(temp2) 
            #     temp2=[]     
            if jey.find('/') and im[i+1].find('/')==-1 and im[i-1].find('/'):
                temp3.append(im[i+1])  
                temp2.append(temp3) 
            # if jey.find('/') and im[i+1].find('/') and im[i-1].find('/'):
            #     temp3.append(im[i+1])  
            #     temp2.append(temp3) 
            # if jey.find('/') and im[i+1].find('/')==-1 and im[i-1].find('/')==-1:
            #     temp4.append(im[i+1])  
            #     temp3.append(temp4) 
            # else:
            #     temp2.append(temp3) 
            #     temp3=[]        
            # if jey.find('/')!= -1 :
            #     temp4.append(im[i])
            #     temp3.append(temp4)     
            # for e in i:
                # print(e)
            # if i.find('/') != -1:
            #     temp2.append(i)
                # print(temp2)
                # if type(im) is list:
                #     print(im, 'this is list')

        # print('\n', temp1, '\n')
        # print('\n', temp2, '\n')
        # print('\n', temp3, '\n')

    print('\n', '\n', fullList, '\n', '\n')



    


    # print('THEOBJECT', fullImage)
    # print('layers:', '\n', layers)
  





