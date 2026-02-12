from core import models


def get_all_products():
    return models.Product.objects.all()


def get_all_employees():
    return models.Employee.objects.all()


def get_all_customers():
    return models.Customer.objects.all()


def get_product_by_id(product_id: int):
    return models.Product.objects.get(id=product_id)


def get_product_group_by_id(product_group_id: int):
    return models.ProductGroup.objects.get(id=product_group_id)


def get_supplier_by_id(supplier_id: int):
    return models.Supplier.objects.get(id=supplier_id)


def get_product_by_name(product_name: str):
    return models.Product.objects.get(name=product_name)


def create_zone():
    models.Zone.objects.create(name='Zone 01')


def create_product():
    product_group = models.ProductGroup.objects.get(id=1)
    supplier = models.Supplier.objects.get(id=1)

    return models.Product.objects.create(
        name='Product 01',
        cost_price='100',
        sale_price='200',
        id_supplier=supplier.id,
        id_product_group=product_group.id,
        active=True,

    )
