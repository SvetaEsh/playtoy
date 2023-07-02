from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from .forms import CreationForm, UserForm, ProfileForm 
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages

# Create your views here.
class LoginView(auth_views.LoginView):
    template_name = 'staff/login.html'

class LogoutView(auth_views.LogoutView):
    template_name='staff/logout.html'

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("staff:login")
    template_name = "staff/signup.html"

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Ваш профиль успешно редактирован!'))
            return redirect('staff:profile')
        else:
            messages.error(request, ('Пожалуйста, проверьте информацию ниже.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'staff/user_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



#profile = Profile.objects.create(user=new_user)
    
"""
class ShowProfilePageView(DetailView):
    model = models.Profile
    template_name = 'staff/user_profile.html'
    form_class = forms.UserForm


    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context
   
"""
