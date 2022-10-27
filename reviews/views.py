from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import CommentForm
from django.http import JsonResponse


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
