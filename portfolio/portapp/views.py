from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.mail import send_mail
import configparser


from .models import Registered
from django.contrib import messages
# Create your views here.


def port(request):
    template = loader.get_template('idea.html')
    return HttpResponse(template.render({}, request))


def project(request):
    template = loader.get_template('project.html')
    return HttpResponse(template.render({}, request))


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({}, request))


def hire(request):
    template = loader.get_template('hire.html')
    return HttpResponse(template.render({}, request))

# Cred from ini file



def registered(request):
    if request.method == 'POST':
        name1 = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("phone")
        comment = request.POST.get("comments")
        choice = request.POST.get("budget")

        if name1 and email and mobile and choice:
            mycreatedrecords = Registered(name=name1, email=email, phone=mobile, comments=comment, budget=choice)
            mycreatedrecords.save()

            # Send the email
            subject = 'New Hire Form Submission'
            message = f"Name: {name1}\nEmail: {email}\nPhone: {mobile}\nComments: {comment}\nBudget: {choice}"
            from_email = "praveenrajvelmurugan@gmail.com"  # Use the email you configured in settings.py
            recipient_list = ["praveenraj22072002@gmail.com"]  # Your email address
            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, "Data has been sent successfully")
            return HttpResponseRedirect(reverse('hire'))
        else:
            messages.error(request, "Enter all details")
            return HttpResponseRedirect(reverse('hire'))

    template = loader.get_template('hire.html')
    return HttpResponse(template.render({}, request))

