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

    class Supplier(NameBaseModel):
        legal_document = models.CharField(max_length=40)

        def __str__(self):
            return self.name
