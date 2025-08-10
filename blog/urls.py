from django.urls import path
from blog.apps import BlogConfig
from .views import BlogListView, BlogCreateView, BlogDeleteView, BlogDetailView, BlogUpdateView

app_name = BlogConfig.name


urlpatterns = [
    path('blog_list/', BlogListView.as_view(), name='blog_lict'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path("blog_detail/<int:pk>/", BlogDetailView.as_view(), name='blog_detail'),
    path("blog_update/<int:pk>/", BlogUpdateView.as_view(), name='blog_update'),
    path("blog_delete/<int:pk>/", BlogDeleteView.as_view(), name='blog_delete'),
]