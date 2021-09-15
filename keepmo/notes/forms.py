from django import forms
from .models import NoteBook, Note, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoteBookForm(forms.ModelForm):
	class Meta:
		model = NoteBook
		fields = ['name', 'description', 'color', 'is_public', 'owner']
		widgets = {'owner': forms.HiddenInput()}


class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = '__all__'
		widgets = {'created_at': forms.HiddenInput(), 'notebook':forms.HiddenInput()}

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class EditProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['photo', 'bio']

	def __init__(self, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)
		self.fields['photo'].required = False