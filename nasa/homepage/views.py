from django.shortcuts import render
from .models import Images
from django.conf import settings


def index_view(request):
    template = 'index.html'
    images = Images.objects.all()
    context = {'images': images,
               'MEDIA_URL': settings.MEDIA_URL}
    return render(request, template, context)
