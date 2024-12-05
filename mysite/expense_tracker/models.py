from django.db import models

class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.category.capitalize()} - {self.amount} on {self.date}"