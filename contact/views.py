from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import  contactForm
from django.core.mail import send_mail
from django.shortcuts import render
from .models import Contact
# Create your views here.





class ContactCreate(CreateView):
	template_name ='contact/contact.html'
	form_class =contactForm
	success_url   = "/contact/MessgaeSent"
	def form_valid(self, form):                                                 
		form.save()                                                     
		username = form.cleaned_data['name'] 
		user_full ="There is a message from "+username+" on your site"                       
		email = form.cleaned_data['email']
		subject = form.cleaned_data['subject'] 
		message = form.cleaned_data['message']    
		print(username,email,subject,message)
		send_mail(
			
				user_full,
				message,
				'mohammedfaried364@gmail.com',
				['mohammedfaried364@gmail.com'], 
			    fail_silently=False,
			)
		return super(ContactCreate, self).form_valid(form)  


	




class success(TemplateView):
	template_name ="contact/msg_sent.html"
	



