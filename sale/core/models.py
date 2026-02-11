from django.db import models


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    id = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NameBaseModel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class State(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    abbreviation = models.CharField(max_length=2)

    class Meta:
        managed = True
        db_table = 'State'
        ordering = ('-name', 'abbreviation')
        verbose_name = 'State'
        verbose_name_plural = 'States'
        indexes = [
            models.Index(fields=['name']),
        ]


class City(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='cities')

    class Meta:
        managed = True
        db_table = 'City'
        ordering = ('name', '-state')
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        indexes = [
            models.Index(fields=['name']),
        ]


class Zone(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'Zone'
        ordering = ('name',)
        verbose_name = 'Zone'
        verbose_name_plural = 'Zones'
        indexes = [
            models.Index(fields=['name']),
        ]


class District(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='districts')
    zone = models.ForeignKey(Zone, on_delete=models.PROTECT, related_name='districts')

    class Meta:
        managed = True
        db_table = 'District'
        ordering = ('name', '-city', 'zone')
        verbose_name = 'District'
        verbose_name_plural = 'Districts'
        indexes = [
            models.Index(fields=['name']),
        ]


class Department(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'Department'
        ordering = ('name',)
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        indexes = [
            models.Index(fields=['name']),
        ]


class Branch(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    district = models.ForeignKey(District, on_delete=models.PROTECT, related_name='branches')

    class Meta:
        managed = True
        db_table = 'Branch'
        ordering = ('name', 'district')
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'
        indexes = [
            models.Index(fields=['name']),
        ]


class MaritalStatus(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'MaritalStatus'
        ordering = ('name',)
        verbose_name = 'MaritalStatus'
        verbose_name_plural = 'MaritalStatus'
        indexes = [
            models.Index(fields=['name']),
        ]


class Custumer(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    income = models.DecimalField(max_digits=16, decimal_places=2)
    gender = models.CharField(max_length=1)
    district = models.ForeignKey(District, on_delete=models.PROTECT, related_name='custumers')
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.PROTECT, related_name='custumers')

    class Meta:
        managed = True
        db_table = 'Custumer'
        ordering = ('name', 'income', 'gender', 'district', 'marital_status')
        verbose_name = 'Custumer'
        verbose_name_plural = 'Custumers'
        indexes = [
            models.Index(fields=['name']),
        ]


class Employee(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    salary = models.DecimalField(max_digits=16, decimal_places=2)
    gender = models.CharField(max_length=1)
    admission_date = models.DateField()
    birth_date = models.DateField()
    district = models.ForeignKey(District, on_delete=models.PROTECT, related_name='employees')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='employees')
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.PROTECT, related_name='employees')

    class Meta:
        managed = True
        db_table = 'Employee'
        ordering = ('name', 'salary', 'gender', 'admission_date', 'birth_date', 'district', 'department',
                    'marital_status')
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        indexes = [
            models.Index(fields=['name']),
        ]


class Supplier(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'Supplier'
        ordering = ('name',)
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        indexes = [
            models.Index(fields=['name']),
        ]


class ProductGroup(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    commission_percentage = models.DecimalField(max_digits=6, decimal_places=2)
    gain_percentage = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'product_group'
        ordering = ('-active', '-id')
        verbose_name = 'Product Group'
        verbose_name_plural = 'Product Groups'
        indexes = [
            models.Index(fields=['name']),
        ]


class Product(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='products')
    product_group = models.ForeignKey(ProductGroup, on_delete=models.PROTECT, related_name='products')

    class Meta:
        managed = True
        db_table = 'product'
        ordering = ('name', 'supplier', 'product_group')
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        indexes = [
            models.Index(fields=['name']),
        ]


class Sale(BaseModel):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='sales')
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, related_name='sales')
    customer = models.ForeignKey(Custumer, on_delete=models.PROTECT, related_name='sales')

    class Meta:
        managed = True
        db_table = 'sale'
        ordering = ('-date', 'department', 'branch', 'customer')
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
        indexes = [
            models.Index(fields=['date']),
        ]


class SaleItem(BaseModel):
    id = models.AutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=16, decimal_places=3)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='items')
    sale = models.ForeignKey(Sale, on_delete=models.PROTECT, related_name='items')

    class Meta:
        managed = True
        db_table = 'sale_item'
        ordering = ('quantity', 'product', 'sale')
        verbose_name = 'Sale Item'
        verbose_name_plural = 'Sales Items'
        indexes = [
            models.Index(fields=['name']),
        ]
