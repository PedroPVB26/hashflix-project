from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

# forms.Form é o form padrão do Django
class FormHomepage(forms.Form):
    email = forms.EmailField(label=False)

class CriarContaForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ('username','email', 'password1', 'password2')