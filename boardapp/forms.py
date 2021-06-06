from django.forms import forms,CharField
from boardapp.models import Post
class TextForm(forms.Form):
    title = CharField(
        initial='',
        label='title',
        max_length=10000,
        required=True,  # 必須
    )
    text = CharField(
        initial='',
        label='memo',
        max_length=10000,
        required=True,  # 必須
    )
    mytext = CharField(
        initial='',
        label='mymemo',
        max_length=10000,
        required=True,  # 必須
    )

    def save(self):
        data = self.cleaned_data
        post = Post(title = data['title'],text=data['text'],mytext=data['mytext'])
        post.save()



from django.contrib.auth import forms as auth_forms

class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label
