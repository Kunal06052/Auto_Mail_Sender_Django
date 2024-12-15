"""
URL configuration for assignment_submission project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path,include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('email_submission/', include('email_submission.urls')),
# ]
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Create a simple view to redirect to the submission page
def home(request):
    return redirect('submit_assignment')  # Redirect to the assignment submission page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Add this line for the root URL
    path('email_submission/', include('email_submission.urls')),
]