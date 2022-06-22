from menu.models import Dish, Category
from django.shortcuts import get_object_or_404, render
from cart.forms import CartAddProduct


def all_menu(request):
    template = 'menu.html'
    categories = Category.objects.all()
    sl = {}
    for i in categories:
        sl[i] = Dish.objects.filter(category=i)
    res = [{'category': i, 'items': sl[i]} for i in sl]
    cart_form = CartAddProduct(request.POST or None)
    context = {'items': res, 'cart_form': cart_form}
    return render(request, template, context)


def get_category(request, pk):
    template = 'menu/category.html'
    category = get_object_or_404(Category, pk=pk)
    dishes = Dish.objects.filter(category=category)
    context = {'category': category, 'dishes': dishes}
    return render(request, template, context)


def get_dish(request, pk):
    template = 'menu/dish.html'
    dish = get_object_or_404(Dish, pk=pk)
    context = {'dish': dish}
    return render(request, template, context)
