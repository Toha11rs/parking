from django.shortcuts import get_object_or_404, redirect, render
from parking import models
from base.forms import TransactionForm
from django.db.models import Sum
from django.db.models import Q

def main(request):
    transaction = models.Transaction.objects.all()
    free_spots = models.parking_place.objects.filter(Availability=0).count()
    occupied_spots = models.parking_place.objects.filter(Availability=1).count()

    search_query = request.GET.get('search')

    if search_query:
        transaction = transaction.filter(
            Q(car__Number__icontains=search_query) |
            Q(car__User__PhoneNumber__icontains=search_query) |
            Q(date_arrival__icontains=search_query) |
            Q(date_departure__icontains=search_query) |
            Q(price__icontains=search_query)
        )

    sort_param = request.GET.get('sort')


    if sort_param == 'price':
       sorte = models.Transaction.objects.order_by('price')
    else:
        sorte = models.Transaction.objects.all()
    
    context = {
        "transactions": transaction,
        "free_spots": free_spots,
        "occupied_spots": occupied_spots,
        'search_query': search_query,
        'sorte':sorte
      
    } 
    return render(request, 'base/main.html', context)

def create_transaction(request):
    form = TransactionForm()

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    cars = models.Car.objects.all()  
    return render(request, 'base/create_transaction.html', {'form': form, 'cars': cars})


def delete_transaction(request, id):
    transaction = models.Transaction.objects.get(id=id)
    transaction.delete()
    return redirect('main')


def edit_transaction(request, pk):
    transaction = get_object_or_404(models.Transaction, pk=pk)
    
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = TransactionForm(instance=transaction)
    
    return render(request, 'base/edit_transaction.html', {'form': form})
