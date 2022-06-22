from django.shortcuts import render
from menu.models import Dish, News, Images


def homepage(request):
    template = 'home.html'
    dishes = Dish.objects.order_by('?')[:3]
    news = News.objects.filter(is_published=True).order_by('-published_date')[:3]
    images = Images.objects.random3()
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
    context = {'dishes': dishes, 'news': news, 'image1': image1, 'image2': image2, 'image3': image3}
    return render(request, template, context)
