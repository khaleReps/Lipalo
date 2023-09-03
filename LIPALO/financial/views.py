from django.shortcuts import render
from .models import Income, Expense, Investment

def dashboard(request):
    # Fetch and process data for the dashboard
    # You can use Python libraries like Pandas for data manipulation
    context = {
        'income_data': income_data,
        'expense_data': expense_data,
        'investment_data': investment_data,
    }
    return render(request, 'finance/dashboard.html', context)
