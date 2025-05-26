from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Category')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    def __str__(self):
        return self.name

    class Meta():
        db_table = 'category'


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='image')
    price = models.DecimalField(default = 0.00, max_digits=7, decimal_places=2, verbose_name='price')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Discount in %")
    quantity = models.PositiveIntegerField(default=0, verbose_name='quantity')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'product'