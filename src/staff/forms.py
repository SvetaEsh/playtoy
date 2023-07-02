from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()





#  создадим собственный класс для формы регистрации
#  сделаем его наследником предустановленного класса UserCreationForm
class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # укажем модель, с которой связана создаваемая форма
        model = User
        # укажем, какие поля должны быть видны в форме и в каком порядке
        fields = ('first_name', 'last_name', 'username', 'email') 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('telefon', 'home_adress', 'additional_info')