from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3
    )

    last_name = forms.CharField(
        required=True,
        min_length=3
    )

    email = forms.EmailField(
        required=True,
        min_length=3
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2'
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError('E-mail already exists.'))


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 
                  'email', 'description', 'category', 'picture')
        # widgets = {
        #     'first_name': forms.TextInput({
        #         'class': 'class-a class-b'
        #     })
        # }
    
    def clean(self) -> dict[str, any]:
        first_name: str = self.cleaned_data.get('first_name')
        last_name: str = self.cleaned_data.get('last_name')

        if first_name.upper() == last_name.upper():
            self.add_error('first_name', ValidationError("First name can't be the same as the last name"))
            self.add_error('last_name', ValidationError("Last name can't be the same as the first name"))

        return super().clean()
    
    def clean_first_name(self):
        first_name: str = self.cleaned_data.get('first_name')
        
        # if first_name.upper() in ['ATC', 'BOI', 'UTA']:
        #     self.add_error(
        #         'first_name',
        #         ValidationError("Don't use bad words.")
        #     )

        return first_name