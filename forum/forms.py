from django import forms

from .models import Comment, Message, Tag

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            "content",
        ]

class MessageForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
    )

    class Meta:
        model = Message
        fields = [
            "content",
        ]