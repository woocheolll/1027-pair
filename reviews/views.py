from django.shortcuts import render
from .models import Review
# Create your views here.


# Create your tests here.
def index(request):
    review = Review.objects.all().order_by('-pk')
    context = {
        'review':review
    }
    return render(request,'reviews/index.html',context)