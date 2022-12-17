from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from .filters import OrderFilter
from .models import *
from .forms import OrderForm


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders,
               'customers': customers,
               'total_orders': total_orders,
               'delivered': delivered,
               'pending': pending}

    return render(request, "accounts/dashboard.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "accounts/register.html", context)


def login(request):
    context = {}
    return render(request, "accounts/login.html", context)


def products(request):
    _products = Product.objects.all()
    return render(request, "accounts/products.html", {"products": _products})


def customer(request, pk):
    _customer = Customer.objects.get(id=pk)
    orders = _customer.order_set.all()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {
        "customer": _customer,
        "orders": orders,
        "myFilter": myFilter
    }
    return render(request, "accounts/customer.html", context)


def create_order(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=("product", "status"), extra=3)
    _customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=_customer)
    if request.method == "POST":
        formset = OrderFormSet(request.POST, instance=_customer)
        if formset.is_valid():
            formset.save()
            return redirect("/")

    context = {"formset": formset}
    return render(request, "accounts/order_form.html", context)


def update_order(requests, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if requests.method == "POST":
        form = OrderForm(requests.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(requests, "accounts/order_form.html", context)


def delete_order(requests, pk):
    order = Order.objects.get(id=pk)
    if requests.method == "POST":
        order.delete()
        return redirect("/")
    context = {"item": order}
    return render(requests, "accounts/delete.html", context)
