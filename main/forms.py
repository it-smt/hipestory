from django import forms


class CommentForm(forms.Form):
    body = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'comments__input',
    }))
