from django import forms
from .models import Category, Auction, Person


class CostsForm(forms.ModelForm):

    class Meta:
        model = Auction
        fields = ('title', 'description', 'Costs',
                  'category', 'person', 'receipt')
        widgets = {'category': forms.Select(choices=Category.objects.all(), attrs={'class': 'form-control'}),
                   'person': forms.Select(choices=Person.objects.all(), attrs={'class': 'form-control'}),
                   'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.TextInput(attrs={'class': 'form-control'}),
                   'Costs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cost', 'title': 'Costs'})}
