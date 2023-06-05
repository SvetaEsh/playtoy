from django import forms


class FeedbackForm(forms.Form):
    contact_email = forms.EmailField(required = True, label = "Введите Ваш email")
    message = forms.CharField(required = True, label = "Введите Ваше сообщение", widget = forms.Textarea())