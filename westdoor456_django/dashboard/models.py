#from django.db import models
from djongo import models
#from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    product_no = models.IntegerField(primary_key=True)
    product_class = models.CharField(max_length=100, null=True, blank=True)
    product_name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.product_no)

class Camera(models.Model):
    camera_no = models.IntegerField(primary_key=True)
    camera_name = models.CharField(max_length=100, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.camera_no)


class ratings(models.Model):
    
    rating0 = models.IntegerField(default=0)
    rating1 = models.IntegerField(default=0)
    rating2 = models.IntegerField(default=0)
    rating3 = models.IntegerField(default=0)
    rating4 = models.IntegerField(default=0)
    rating5 = models.IntegerField(default=0)
    rating6 = models.IntegerField(default=0)
    rating7 = models.IntegerField(default=0)
    rating8 = models.IntegerField(default=0)
    rating9 = models.IntegerField(default=0)
    
    class Meta:
        abstract = True

# for i in range(10):
#     first_key = 'rating' + str(i)
#     first_value = models.IntegerField(default=0)
#     setattr(ratings, first_key, first_value)


# class ratingForm(forms.ModelForm):
#     class Meta:
#         model = rating
#         fields = ('rating_no', 'rating_value')
    

class Customer(models.Model):
    customer_no = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_gender = models.CharField(max_length=10, choices=(('Male','Male'),('Female','Female')), null=True, blank=True)
    customer_age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], null=True, blank=True)
    customer_market_in = models.BooleanField(default=False)
    customer_ratings = models.EmbeddedModelField(
        model_container=ratings
        #model_form_class=ratingForm
    )
    def __str__(self):
        return str(self.customer_no)

class CameraLog(models.Model):
    camera = models.ForeignKey(Camera, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    datetime_now = models.DateTimeField(auto_now = True)
