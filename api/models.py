from django.db import models

# Create your models here.
class Product(models.Model):
    store_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    sizes = models.TextField()
    colors = models.TextField()
    images = models.TextField()
    price = models.FloatField()
    instore_eligible = models.BooleanField(default = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    