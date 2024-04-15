from django import forms
from django.core.exceptions import ValidationError

class FormLogin(forms.Form):
    nome = forms.CharField(
        label='Nome de login',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: joao'})
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )

class FormCadastro(forms.Form):
    nome = forms.CharField(
        label='Nome de cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: joao'})
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: joao@example.com'})
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )
    confirmar_senha = forms.CharField(
        label='Confirmar Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'})
    )
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if ' ' in nome:
            raise forms.ValidationError('Não é possível inserir espaços dentro do nome de usuário!')
        return nome.strip()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        allowed_domains = ['gmail.com', 'outlook.com','yahoo.com','hotmail.com']
        email_domain = email.split('@')[-1]
        if email_domain not in allowed_domains:
            raise ValidationError(f'Por favor, utilize um e-mail com os seguintes domínios: {", ".join(allowed_domains)}')
        return email

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')
        if senha and confirmar_senha and senha != confirmar_senha:
            self.add_error('confirmar_senha', 'As senhas não são iguais!')