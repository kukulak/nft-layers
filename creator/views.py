from django.shortcuts import render
from .models import UpImage, Compound, Layer, Project, groupImage
from .imgCreator import creatorNFT
from PIL import Image

def creator(request):
    #read the image
    im = Image.open("http://127.0.0.1:8000/media/imagesLayers/cuerpo-001.png")

    #show image
    im.show()
    layer = Layer.objects.all() 
    compound = Compound.objects.all()
    group = groupImage.objects.all()
    # creator = creatorNFT(layer, compound, group)
    return render(
                  request,
                  'creator/layerView.html',
                  {
                   'layer': layer,
                   'compound': compound,
                   'group': group,
                   'creator': creator
                                    })