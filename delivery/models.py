from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.username} {self.phone} {self.address} {self.email} {self.password}"
    
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    picture = models.URLField(max_length=500, default="https://imgs.search.brave.com/zxR8HPyZAag5y4XNDNTd0KA9OX4tft3V4VOkuckbUIs/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4t/aWNvbnMtcG5nLmZs/YXRpY29uLmNvbS8x/MjgvMTM3Ni8xMzc2/MzM3LnBuZw")
    cuisine = models.CharField(max_length=200)
    rating = models.FloatField()

    def __str__(self):
        return f"{self.name} {self.cuisine} {self.rating}/5"
    
class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name = "menu_items")
    name = models.CharField(max_length=50)
    picture = models.URLField(max_length=500, default="https://imgs.search.brave.com/zxR8HPyZAag5y4XNDNTd0KA9OX4tft3V4VOkuckbUIs/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4t/aWNvbnMtcG5nLmZs/YXRpY29uLmNvbS8x/MjgvMTM3Ni8xMzc2/MzM3LnBuZw")
    description = models.CharField(max_length=200)
    price = models.FloatField()
    is_veg = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.description} {self.price}"
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name = "cart")
    items = models.ManyToManyField("MenuItem", related_name="carts")
    
    def total_price(self):
        return sum(item.price for item in self.items.all())

    def __str__(self):
        return f"{self.customer.username} {self.total_price}"