from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import CommentForm, ReviewForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def index(request):
    review = Review.objects.all().order_by("-pk")
    context = {"review": review}
    return render(request, "reviews/index.html", context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm()

    context = {
        "review": review,
        "comment_form": comment_form,
    }
    return render(request, "reviews/detail.html", context)


def comments(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        context = {
            "content": comment.content,
            "userName": comment.user.username,
        }
    return JsonResponse(context)


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

def update(request,pk):
    db_data = Review.objects.get(pk=pk)

    if request.method == 'POST':
        data = ReviewForm(request.POST, instance=db_data)

        if data.is_valid():
            data.save()

            return redirect('reviews:index')

    else:
        data = ReviewForm(instance=db_data)

    return render(request, 'reviews/create.html', {'data': data})

