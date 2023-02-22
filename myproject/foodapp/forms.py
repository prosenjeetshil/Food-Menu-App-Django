from models import Food
from django import forms

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'

        labels = {
            'fid': 'Food ID',
            'fname': 'Food Name',
            'fdesc': 'Food Description',
            'fprice': 'Food Price'
        }

        widgets = {
            'fid': forms.NumberInput(attrs={'placholder': 'e.g 100'}),
            'fname': forms.TextInput(attrs={'placeholder': 'e.g. Butter Chicken'}),
            'fdesc': forms.TextInput(attrs={'placholder': 'e.g Butter chicken, traditionally known as murgh makhani, is an Indian dish originating in New Delhi.'}),
            'fprice': forms.NumberInput(attrs={'placholder': 'e.g ₹449'})
        }