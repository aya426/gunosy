from django import forms

class URLForm(forms.Form):
    article_url = forms.CharField(
        label='カテゴリ判定したい記事のURLを入力してください',
        required=True,
        max_length = 255,
        widget=forms.Textarea()
    )

    send_message = forms.BooleanField(
        label='送信する',
        required=False,
    )
