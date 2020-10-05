from django import forms


class Login_form(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "u-border-4 u-border-grey-80 u-border-radius-4 u-grey-80 u-input u-input-round u-input-1",
                   "id": "name-f344","placeholder": "نام کاربری خود را وارد کنید"}),label=" ")

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "u-border-4 u-border-grey-80 u-border-radius-4 u-grey-80 u-input u-input-round u-input-2",
                   "id": "email-f344","placeholder": "رمز عبور خود را وارد کنید"}),label=" ")
