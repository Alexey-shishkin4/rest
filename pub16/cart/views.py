from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from menu.models import Dish
from cart.models import Orders
from cart.cart import Cart
from cart.forms import CartAddProduct, CartUpdateProduct, DeliveyForm
from django.shortcuts import get_object_or_404, render
import pub16.settings

from datetime import datetime
from cloudipsp import Api, Checkout


@require_POST
def cart_add(request, prod_id):
    cart = Cart(request)
    product = get_object_or_404(Dish, id=prod_id)
    form = CartAddProduct(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.remove(product)
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, prod_id):
    cart = Cart(request)
    product = get_object_or_404(Dish, id=prod_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    total_price = 0
    for item in cart:
        item['update_quantity_form'] = CartUpdateProduct(initial={'quantity': int(item['quantity']),
                                                                   'update': True})
        total_price += (item['total_price'])
    cart = sorted(cart, key=lambda x: x['product'].name)
    total_price = Decimal(total_price)
    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})


def pay_fondy(request):
    cart = Cart(request)
    total_price = 0
    for item in cart:
        total_price += (item['total_price'])
    total_price = Decimal(total_price)

    api = Api(merchant_id=pub16.settings.MERCHANT_ID,
          secret_key=pub16.settings.FONDY_SECRET_KEY)
    checkout = Checkout(api=api)
    data = {
        "currency": "RUB",
        "amount": str(int(total_price)) + "00"
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)


def delivery_form(request):
    template = 'delivery.html'
    form = DeliveyForm(request.POST or None)
    if form.is_valid():
        cd = form.cleaned_data
        name = cd['name']
        table = cd['table']
        phone = cd['phone']
        created = Orders.objects.update_or_create(name=name, table=table, phone=phone)
        return redirect(reverse('cart:pay_fondy'))
    context = {'form': form}
    return render(request, template, context)

def succes(request):
    template = 'succes.html'
    context = {}
    return render(request, template, context)