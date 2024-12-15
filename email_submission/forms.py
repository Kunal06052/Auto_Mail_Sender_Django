from django import forms

class AssignmentSubmissionForm(forms.Form):
    screenshot = forms.FileField(label='Screenshot of the form filled via code')
    source_code = forms.URLField(label='Source Code (GitHub repository)')
    documentation = forms.FileField(label='Brief documentation of your approach')
    resume = forms.FileField(label='Your resume')
    project_links = forms.CharField(widget=forms.Textarea, label='Links to past projects/work samples')
    availability = forms.CharField(label='Confirm your availability to work full time (10 am to 7 pm) for the next 3-6 months')