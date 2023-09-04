from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinValueValidator
# Create your models here.

STATES=(('peshawar',"Peshawar"),
        ("islamabad","Islamabad"),
        ('karachi','Karachi'),
        ('lahore','Lahore'),
        ('mardan','Mardan'),
        ('swat','Swat'),
        ('nowshera','Nowshera'),
        )
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    locality= models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=40,choices=STATES)

    def __str__(self):
        return str(self.state)


CATEGORY=(
    ('L','Laptop'),
    ('M','Mobile'),
    ('TP','Top wear'),
    ('BW','Bottom wear'),

)
class Product(models.Model):
    title=models.CharField(max_length=30)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=CATEGORY)
    product_image=models.ImageField(upload_to="productimg")

    def __str__(self):
        return str(self.title)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{str(self.user)} , {str(self.product.title)}"
    
    @property
    def tcost(self):
        return self.product.discount_price* self.quantity


STATUS=(
    ('accepted','Accepted'),
    ('delivered','Delivered'),
    ('on the way','On the way'),
    ('packed','Packed'),
    ('cancel','Cancel'),
)
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=40,choices=STATUS,default="pending")

