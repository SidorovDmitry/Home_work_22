from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .apps import UsersConfig
from .views import RegisterView, UpdateUserView, valid_user_from_email

app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:home'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('update/', UpdateUserView.as_view(), name='update'),
    path('valid_token/<str:token>/',valid_user_from_email, name="valid_token"),
]