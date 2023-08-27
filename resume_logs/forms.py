from django import forms
from .models import Topic, Entry, QuestionHistory

# Create model forms

class TopicForm(forms.ModelForm):
  
  class Meta:
    model = Topic
    fields = ['text']
    labels = {'text' : ''}
    

class EntryForm(forms.ModelForm):
  
  class Meta:
    model = Entry
    fields = ['text']
    labels = {'text' : 'Info'}
    widgets = {'text' : forms.Textarea(attrs={'cols' : 100, 'rows' : 3})}
    

class PersonalInfoForm(forms.ModelForm):
  
  class Meta:
    model = Entry
    fields = ['text']
    labels = {'text' : 'Info'}
    widgets = {'text' : forms.Textarea(attrs={'cols' : 100, 'rows' : 3})}
  
  
class QuestionForm(forms.ModelForm):
  
  class Meta:
    model = QuestionHistory
    fields = ['question']
    labels = {'question' : 'Info'}
    widgets = {'question' : forms.Textarea(attrs={'cols' : 100, 'rows' : 3})}
  
