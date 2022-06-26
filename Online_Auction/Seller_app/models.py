from django.db import models
from User_app.models import MyUser

# Create your models here.
class ProductCategory(models.Model):
    product_category_id = models.AutoField(primary_key=True)
    product_category_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.product_category_name)

class ProductSubCategory(models.Model):
    product_sub_category_id = models.AutoField(primary_key=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_sub_category_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.product_sub_category_name)

class ProductInformation(models.Model):
    product_info_id = models.AutoField(primary_key=True)
    product_sub_category = models.ForeignKey(ProductSubCategory, on_delete=models.CASCADE)
    myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_info_details = models.TextField()
    product_verify = models.BooleanField(default=False)
    product_baseprice = models.BigIntegerField()
    is_sold = models.BooleanField(default=False)
    product_location = models.CharField(max_length=50)

    def __str__(self):
        return str(self.product_name)

class ProductImages(models.Model):
    product_image_id = models.AutoField(primary_key=True)
    product_information = models.ForeignKey(ProductInformation, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to = 'ProductPhotos/')

    def __str__(self):
        return str(self.product_image_id)