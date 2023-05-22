from django.db import models

# Create your models here.
class Product(models.Model):
    uniq_id = models.CharField(max_length=225)
    product_name = models.CharField(max_length=225)
    category_id = models.IntegerField()
    product_url = models.CharField(max_length=225)
    pid = models.CharField(max_length=225)
    retail_price      =  models.DecimalField(max_digits=12,decimal_places=3)
    discounted_price  = models.DecimalField(max_digits=12,decimal_places=3)
    is_FK_Advantage_product = models.BooleanField(default=False)
    description = models.TextField()
    product_rating = models.IntegerField(default=0)
    overall_rating = models.IntegerField(default=0)
    brand = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Product_images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.PROTECT,blank=False)
    image_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Product_specifications(models.Model):
    product=models.ForeignKey(Product,on_delete=models.PROTECT,blank=False)
    key = models.TextField()
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
