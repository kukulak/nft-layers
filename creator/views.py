from django.shortcuts import render
from .models import UpImage, Compound, Layer, Project, groupImage
# Create your views here.

def creator(request):
    layer = Layer.objects.all() 
    return render(
                  request,
                  'creator/layerView.html',
                  {
                   'layer' : layer
                                        })