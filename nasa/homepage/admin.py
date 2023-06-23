from django.contrib import admin
from .models import Images
from django.utils.html import format_html


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_image')

    def display_image(self, obj):
        image_html = format_html(f'<img src="{obj.image.url}" width="50" height="50" alt="{obj.name}">')
        return image_html

    display_image.short_description = 'Image'
    display_image.allow_tags = True 