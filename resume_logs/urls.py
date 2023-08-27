"""resume_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from . import views

app_name = 'resume_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
	
	# Topic related pages
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
    # Adding a new user answer
    path('new_answer/<int:topic_id>/', views.new_answer, name='new_answer'),
	
	# Q & A page functions
    path('q_and_a/', views.q_and_a, name='q_and_a'),
    path('send_question/', views.send_question, name='send_question'),
    
	# Resume generation function URLs
    path('generate_resume/', views.generate_resume, name='generate_resume'),
    path('extract_entries/', views.extract_entries, name='extract_entries'),
	
	# File generation function URLs
    path('generate_txt/', views.generate_txt, name='generate_txt'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('generate_docx/', views.generate_docx, name='generate_docx'),
    ]
