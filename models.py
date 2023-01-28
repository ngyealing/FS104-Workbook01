from django.db import models
CATEGORIES = (
    ('starters', 'Starters'),
    ('mains','Mains'),
    ('beverages','Beverages'),
    ('desserts','Desserts'),
)
class Menu(models.Model):
    product_name = models.CharField(max_length = 250)
    price = models.CharField(max_length = 50)
    product_image = models.ImageField()
    category = models.CharField(max_length=250, choices=CATEGORIES)
    def __str__(self):
        return self.product_name
