from django import forms
from contact.models import Contact


# write your forms here 

class  contactForm(forms.ModelForm):

	class Meta :
		model =Contact
		fields =['name','email','subject','message']

	

