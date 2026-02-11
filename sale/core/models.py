from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class NameBaseModel(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class ProductGroup(NameBaseModel):
    commission_porcentage = models.DecimalField(decimal_places=2, max_digits=6)
    gain_porcentage = models.DecimalField(decimal_places=2, max_digits=6)


class Supplier(NameBaseModel):
    legal_document = models.CharField(max_length=40)


class Product(NameBaseModel):
    supplier = models.ForeignKey(to='Supplier', on_delete=models.RESTRICT)
    product_group = models.ForeignKey(to='ProductGroup', on_delete=models.RESTRICT)


class Sale(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    # department = models.ForeignKey(to='Department', on_delete=models.RESTRICT)
    # branch = models.ForeignKey(to='Branch', on_delete=models.RESTRICT)
    # customer = models.ForeignKey(to='Customer', on_delete=models.RESTRICT)


class SaleItem(BaseModel):
    quantity = models.DecimalField(max_digits=16, decimal_places=3)
    product = models.ForeignKey(to='Product', on_delete=models.RESTRICT)
    sale = models.ForeignKey(to='Sale', on_delete=models.RESTRICT)


class Customer(NameBaseModel):
    income = models.DecimalField(decimal_places=2, max_digits=16)
    gender = models.CharField(max_length=1)
    district = models.ForeignKey(to='District', on_delete=models.RESTRICT)
    marital_status = models.ForeignKey(to='MaritalStatus', on_delete=models.RESTRICT)


class MaritalStatus(NameBaseModel):
    class Meta:
        managed = True


class Employee(NameBaseModel):
    salary = models.DecimalField(decimal_places=2, max_digits=16)
    gender = models.CharField(max_length=1)
    admission_date = models.DateField()
    birth_date = models.DateField()
    district = models.ForeignKey(to='District', on_delete=models.RESTRICT)
    department = models.ForeignKey
