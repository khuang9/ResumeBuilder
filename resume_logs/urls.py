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
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    
    #path('topics_editprofile/', views.topics_editprofile, name='topics_editprofile'),
    #path('topics_editprofile/<int:topic_id>/', views.topic_editprofile, name='topic_editprofile'),
    
    #path('new_topic_editprofile/', views.new_topic_editprofile, name='new_topic_editprofile'),
    # Page for adding a new entry
    #path('new_entry_editprofile/<int:topic_id>/', views.new_entry_editprofile, name='new_entry_editprofile'),
    # Page for editing an entry.
    path('edit_entry_editprofile/<int:entry_id>/', views.edit_entry_editprofile, name='edit_entry_editprofile'),
    
    #path('view_profile', views.view_profile, name='view_profile'),
    path('generate_resume/', views.generate_resume, name='generate_resume'),
    path('extract_entries/', views.extract_entries, name='extract_entries'),
    path('generate_txt/', views.generate_txt, name='generate_txt'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('generate_docx/', views.generate_docx, name='generate_docx'),
    path('q_and_a/', views.q_and_a, name='q_and_a'),
    path('send_question/', views.send_question, name='send_question'),
    
    path('generate_section/<int:entry_id>/', views.generate_section, name='generate_section'),
    path('download/', views.download_template, name='download_template'),
    path('topics/ai_advisor/', views.ai_advisor, name='ai_advisor'),
 
    ]
