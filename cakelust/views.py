from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def home(request):

    gallery = Gallery.objects.all().order_by('-id')[:6]
    review = Review.objects.all().order_by('-id')

    form = reviewsForm()

    if request.method == 'POST':
        form = reviewsForm(request.POST)
        if form.is_valid():
            form = form.save()

            messages.success(request, "Thank you for your comment.")
            return redirect('home')

    context = {
        'gallery':gallery,
        'form':form,
        'review':review,
    }
    return render (request, 'cakelust/index.html', context=context)


def gallery(request):
    
    gallery = Gallery.objects.all().order_by('-id')[:10]

    context = {
        'gallery':gallery,
    }
    return render (request, 'cakelust/gallery.html', context=context)


def priceguide(request):

    pricelist = Pricelist.objects.all().order_by('-id')[:1]

    context = {
        'pricelist':pricelist,
    }
    return render (request, 'cakelust/priceguide.html', context=context)


def flavours(request):

    cake = Cake.objects.all()

    context = {
        'cake':cake,
    }
    return render (request, 'cakelust/flavours.html', context=context)

def order(request):

    context = {
    }
    return render (request, 'cakelust/order.html', context=context)
