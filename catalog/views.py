# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from .models import Product
#
# def home(request):
#     return render(request, template_name="home.html")
#
#
# # ФУНКЦИЯ ОТОБРАЖЕНИЯ И ОТПРАВКИ ФОРМЫ ЗАПРОСА
# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
#     return render(request, 'contacts.html')
#
#
# def product_card(request,product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     context = {"product": product}
#     return render(request, "product_card.html", context=context)
#
#
# def product_catalog(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, 'product_catalog.html', context=context)
#
# def pay(request):
#     return render(request, "pay.html")

from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView

from catalog.models import Product


class HomeView(TemplateView):
    template_name = 'home.html'
    success_url = reverse_lazy('home')


class ContactsView(TemplateView):
    template_name = 'contacts.html'
    success_url = reverse_lazy('contacts')


class ProductPayView(TemplateView):
    template_name = 'pay.html'
    success_url = reverse_lazy('pay')


class ProductListView(ListView):
    model = Product
    template_name = 'product_catalog.html'
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_card.html'
    context_object_name = 'product'
