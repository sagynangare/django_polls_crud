from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=('bio','phone_no','facebook','instagram','linkedin','image')