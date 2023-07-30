from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            {
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio da classe'
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para eu usuário'
    )

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'description')
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
        
        if first_name.upper() in ['ATC', 'BOI', 'UTA']:
            self.add_error(
                'first_name',
                ValidationError("Don't use bad words.")
            )

        return first_name