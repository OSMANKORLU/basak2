from django import forms
from .models import Home
from captcha.fields import ReCaptchaField




class HomeForm(forms.ModelForm):
	captcha = ReCaptchaField()


	class Meta:
		model = Home
		fields = [
			'title',
			'content',
			'image',
			

		]
'''
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = [
		'name',
		'content'
		]
'''