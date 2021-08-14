from django.shortcuts import render

# Create your views here.
def home(request):

    context = {
    }
    return render (request, 'cakelust/index.html', context=context)


def gallery(request):

    context = {
    }
    return render (request, 'cakelust/gallery.html', context=context)


def priceguide(request):

    context = {
    }
    return render (request, 'cakelust/priceguide.html', context=context)


def flavours(request):

    context = {
    }
    return render (request, 'cakelust/flavours.html', context=context)
