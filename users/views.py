import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from .models import CustomUser
from config.settings import EMAIL_HOST_USER



class RegisterView(CreateView):
    """ Регистрация нового пользователя. """
    model = CustomUser
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.token = secrets.token_hex(16)
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/valid_token/{user.token}'

        send_mail(
            subject='Спасибо за что зарегистрировались!',
            message=f'Перейдите по ссылке {url} для подтверждения email',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def valid_user_from_email(requeast, token):
    """ Верификация пользователя. """
    user = get_object_or_404(CustomUser, token=token)
    if user:
        user.is_active = True
        user.save()
        return redirect('users:login')
    return PermissionDenied


class UpdateUserView(LoginRequiredMixin, UpdateView):
    """ Редактирование данных зарегистрированного пользователя. """
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'update_user.html'
    success_url = reverse_lazy('catalog:home')

    def get_object(self):
        return self.request.user
