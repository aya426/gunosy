from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(
        label='カテゴリ判定したい記事のURLを入力してください',
        required=True,
        max_length = 255,
        widget=forms.Textarea()
    )