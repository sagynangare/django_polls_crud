from django import forms
from .models import Question, Choice
from django.utils import timezone

class QuestionForm(forms.ModelForm):
	question_text =forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Question",
												"class":"form-control"}))
	pub_date=forms.DateTimeField(initial=timezone.now())

	class Meta:
		model=Question
		fields="__all__"#('question_text',)

class ChoiceForm(forms.ModelForm):
	choice_text =forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Choice",
												"class":"form-control"}))

	votes = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter Votes",
									"class":'form-control'}))

	class Meta:
		model=Choice
		fields="__all__"
