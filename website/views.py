from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request): 
	return render(request, 'home.html', {})

def contact(request): 
	if request.method =="POST":
		#do stuf
		message_name =request.POST['message-name']
		message_email = request.POST['message-email']
		message= request.POST['message']
		return render(request, 'contact.html', {'message_name': message_name})

		# Send email
		send_mail(
			message_name,
			message,
			message_email,
			['mehtabbandesha@gmail.com'],
			fail_silently=False,
			)


	else:
		# return the page
		return render(request, 'contact.html', {})