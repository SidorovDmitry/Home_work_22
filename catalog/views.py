from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product

def home(request):
    return render(request, template_name="home.html")


# ФУНКЦИЯ ОТОБРАЖЕНИЯ И ОТПРАВКИ ФОРМЫ ЗАПРОСА
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contacts.html')


def product_card(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {"product": product}
    return render(request, "product_card.html", context=context)


def product_catalog(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'product_catalog.html', context=context)

def pay(request):
    return render(request, "pay.html")
