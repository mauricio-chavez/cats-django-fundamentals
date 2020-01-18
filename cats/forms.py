"""Cats app forms"""

from django import forms
from django.utils import timezone

from .models import Cat


class CatForm(forms.Form):
    name = forms.CharField()
    breed = forms.CharField()
    age = forms.IntegerField()

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'Chanchito':
            raise forms.ValidationError('El gato no se puede llamar Chanchito')
        return name

    def save(self, request):
        data = self.cleaned_data
        data['birthday'] = timezone.now()
        data['owner'] = request.user

        return Cat.objects.create(**data)


class CatModelForm(forms.ModelForm):
    """Form definition for Cat."""
    class Meta:
        """Meta definition for Catform."""
        model = Cat
        fields = ['name', 'breed', 'age']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'Chanchito':
            raise forms.ValidationError('El gato no se puede llamar Chanchito')
        return name

    def save(self, request):
        data = self.cleaned_data
        data['birthday'] = timezone.now()
        data['owner'] = request.user

        return Cat.objects.create(**data)
