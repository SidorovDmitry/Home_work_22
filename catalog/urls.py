from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_card, product_catalog, pay


app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path("product_card/<int:product_id>/", product_card, name="product_card"),
    path('product_catalog/', product_catalog, name='product_catalog'),
    path('pay/', pay, name='pay'),
]