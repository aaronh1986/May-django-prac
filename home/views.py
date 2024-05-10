from django.shortcuts import render
from .models import Band


# Create your views here.
def home(request):
    band = Band.objects.all()

    context = {
        'band': band,
    }

    return render(request, 'home/index.html', context)
