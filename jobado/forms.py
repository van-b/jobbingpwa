#-*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import *

class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = Poster
		fields = UserCreationForm.Meta.fields + ('district', 'sex', 'last_name', 'first_name', 'email', 'phone_number', 'photo',)

class CustomUserChangeForm(UserChangeForm):

	class Meta(UserChangeForm.Meta):
		model = Poster
		fields = UserCreationForm.Meta.fields + ('district', 'sex','last_name', 'first_name', 'email','phone_number', 'photo',)

class JobberCreationForm(CustomUserCreationForm):
	categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
	class Meta(CustomUserCreationForm.Meta):
		model = Jobber
		fields = CustomUserCreationForm.Meta.fields + ('biography', 'categories')

class JobberChangeForm(CustomUserChangeForm):

	class Meta(CustomUserChangeForm.Meta):
		model = Jobber
		fields = CustomUserChangeForm.Meta.fields + ('biography', 'categories')

class UserAuthenticationForm(AuthenticationForm):
	pass
	
"""
class BecomeJobberForm(forms.ModelForm):

	class Meta:
		model = Jobber
		fields = ('last_name', 'first_name','categories', 'biography')
"""

class JobForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = ('service', 'description', 'completion_date', 'completion_hour', 'expiration_date', 'jobbers_number', 'unit_price',)

"""
class PosterForm(BSModalForm):
	class Meta:
		model = Poster
		fields = ['district', 'sex', 'username', 'last_name', 'first_name', 'email', 'phone_number', 'photo', 'password']

class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin,UserCreationForm):
	class Meta:
		model = Poster
		fields = ['username', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
	class Meta:
		model = Poster
		fields = ['username', 'password']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
# on decide de valider nous meme notre formulaire
    def clean(self):
        
        cleaned_data = super(ProductForm, self).clean()
        price_ht = cleaned_data.get("price_ht")
        price_ttc = cleaned_data.get("price_ttc")

        if price_ht > price_ttc:
            msg = u"Le prix HT doit être plus élevé que le prix TT"
            self._errors['price_ht'] = self.error_class([msg])

        return cleaned_data
"""
