from django import forms


class send_wrong_word(forms.Form):
    farsi = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "u-border-4 u-border-grey-80 u-border-radius-7 u-grey-80 u-input u-input-round u-text-white u-input-1",
            "id": "name-19e6","placeholder": "کلمه"}),label=" ")

    kurdi = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "u-border-4 u-border-grey-80 u-border-radius-7 u-grey-80 u-input u-input-round u-text-white u-input-2",
            "id": "email-19e6","placeholder": "معادل "}),label=" ")


    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "u-border-4 u-border-grey-80 u-border-radius-7 u-grey-80 u-input u-input-round u-text-white u-input-4",
            "id": "message-19e6",
            "placeholder": "علت اشتباە بودن این کلمە را بنویسید یا اگر مشکل دیگری مانند عدم وجود معادل کلمە وجود داشت آن را هم در اینجا بنویسید"}),
        label=" ")
