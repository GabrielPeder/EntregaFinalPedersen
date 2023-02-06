
from django.urls import path
from Products import views
from Products.views import add_product, list_products, list_scooter, list_street, list_offroad, searchform, inicio, ProductCreateView


urlpatterns = [
    path('', inicio),
    path('add_product/', ProductCreateView.as_view()),
    path('list_products/', list_products),
    path('search/', searchform),
    path('Styles/Scooter/', list_scooter),
    path('Styles/Street/', list_street),
    path('Styles/Offroad/', list_offroad)
]