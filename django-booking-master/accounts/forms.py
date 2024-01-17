from django import forms
from allauth.account.forms import SignupForm


class SignupUserForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='姓')
    last_name = forms.CharField(max_length=30, label='名')


    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='姓')
    last_name = forms.CharField(max_length=30, label='名')
    description = forms.CharField(label='自己紹介', widget=forms.Textarea(), required=False) # required=Falseで必須項目ではない.textareaで複数行入力可能に
    image = forms.ImageField(required=False, )
