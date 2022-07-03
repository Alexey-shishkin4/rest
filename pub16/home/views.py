from django.shortcuts import render
from menu.models import Dish, News, Images


def homepage(request):
    template = 'home.html'
    dishes = Dish.objects.order_by('?')[:1].get()
    news = News.objects.filter(is_published=True).order_by('-published_date')[:2]
    context = {'dishes': dishes, 'news': news}
    return render(request, template, context)
