from django.db import models

class Expense(models.Model):
    """Expense model to represent an expense entry."""

    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    #category choice
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Entertainment', 'Entertainment'),
        ('Utilities', 'Utilities'),
        ('Other', 'Other'),
    ]
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f'{self.name} - {self.amount}'  
    
