from django import forms

from ads.models import Ad


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'text','price']
        labels = {
            'price': 'Precio',
        }