from django import forms
from .models import Costumer, Seller, Product, Review

class CostumerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Costumer
        exclude = ['points']

class SellerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Seller
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'review_img', 'rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'type': 'hidden', 'id': 'id_rating'}),
        }