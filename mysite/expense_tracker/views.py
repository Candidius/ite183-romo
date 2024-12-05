from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer
from .forms import TransactionForm
from django.db.models import Sum

class TransactionListCreateAPI(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'expense_tracker/transaction_list.html', {'transactions': transactions})

def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'expense_tracker/transaction_form.html', {'form': form})

def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'expense_tracker/transaction_form.html', {'form': form})

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    return redirect('transaction_list')

def monthly_summary(request):
    summary = Transaction.objects.values('date__month', 'category').annotate(total=Sum('amount'))
    return render(request, 'expense_tracker/monthly_summary.html', {'summary': summary})
