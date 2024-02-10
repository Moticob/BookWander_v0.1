# views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

def signup(request):
    if request.method == 'POST':
        # Get form data
        your_name = request.POST.get('your_name', '')
        your_email = request.POST.get('your_email', '')
        your_password = request.POST.get('your_password', '')

        # Save data to your database if necessary

        # Send an email with the form information
        subject = 'New Signup on BookWander'
        message = f'Name: {your_name}\nEmail: {your_email}\nPassword: {your_password}'
        from_email = 'your_email@example.com'
        recipient_list = ['your_email@example.com']

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        # Redirect the user to a confirmation page
        return HttpResponseRedirect(reverse('confirmation_page'))

    return render(request, 'landing_page/BookWander-Landing.html')
