from django.contrib import admin
from expenses.models import Expense

class ExpenseSettings(admin.ModelAdmin):
    list_display = ("id", "name", "group", "category", "cost", "currency", "date", "rates")


admin.site.register(Expense, ExpenseSettings)

