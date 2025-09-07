from .models import Product


# def get_products_by_category(category_id):
#     """ Возвращает список продуктов, относящихся к указанной категории."""
#
#     try:
#         category = Category.objects.get(pk=category_id)
#     except Category.DoesNotExist:
#         return Product.objects.none()
#
#     if hasattr(category, "products"):
#         products = category.products.all()
#     else:
#         products = Product.objects.filter(category=category)
#
#     return products

def get_products_by_category(category_id):
    """Возвращает список продуктов, относящихся к указанной категории."""
    return Product.objects.filter(category_id=category_id)