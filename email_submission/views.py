from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import AssignmentSubmissionForm
from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    return render(request, 'email_submission/home.html')  

def submit_assignment(request):
    if request.method == 'POST':
        form = AssignmentSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            # Prepare email
            subject = f"Python (Selenium) Assignment - {request.POST.get('name')}"
            body = f"""
            Dear Hiring Team,

            Please find attached the required documents for the Selenium Automation Developer Internship Assignment.

            1. Screenshot: {form.cleaned_data['screenshot'].name}
            2. Source Code: {form.cleaned_data['source_code']}
            3. Documentation: {form.cleaned_data['documentation'].name}
            4. Resume: {form.cleaned_data['resume'].name}
            5. Project Links: {form.cleaned_data['project_links']}
            6. Availability: {form.cleaned_data['availability']}

            Best regards,
            {request.POST.get('name')}
            """

            email = EmailMessage(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                ['25073@arsd.du.ac.in'],
                cc=['atr.kunal0506@gmail.com'],
            )

            # Attach files
            email.attach(form.cleaned_data['screenshot'].name, form.cleaned_data['screenshot'].read(), 'image/png')
            email.attach(form.cleaned_data['documentation'].name, form.cleaned_data['documentation'].read(), 'application/pdf')
            email.attach(form.cleaned_data['resume'].name, form.cleaned_data['resume'].read(), 'application/pdf')

            # Send the email
            email.send()

            return HttpResponse("Email sent successfully!")
    else:
        form = AssignmentSubmissionForm()

    return render(request, 'email_submission/submit_assignment.html', {'form': form})