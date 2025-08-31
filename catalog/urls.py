from django.urls import path
from catalog.apps import CatalogConfig
from .views import HomeView, ContactsView, ProductPayView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductPublishView, ProductUnpublishView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_card/<int:pk>/', ProductDetailView.as_view(), name="product_card"),
    path('product_catalog/', ProductListView.as_view(), name='product_catalog'),
    path('pay/', ProductPayView.as_view(), name='pay'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/publish/<int:pk>/', ProductPublishView.as_view(), name='product_publish'),
    path('product/unpublish/<int:pk>/', ProductUnpublishView.as_view(), name='product_unpublish'),
]