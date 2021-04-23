from django.shortcuts import render, redirect
from .models import WishList
from django.views.generic.edit import CreateView

def index(request):
    wishlist = WishList.objects.all()
    return render(request, 'index.html', { 'wishlist': wishlist })

class WishCreate(CreateView):
    model = WishList
    fields = '__all__'

def delete_wish(request, wish_id):
    WishList.objects.get(id=wish_id).delete()
    return redirect('/')