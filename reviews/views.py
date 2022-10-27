from django.shortcuts import render,redirect
from .models import Review

from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


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


@login_required
def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            db_review_form = review_form.save(commit=False)
            db_review_form.user = request.user
            db_review_form.save()
            return redirect('reviews:index')
    else:
        review_form = ReviewForm()
    return render(request,'reviews/create.html',{'review_form':review_form})

