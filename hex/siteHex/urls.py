from django.urls import path

from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name="about"),
    path('product',views.product, name='produto'),
    path('products',views.products, name='produtos'),
    path('contato/',views.contact, name='contato'),
]
