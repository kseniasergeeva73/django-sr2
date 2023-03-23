from django.shortcuts import render, redirect
from .models import Seller, Customer
from .forms import SellerForm
from .forms import CustomerForm


def customer(request):
    customers = Customer.objects.order_by('last_name')

    return render(request, 'customer.html', {'customers': customers})


def seller(request):
    sellers = Seller.objects.order_by('company_name')

    return render(request, 'seller.html', {'sellers': sellers})


def sellers(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sellers/')
    else:
        form = SellerForm()

    return render(request, 'forms.html', {'form': form})


def customers(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data
            new = Customer(
                name=result['name'],
                last_name=result['last_name'],
                phone=result['phone'])
            new.save()
            return redirect('/customers/')
    else:
        form = CustomerForm()

        return render(request, 'forms.html', {'form': form})