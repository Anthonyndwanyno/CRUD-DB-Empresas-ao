from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Empresa

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder': 'E-mail' }))
    fist_name= forms.CharField(label="",max_length="60", widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder': 'Primeiro Nome' }))
    last_name= forms.CharField(label="",max_length="60", widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder': 'Último Nome' }))

    class meta:
        model= User 
        fields= ('username', 'firs_name', 'last_name','email','password1','password2'  )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nome do Utilizador'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Senha'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	
		
class addEmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = ['nif','nome', 'telefone', 'email', 'website', 'descricao', 'id_sector', 'id_endereco']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),  # Definindo um widget para o campo descrição
        }
        exclude = ("user",)

