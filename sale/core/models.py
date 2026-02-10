from django.db import models

class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    commission_percentage = models.DecimalField(decimal_places=2, max_digits=6)
    gain_percentage = models.DecimalField(decimal_places=2, max_digits=6)

    class Meta:
        managed = True

class Supplier(NameBaseModel):
    legal_document = models.CharField(max_length=40)

    class Meta:
        managed = True

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