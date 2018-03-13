from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" %  self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    # floors = models.DecimalField(max_digits=1, decimal_places=1, default=1)
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    area = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    floors = models.DecimalField(max_digits=4, decimal_places=0, default=0)
    rooms = models.DecimalField(max_digits=2, decimal_places=0, default=1)
    height = models.DecimalField(max_digits=4, decimal_places=2, default=2.8)
    foundation = models.CharField(max_length=5, blank=True, null=True, default='СВФ')
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    roof_price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    water_price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    front_price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'