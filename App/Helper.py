from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings




def sendMail(recipient_list = [], subject_string = "", html_template = "", context = {}):
    try: 
        email_from = settings.EMAIL_HOST_USER
        if html_template == "":
            raise ValueError("html template must be a valid tamplate string")
        if subject_string == "":  
            raise ValueError("subject string must be a valid string")
        
        html_message = render_to_string(html_template, context=context)
        message = EmailMessage(subject_string, html_message,email_from, recipient_list)
        message.content_subtype = 'html'
        message.send(fail_silently=False)
    except Exception as e:
        print(e)
        
