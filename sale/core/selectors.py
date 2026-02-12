from core import models


def get_all_products():
    return models.Product.objects.all()
