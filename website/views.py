from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request,'home.html',{})

def contact(request):
    if request.method == "POST":
        #find navnene på de der bokse der er i contact informationen. (linje 200 i cotnact html)
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message =request.POST['message']

        # send email
        send_mail(
            message_name, #subject
            message, #message
            message_email, #from
            ["lind1994@hotmail.com"], #to
            fail_silently=False,
        )


        return render(request, 'contact.html', {'message_name':message_name})

    else:
        return render(request,'contact.html',{})
