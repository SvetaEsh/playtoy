from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import forms

# Create your views here.
def send_email(request):
    if request.method=="GET":
        form=forms.FeedbackForm()
        return render(request, template_name="feedback/send-email.html", context={'form': form})
    else:
        form=forms.FeedbackForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
        else:
            return render(request, template_name="feedback/send-email.html", context={'form': form})
