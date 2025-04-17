from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Item
from .forms import ItemForm

def home(request):
    items = Item.objects.all().order_by('-created_at')
    form = ItemForm()
    
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item added successfully!')
            return redirect('home')
    
    context = {
        'items': items,
        'form': form
    }
    return render(request, 'item_app/home.html', context)