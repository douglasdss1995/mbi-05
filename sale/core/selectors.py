from core import models


def get_all_products():
    return models.Product.objects.all()


def get_all_employees():
    return models.Employee.objects.all()


def get_all_customers():
    return models.Customer.objects.all()


def get_product_by_id(product_id: int):
    return models.Product.objects.get(id=product_id)


def get_employee_by_id(employee_id: int):
    return models.Employee.objects.get(id=employee_id)


def get_customer_by_id(customer_id: int):
    return models.Customer.objects.get(id=customer_id)


def get_product(name: str):
    return models.Product.objects.get(name=name)


def get_employee(name: str):
    return models.Employee.objects.get(name=name)


def get_customer_by_name(name: str):
    return models.Customer.objects.get(name=name)


def create_zone():
    models.Zone.objects.create(name='Zona 01')


def create_product():
    product_group = models.ProductGroup.objects.get(id=1)
    suppiler = models.Supplier.objects.get(id=1)
    models.Product.objects.create(
        name='produto 01',
        const_price=1,
        sale_price=1,
        id_suppiler=suppiler,
        id_product_group=product_group,
        active=True

    )
