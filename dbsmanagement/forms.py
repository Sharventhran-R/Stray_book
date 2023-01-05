from django import forms
from .models import Info

class InfoForm(forms.ModelForm):
	class Meta:
		model = Info
		fields = ['number', 'name', 'animal', 'comments', 'image', 'barcode']

	def clean_animal(self):
		animal = self.cleaned_data.get('animal')
		if not animal:
			raise forms.ValidationError('This field is required')
		return animal


# def clean_date(self):
#     date = self.cleaned_data.get('date')
#     if not date:
#         raise forms.ValidationError('This field is required')
#     return date
class InfoSearchForm(forms.ModelForm):
	class Meta:
		model = Info
		fields = ['name', 'animal']

class InfoUpdateForm(forms.ModelForm):
	class Meta:
		model = Info
		fields = ['number', 'name', 'animal', 'comments', 'image', 'barcode']

