from django.db import models


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class NameBaseModel(BaseModel):
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True


class ProductGroup(NameBaseModel):
    comission_percentage = models.DecimalField(null=False, blank=False, max_digits=6, decimal_places=2)
    gain_percentage = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)

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
    legal_document_number = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'supplier'
        ordering = ['-active', '-id']
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['legal_document_number']),
        ]


class MaritalStatus(NameBaseModel):
    class Meta:
        managed = True
        db_table = 'marital_status'
        ordering = ['-active', '-id']
        verbose_name = 'Marital Status'
        verbose_name_plural = 'Marital Status'
        indexes = [
            models.Index(fields=['name']),
        ]


class Customer(NameBaseModel):
    income = models.DecimalField(null=False, blank=False, max_digits=16, decimal_places=2)
    gender = models.CharField(null=False, blank=False, max_length=1)
    district = models.ForeignKey(to='District', on_delete=models.RESTRICT)
    marital_status = models.ForeignKey(to='MaritalStatus', on_delete=models.RESTRICT)

    class Meta:
        managed = True
        db_table = 'customer'
        ordering = ['-active', '-id']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        indexes = [
            models.Index(fields=['name']),
        ]


class Department(NameBaseModel):
    class Meta:
        managed = True
        db_table = 'department'
        ordering = ['-active', '-id']
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        indexes = [
            models.Index(fields=['name']),
        ]


class Branch(NameBaseModel):
    class Meta:
        managed = True
        db_table = 'branch'
        ordering = ['-active', '-id']
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'
        indexes = [
            models.Index(fields=['name']),
        ]


class Sale(BaseModel):
    date = models.DateField()
    departament = models.ForeignKey(to='Department', on_delete=models.RESTRICT)
    branch = models.ForeignKey(to='Branch', on_delete=models.RESTRICT)
    customer = models.ForeignKey(to='Customer', on_delete=models.RESTRICT)

    class Meta:
        managed = True
        db_table = 'sale'
        ordering = ['-active', '-id']
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
        indexes = [
            models.Index(fields=['date']),
        ]


class Employee(NameBaseModel):
    salary = models.DecimalField(null=False, blank=False, max_digits=16, decimal_places=2)
    gender = models.CharField(null=False, blank=False, max_length=1)
    admission_date = models.DateField()
    birth_date = models.DateField()
    district = models.ForeignKey(to='District', on_delete=models.RESTRICT)
    department = models.ForeignKey(to='Department', on_delete=models.RESTRICT)
    marital_status = models.ForeignKey(to='MaritalStatus', on_delete=models.RESTRICT)

    class Meta:
        managed = True
        db_table = 'employee'
        ordering = ['-active', '-id']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        indexes = [
            models.Index(fields=['salary']),
            models.Index(fields=['gender']),
        ]


class Zone(NameBaseModel):
    class Meta:
        managed = True
        db_table = 'zone'
        ordering = ['-active', '-id']
        verbose_name = 'Zone'
        verbose_name_plural = 'Zones'
        indexes = [
            models.Index(fields=['name']),
        ]


class SaleItem(BaseModel):
    quantity = models.DecimalField(null=False, blank=False, max_digits=16, decimal_places=3)
    product = models.ForeignKey(to='ProductGroup', on_delete=models.RESTRICT)
    sale = models.ForeignKey(to='Sale', on_delete=models.RESTRICT)

    class Meta:
        managed = True
        db_table = 'sale_item'
        ordering = ['-active', '-id']
        verbose_name = 'Sale Item'
        verbose_name_plural = 'Sale Items'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['quantity']),
        ]


class Product(NameBaseModel):
    supplier = models.ForeignKey(to='Supplier', on_delete=models.RESTRICT)
    product_group = models.ForeignKey(to='ProductGroup', on_delete=models.RESTRICT)

    class Meta:
        managed = True
        db_table = 'product'
        ordering = ['-active', '-id']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['supplier']),
        ]


class State(NameBaseModel):
    abbreviation = models.CharField(max_length=2)

    class Meta:
        managed = True
        db_table = 'state'
        ordering = ['-active', '-id']
        verbose_name = 'State'
        verbose_name_plural = 'States'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['abbreviation']),
        ]


class City(NameBaseModel):
    state = models.ForeignKey(to='State', on_delete=models.RESTRICT)

    class Meta:
        managed = True
        db_table = 'city'
        ordering = ['-active', '-id']
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['state']),
        ]


class District(NameBaseModel):
    city = models.ForeignKey(to='City', on_delete=models.RESTRICT)
    zone = models.ForeignKey(to='Zone', on_delete=models.RESTRICT)

    class Meta:
        managed = True
        db_table = 'district'
        ordering = ['-active', '-id']
        verbose_name = 'District'
        verbose_name_plural = 'Districts'
        indexes = [
            models.Index(fields=['city']),
            models.Index(fields=['zone']),
        ]
