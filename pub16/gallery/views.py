from django.shortcuts import render
from menu.models import Images


def gallery(request):
    template = 'gallery.html'
    images = Images.objects.random6()
    try:
        image1 = images[0]
    except:
        image1 = None
    try:
        image2 = images[1]
    except:
        image2 = None
    try:
        image3 = images[2]
    except:
        image3 = None
    try:
        image4 = images[3]
    except:
        image4 = None
    try:
        image5 = images[4]
    except:
        image5 = None
    try:
        image6 = images[5]
    except:
        image6 = None
    context = {'image1': image1, 'image2': image2, 'image3': image3,
               'image4': image4, 'image5': image5, 'image6': image6}
    return render(request, template, context)
