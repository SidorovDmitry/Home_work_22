from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from catalog.models import Product
from catalog.forms import ProductForm
from django.views import View
from django.shortcuts import get_object_or_404, redirect


class ProductPublishView(PermissionRequiredMixin, View):
    permission_required = 'catalog.can_publish_product'

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.is_published = True
        product.save()
        return redirect('catalog:product_detail', pk=pk)


class ProductUnpublishView(PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.is_published = False
        product.save()
        return redirect('catalog:product_detail', pk=pk)

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

    def get_queryset(self):
        if self.request.user.has_perm('catalog.can_publish_product'):
            return Product.objects.all()
        return Product.objects.filter(is_published=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_card.html'
    context_object_name = 'product'

    def get_queryset(self):
        if self.request.user.has_perm('catalog.can_publish_product'):
            return Product.objects.all()
        return Product.objects.filter(is_published=True)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:product_catalog')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user

    def get_success_url(self):
        """ Перенаправление на страницу созданного блога. """
        return reverse("catalog:product_card", kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_catalog')
    raise_exception = True

    def test_func(self):
        product = self.get_object()
        # Может удалять владелец или модератор
        return (product.owner == self.request.user or
                self.request.user.has_perm('catalog.delete_product'))