from django.contrib import admin

# Register your models here.

from .models import UpImage, Compound, Layer, Project, groupImage

admin.site.register(UpImage)
admin.site.register(Compound)
admin.site.register(Layer)
admin.site.register(Project)
admin.site.register(groupImage)


