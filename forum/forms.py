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
            # 15で追加
            "image",
        ]

# 17で追加
class MessageSearchForm(forms.Form):

    keyword = forms.CharField(
        label="検索",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "メッセージで検索"}),
    )

