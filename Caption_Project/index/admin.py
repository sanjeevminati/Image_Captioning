from django.contrib import admin
from .models import *
from django.utils.html import format_html

class GalleryAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.imageURL.url))

    image_tag.short_description = 'Image Preview'

    readonly_fields = ['image_tag']


class ImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.image.url))

    image_tag.short_description = 'Image Preview'

    readonly_fields = ['image_tag']

admin.site.register(Image,ImageAdmin)
admin.site.register(Caption,GalleryAdmin)
