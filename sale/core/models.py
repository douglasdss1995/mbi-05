from django.db import models


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class NameBaseModel(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class ProductGroup(NameBaseModel):
    commission_percentage = models.DecimalField(decimal_places=2, max_digits=6)
    gain_percentage = models.DecimalField(decimal_places=2, max_digits=6)

    class Meta:
        managed = True
        db_table = 'product_group'
        ordering = ['-active', '-id']
        verbose_name = 'Product Group'
        verbose_name_plural = 'Product Groups'
        indexes = [
            models.Index(fields=['name']),
        ]


class Supplier(NameBaseModel):
    legal_document = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'supplier'


class Product(NameBaseModel):
    supplier = models.ForeignKey(
        to='Supplier',
        on_delete=models.RESTRICT
    )
    product_group = models.ForeignKey(
        to='ProductGroup',
        on_delete=models.RESTRICT
    )

    class Meta:
        managed = True


class Zone(NameBaseModel):
    class Meta:
        managed = True


class State(NameBaseModel):
    abbreviation = models.CharField(max_length=2)

    class Meta:
        managed = True


class City(NameBaseModel):
    state = models.ForeignKey(to='State', on_delete=models.RESTRICT)

    class Meta:
        managed = True


class District(NameBaseModel):
    city = models.ForeignKey(to='City', on_delete=models.RESTRICT)
    zone = models.ForeignKey(to='Zone', on_delete=models.RESTRICT)

    class Meta:
        managed = True


class Branch(NameBaseModel):
    district = models.ForeignKey(to='District', on_delete=models.RESTRICT)

    class Meta:
        managed = True


class Department(NameBaseModel):
    class Meta:
        managed = True


class MaritalStatus(NameBaseModel):
    class Meta:
        managed = True


class Employee(NameBaseModel):
    salary = models.DecimalField(decimal_places=2, max_digits=16)
    gender = models.CharField(max_length=1)
    admission_date = models.DateField()
    birth_date = models.DateField()
    district = models.ForeignKey(to='District', on_delete=models.RESTRICT)
    department = models.ForeignKey(to='Department', on_delete=models.RESTRICT)
    marital_status = models.ForeignKey(to='MaritalStatus', on_delete=models.RESTRICT)


class Customer(NameBaseModel):
    income = models.DecimalField(decimal_places=2, max_digits=16)
    district = models.ForeignKey(to='District', on_delete=models.RESTRICT)
    marital_status = models.ForeignKey(to='MaritalStatus', on_delete=models.RESTRICT)


class Sale(BaseModel):
    date = models.DateField()
    branch = models.ForeignKey(to='Branch', on_delete=models.RESTRICT)
    employee = models.ForeignKey(to='Employee', on_delete=models.RESTRICT)
    customer = models.ForeignKey(to='Customer', on_delete=models.RESTRICT)


class SaleItem(BaseModel):
    sale = models.ForeignKey(to='Sale', on_delete=models.RESTRICT)
    quantity = models.DecimalField(decimal_places=2, max_digits=6)
    product = models.ForeignKey(to='Product', on_delete=models.RESTRICT)
