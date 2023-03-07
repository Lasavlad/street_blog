from django import forms
from .models import Comment

class Comment_form(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 60,}))

    class Meta:
        model = Comment
        fields = ('body',)