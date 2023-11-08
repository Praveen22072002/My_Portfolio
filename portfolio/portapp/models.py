from django.db import models


# Create your models here.

class Registered(models.Model):
    name = models.CharField(max_length=32, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    phone = models.CharField(max_length=13, blank=True)
    comments = models.CharField(max_length=1000, blank=False)
    BUDGET_CHOICES = (
        ('1', '5000-10000'),
        ('2', '10000-20000'),
        ('3', '20000-30000'),
        ('4', 'Above 30000'),
    )

    budget = models.CharField(max_length=2, choices=BUDGET_CHOICES, default='1')

    def __str__(self):
        return "{}".format(self.name)
