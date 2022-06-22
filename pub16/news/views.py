from django.shortcuts import render
from menu.models import News


def news(request):
    template = 'news.html'
    news = News.objects.filter(is_published=True).order_by('-published_date')[:3]
    try:
        news1 = news[0]
    except Exception:
        news1 = None
    try:
        news2 = news[1]
    except Exception:
        news2 = None
    try:
        news3 = news[2]
    except Exception:
        news3 = None
    context = {'news1': news1, 'news2': news2, 'news3': news3}
    return render(request, template, context)
