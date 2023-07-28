from django.db import models

class Currency(models.TextChoices):
    EUR = "EUR",
    GBP = "GBP",
    CAD = "CAD",
    JPY = "JPY"


class ExpenseType(models.TextChoices):
    Accomodation = "Accomodation",
    Transportation = "Transportation",
    Food = "Food",
    Services = "Services",
    Hobbies = "Hobbies",
    Turism = "Turism",
    Misc = "Misc" 

class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=ExpenseType.choices)
    cost = models.DecimalField(decimal_places=2, max_digits=7)
    currency = models.CharField(max_length=3, choices=Currency.choices)
    date = models.DateTimeField()
    rates = models.JSONField()

    class Meta:
        db_table = "expenses"
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"





