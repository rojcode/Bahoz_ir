from django import forms
from django.contrib.auth import get_user_model,login,authenticate
from django.core import validators

User = get_user_model()


class register_form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "u-border-4 u-border-grey-80 u-border-radius-4 u-grey-80 u-input u-input-round u-input-1",
                   "placeholder": "نام کاربری خود را وارد کنید","id": "name-f344"}),label=" ")
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "u-border-4 u-border-grey-80 u-border-radius-4 u-grey-80 u-input u-input-round u-input-2",
                   "id": "email-f344","placeholder": "ایمیل خود را وارد کنید"}),label=" ")

    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'شمارە تلفن',"id": "text-fd41",
                                      "class": "u-border-4 u-border-grey-80 u-border-radius-4 u-grey-80 u-input "
                                               "u-input-round u-input-3"}),
        label=" ")

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "u-border-4 u-border-grey-80 u-border-radius-4 u-grey-80 u-input u-input-round u-input-4",
                   "id": "text-9f43","placeholder": "رمز خود را وارد کنید"}),label=" ")

    password_again = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "u-border-4 u-border-grey-80 u-border-radius-4 u-grey-80 u-input u-input-round u-input-5",
                   "id": "text-3cd5","placeholder": "رمز خود را دوبارە وارد کنید"}),label=" ")

    image_profile = forms.ImageField(required=True,label='انتخاب عکس پروفایل')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("این نام کاربری توسط شخص دیگری استفادە شدە است")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("این ایمیل توسط شخص دیگری استفادە شدە است")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password_again")
        if password != password2:
            raise forms.ValidationError("رمز ها با هم مغایرت دارند")
        return data





