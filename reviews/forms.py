from django import forms
from .models import Comment, Review


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        labels = {
            "content": "",
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "content", "movie_name", "grade", "category"]
