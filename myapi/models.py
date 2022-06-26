from django.db import models

# Create your models here.

class ShopUnit (models.Model):
    name = models.CharField(max_length=255)
    # ShopUnit Type Choices
    CHOICES = (
        ('OFFER', 'OFFER'),
        ('CATEGORY', 'CATEGORY'))
        
    type = models.CharField(max_length=10, choices = CHOICES)
    date = models.DateTimeField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank = True, null = True)
    price = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return self.name

