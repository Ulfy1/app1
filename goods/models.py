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
    price = models.DecimalField(default = 0.00, max_digits=7, decimal_places=2, verbose_name='price')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Discount in %")
    quantity = models.PositiveIntegerField(default=0, verbose_name='quantity')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    def first_image(self):
        images = self.images.all()
        return images[0] if images else None

    def __str__(self):
        return self.name
    
    def sell_price(self):
        return round(self.price - (self.price * self.discount) / 100, 2)

    class Meta():
        db_table = 'product'


class ProductImage(models.Model):
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/', verbose_name="Additional images")


    def __str__(self):
        return f"{self.product.name} with id: {self.product.id}"