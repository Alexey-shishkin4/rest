from django.urls import path
import cart.views as view

app_name = 'cart'

urlpatterns = [
    path('', view.cart_detail, name='cart_detail'),
    path('add/<int:prod_id>/', view.cart_add, name='cart_add'),
    path('remove/<int:prod_id>/', view.cart_remove, name='cart_remove'),
    path('pay/', view.pay_fondy, name='pay_fondy'),
    path('form/', view.delivery_form, name='delivery_page'),
    path('succes/', view.succes, name='succes')
]
