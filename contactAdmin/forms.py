from django import forms


class ContactAdminForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "u-border-1 u-border-grey-80 u-border-radius-6 u-grey-80 u-input u-input-round",
                   "id": "name-d050","placeholder": "موضوع"}),label=" ")

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "u-border-1 u-border-grey-80 u-border-radius-6 u-grey-80 u-input u-input-round",
                   "id": "message-d050",
                         "placeholder": "پیغام خود را بنویسید"}),label=" ")



