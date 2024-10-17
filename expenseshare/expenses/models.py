from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Expense(models.Model):
    EQUAL = 'equal'
    EXACT = 'exact'
    PERCENTAGE = 'percentage'

    SPLIT_METHODS = [
        (EQUAL, 'Equal'),
        (EXACT, 'Exact'),
        (PERCENTAGE, 'Percentage')
    ]

    description = models.CharField(max_length=255)
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    payer = models.ForeignKey(User, related_name='payer', on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='participants')
    splitMethod = models.CharField(max_length=20, choices=SPLIT_METHODS)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.description} - {self.totalAmount}'
