from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.contrib.auth.models import User
from datetime import date, datetime
from django.utils import timezone
from .serializers import ExpenseSerializer
from .models import Expense, Currency, ExpenseType
from currency_converter import CurrencyConverter


@csrf_exempt
@api_view(['GET'])
def get_expense(request):
    """
        Returns expense by id
    """
    print(request.GET.get('id', ''))
    if request.method == 'GET':
        return Response({
            "expense": ExpenseSerializer(Expense.objects.get(id=request.GET.get('id', '')), many=False).data
        })



@csrf_exempt
@api_view(['GET'])
def all_expenses(request):
    """
        Returns all expenses
    """
    
    if request.method == 'GET':
        c = CurrencyConverter(fallback_on_missing_rate=True, fallback_on_wrong_date=True)
                
        category = request.GET.get('category', '')        
        expenses = []
        if (category != "All"):
            expenses = Expense.objects.filter(category=category)
        else:
            expenses = Expense.objects.all()
        
        for exp in expenses:
            exp.rates = []
            currencies = [curr.value for curr in Currency]

            for curr in currencies:
                if exp.currency != curr:
                    exp.rates.append(str(round(c.convert(exp.cost, curr, exp.currency, date=date.today()),2)) + " " + curr)


        return Response({
            "expenses": ExpenseSerializer(expenses, many=True).data
        })

@csrf_exempt
@api_view(['POST'])
def new_expense(request):
    """
        Creates a new expense
    """
    if request.method == 'POST':
        expense = Expense(
            name = str(request.data['name']),
            group = str(request.data['group']),
            category = str(request.data['category']),
            cost = float(request.data['cost']),
            currency = str(request.data['currency']),
            date = datetime.now(tz=timezone.utc),
            rates = {}
        )
        expense.save()
        return Response({"success": True})


@csrf_exempt
@api_view(['PUT'])
def edit_expense(request):
    """
        Creates a new expense
    """
    if request.method == 'PUT':
        print(request.data)
        expense = Expense(
            id = str(request.data['id']),
            name = str(request.data['name']),
            group = str(request.data['group']),
            category = str(request.data['category']),
            cost = float(request.data['cost']),
            currency = str(request.data['currency']),
            date = datetime.now(tz=timezone.utc),
            rates = {}
        )
        print(expense)
        expense.save(force_update=True)
        return Response({"success": True})




@csrf_exempt
@api_view(['DELETE'])
def delete_expense(request):
    """
        Creates a new expense
    """
    if request.method == 'DELETE':
        expense = Expense.objects.get(id=request.data['id'])
        expense.delete()
        return Response({"success": True})

