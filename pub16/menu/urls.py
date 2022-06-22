from django.urls import path
import menu.views as vw

urlpatterns = [
    path('', vw.all_menu, name='menu-page'),
    path('cat/<int:pk>', vw.get_category, name='category-page'),
    path('dish/<int:pk>', vw.get_dish, name='dish-page'),
]