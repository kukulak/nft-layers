from PIL import Image, ImageColor, ImageEnhance, ImageFilter, ImageOps

# generate random integer values
from numpy.random import seed
from numpy.random import randint
# seed random number generator
seed(1)

import numpy as np
# import cv2
 



fondos = ['fondo-001.png', 'fondo-002.png', 'fondo-003.png']

mascaras = ['masCara-Azul1.png', 'masCara-RED.png', 'masCara.png']

# adornos = ['adorno0-00_mask.png', 'adorno0-001_mask.png', 'adorno0-003_mask.png', 'adorno0-004.png', 'adorno0-005.png', 'adorno0-006.png', 'adorno0-008.png', 'adorno0-009.png',  'adorno0-0010.png', 'adorno1-00.png', 'adorno1-001.png']

# adornos = ['adorno0-00_mask.png', 'adorno0-001_mask.png', 'adorno1-001_mask.png']


adornos = ['adorno0-00.png', 'adorno0-001.png', 'adorno0-003.png', 'adorno1-001.png']

colores = ['color', 'color1', 'color2']

ojos = ['ojos1.png', 'ojos2.png', 'ojos3.png', 'ojos2.png']

bocas = ['boca-001.png', 'boca-002.png', 'boca-001.png', 'boca-002.png']

FileSize = (2001, 2001)
position = (0, 0)
#layer un layer definir primero un layer con sus variables
theImage = Image.new('RGBA', (FileSize))


allElements = [fondos, mascaras, adornos, colores, ojos, bocas]

# theImage.paste('separados/fondos/' + fondos[1], (0, 0), 'separados/fondos/' + fondos[1])
ar = []
for b in allElements:
    ar.append(len(b))
# print(ar)
bigerArray = np.max(ar)
smallerArray = np.min(ar)

# print('Chico y grande', smallerArray, bigerArray)
mask = 0

# files most be a list

# def createLayer(first, second, file_size):
#     for f in first:
#         thisImage = Image.new('RGBA', (FileSize), (228, 150, 150))

#         imageOriginal = Image.open('separados/adorno/'+f)
#         imageF = Image.open('separados/adorno/'+f)
#         datas = imageF.getdata()
#         newData = []
#         for item in datas:
#             if item[0] == 13 and item[1] == 255 and item[2] == 0:
#                 newData.append((255, 255, 255, 0))
#             else:
#                 newData.append(item)
#         imageF.putdata(newData)  
#         imageOriginalSize = imageOriginal.resize(file_size) 
#         fSize = imageF.resize(file_size)
#         for s in second:
#             imageS = Image.open('separados/ojos/'+s)
#             sSize = imageS.resize(file_size)
#             # thisImage.paste(sSize, (0, 0), sSize) 
#             thisImage.paste(sSize, (0, 0), imageOriginalSize) 
#             thisImage.paste(fSize, (0, 0), fSize)
#             thisImage.show()

    
# createLayer(adornos, ojos, FileSize)      

fSize = None


def loadImage(image):
        imageSL = Image.open(image)
        fSize = imageSL.resize(FileSize)
        print(fSize)
        return fSize
       

# automatizar estos layers       
# background = loadImage('separados/fondos/' + fondos[1])
# mascara = loadImage('separados/mascaras/' + mascaras[1])





def createCompoundLayer(x, y): 
    compoundImage = Image.new('RGBA', (FileSize))
    layerX = loadImage(x)   
    layerY = loadImage(y)   
    compoundImage.paste(layerX, position, layerX)
    compoundImage.paste(layerY, position, layerY)
    # compoundImage.show()  
    return compoundImage


# createCompoundLayer()

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




def createBase(file, file_size):
    masks = []
    maskMe = None
    theFile = Image.open(file)
    if file.find('_mask') != -1:
        print('caracteristic')
        datas = theFile.getdata()
        newData = []
        masks.append(theFile)
        for item in datas:
            if item[0] == 13 and item[1] == 255 and item[2] == 0:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        theFile.putdata(newData)  
   
    theSize = theFile.resize(file_size)
    with theSize as fileColors:
        fileColors = fileColors.convert('RGB')
    r, g, b = fileColors.split()
    fileColors = Image.merge('RGB', (r, g, b))
    theImage.paste(fileColors, (0, 0), theSize)

i = 0

aLists = []


for a in allElements:
    length = bigerArray
    # newList = a[:]*bigerArray + a[:1]
    newList = a[:]*bigerArray
    # newList = newList[:length]
    newList = a[:length]
    
    # newList
    aLists.append(newList)



a = 0
b = 0
c = 0
d = 0

for aL in range(smallerArray):

  
    
    for aL in aLists[2]:
        if a >= len(aLists[0]):
            a = 0
           
            background = loadImage('separados/fondos/'+aLists[0][a])
            theImage.paste(background, (0, 0), background)

        else:    
         
            background = loadImage('separados/fondos/'+aLists[0][a])
            theImage.paste(background, (0, 0), background)

        if b >= len(aLists[1]):
            b = 0    
          
            mascara = loadImage('separados/mascaras/'+aLists[1][b])
            theImage.paste(mascara, (0, 0), mascara)
        else:
        
            mascara = loadImage('separados/mascaras/'+aLists[1][b])
            theImage.paste(mascara, (0, 0), mascara)



        b += 1
  

        createSimpleLayer('separados/adorno/'+aLists[2][c], 'separados/boca/'+aLists[5][c], 'separados/ojos/'+aLists[4][c])

        c += 1
        theImage.show()
        theImage.save('test/imgtest00'+str(d)+'.png', 'PNG')
        d += 1
    a += 1
    b = 0
    c = 0


