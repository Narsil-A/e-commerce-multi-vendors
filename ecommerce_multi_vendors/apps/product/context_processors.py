from apps.product.models import Category  #global functionality


def menu_categories(request):
    categories = Category.objects.all()

    return {'menu_categories':categories}

