from django.shortcuts import render
from .models import Review

def index(request):
    review = Review.objects.all().order_by('-pk')
    context = {
        'review':review
    }
    return render(request,'reviews/index.html',context)

def detail(request, pk):
    review = Review.objects.get(pk=pk)

     
    context = {
        'review':review,
    }
    return render(request, 'reviews/detail.html',context)
