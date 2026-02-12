from datetime import date

from django.db import models


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True, null=False, verbose_name='Identifier', db_column='id')
    created_at = models.DateTimeField(null=True, auto_created=True, verbose_name='Created at', db_column='created_at')
    modified_at = models.DateTimeField(null=True, auto_now_add=True, verbose_name='Modified at',
                                       db_column='modified_at')
    active = models.BooleanField(db_column='active', default=True)

    class Meta:
        abstract = True
        ordering = ['-active', '-id']

    def __str__(self) -> str:
        return str(self.id)


class NameBaseModel(BaseModel):
    name = models.CharField(unique=False, max_length=128, db_column='name')

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'ID: {self.id} - Name: {self.name}'


class Branch(NameBaseModel):
    id_district = models.ForeignKey(
        to='District', on_delete=models.RESTRICT, db_column='id_district'
    )

    class Meta:
        managed = True
        db_table = 'branch'
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'
        db_table_comment = 'Place where the sales are made'


class City(NameBaseModel):
    id_state = models.ForeignKey(to='State', on_delete=models.RESTRICT, db_column='id_state')

    class Meta:
        managed = True
        db_table = 'city'
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        db_table_comment = 'Place where the sales are made'


class Customer(NameBaseModel):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'

    gender = models.CharField(max_length=1, choices=Gender.choices, db_column='gender')
    income = models.DecimalField(max_digits=16, decimal_places=2, db_column='income')
    id_district = models.ForeignKey(
        to='District', on_delete=models.RESTRICT, db_column='id_district'
    )
    id_marital_status = models.ForeignKey(
        to='MaritalStatus', on_delete=models.RESTRICT, db_column='id_marital_status'
    )

    class Meta:
        managed = True
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        db_table_comment = 'Person who buys the products'


class Department(NameBaseModel):
    class Meta:
        managed = True
        db_table = 'department'
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        db_table_comment = 'Department where the employees work'


class District(NameBaseModel):
    id_city = models.ForeignKey(to='City', on_delete=models.RESTRICT, db_column='id_city')
    id_zone = models.ForeignKey(to='Zone', on_delete=models.RESTRICT, db_column='id_zone')

    class Meta:
        managed = True
        db_table = 'district'
        verbose_name = 'District'
        verbose_name_plural = 'Districts'
        db_table_comment = 'Place where the sales are made'


class Employee(NameBaseModel):
    salary = models.DecimalField(max_digits=16, decimal_places=2, db_column='salary')
    gender = models.CharField(max_length=1, db_column='gender')
    admission_date = models.DateField(db_column='admission_date')
    birth_date = models.DateField(db_column='birth_date')
    id_department = models.ForeignKey(
        to='Department', on_delete=models.RESTRICT, db_column='id_department'
    )
    id_district = models.ForeignKey(District, models.RESTRICT, db_column='id_district')
    id_marital_status = models.ForeignKey(
        to='MaritalStatus', on_delete=models.RESTRICT, db_column='id_marital_status'
    )

    class Meta:
        managed = True
        db_table = 'employee'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        db_table_comment = 'Person who works in the company'

    @property
    def age(self) -> int:
        """Calculate age of employee."""
        today = date.today()

        # Calcula diferença bruta de anos
        age_years = today.year - self.birth_date.year

        # Verifica se o aniversário deste ano já passou
        birthday_this_year = date(today.year, self.birth_date.month, self.birth_date.day)

        # Se o aniversário ainda não chegou, subtrai 1
        if today < birthday_this_year:
            age_years -= 1

        return age_years


class MaritalStatus(NameBaseModel):
    class Meta:
        managed = True
        db_table = 'marital_status'
        verbose_name = 'Marital Status'
        verbose_name_plural = 'Marital Statuses'
        db_table_comment = 'Marital status of the customers and employees'


class Product(NameBaseModel):
    cost_price = models.DecimalField(max_digits=16, decimal_places=2, db_column='cost_price')
    sale_price = models.DecimalField(max_digits=16, decimal_places=2, db_column='sale_price')
    id_product_group = models.ForeignKey(
        to='ProductGroup', on_delete=models.RESTRICT, db_column='id_product_group'
    )
    id_supplier = models.ForeignKey(
        to='Supplier', on_delete=models.RESTRICT, db_column='id_supplier'
    )

    class Meta:
        managed = True
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table_comment = 'Product that is sold'


class ProductGroup(NameBaseModel):
    commission_percentage = models.DecimalField(max_digits=6, decimal_places=2, db_column='commission_percentage')
    gain_percentage = models.DecimalField(max_digits=6, decimal_places=2, db_column='gain_percentage')

    class Meta:
        managed = True
        db_table = 'product_group'
        verbose_name = 'Product Group'
        verbose_name_plural = 'Product Groups'
        db_table_comment = 'Group of products'


class Sale(BaseModel):
    date = models.DateTimeField(db_column='date')
    id_branch = models.ForeignKey(to='Branch', on_delete=models.RESTRICT, db_column='id_branch')
    id_customer = models.ForeignKey(
        to='Customer', on_delete=models.RESTRICT, db_column='id_customer'
    )
    id_employee = models.ForeignKey(
        to='Employee', on_delete=models.RESTRICT, db_column='id_employee',
    )

    class Meta:
        managed = True
        db_table = 'sale'
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
        db_table_comment = 'Sale made by an employee to a customer'


class SaleItem(BaseModel):
    quantity = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        db_column='quantity',
    )
    id_product = models.ForeignKey(
        to='Product',
        on_delete=models.RESTRICT,
        db_column='id_product',
    )
    id_sale = models.ForeignKey(
        to='Sale',
        on_delete=models.RESTRICT,
        db_column='id_sale',
    )
    sale_price = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        blank=True,
        null=True,
        db_column='sale_price',
    )

    class Meta:
        managed = True
        db_table = 'sale_item'
        verbose_name = 'Sale Item'
        verbose_name_plural = 'Sale Items'
        db_table_comment = 'Item of a sale'


class State(NameBaseModel):
    abbreviation = models.CharField(
        max_length=2,
        db_column='abbreviation',
    )

    class Meta:
        managed = True
        db_table = 'state'
        verbose_name = 'State'
        verbose_name_plural = 'States'
        db_table_comment = 'State where the customers live'


class Supplier(NameBaseModel):
    legal_document = models.CharField(
        unique=True,
        max_length=20,
        db_column='legal_document',
    )

    class Meta:
        managed = True
        db_table = 'supplier'
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        db_table_comment = 'Person who supplies the products'


class Zone(NameBaseModel):
    class Meta:
        managed = True
        db_table = 'zone'
        verbose_name = 'Zone'
        verbose_name_plural = 'Zones'
        db_table_comment = 'Zone where the customers live'
