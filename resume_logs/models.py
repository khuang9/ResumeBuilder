from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
  text = models.CharField(max_length = 200)
  resume_text = models.TextField()
  date_added = models.DateTimeField(auto_now_add = True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  question_index = models.PositiveIntegerField(default=0)
  
  def __str__(self):
    """ Return a string representation of the model. """
    return self.text

class Entry(models.Model):
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  section = models.TextField(default="")
  sender = models.TextField(default="Anonymous Sender")
  text = models.TextField(blank=True)
  gpt = models.TextField()
  keyword = models.TextField() 
  date_added = models.DateTimeField(auto_now_add = True)
  
  class Meta:
    verbose_name_plural = 'entries'
    
  def __str__(self):
    return f"{self.text[:50]}..."
  
class QuestionHistory(models.Model):
  question = models.TextField()
  answer = models.TextField()
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    """ Return a string representation of the model. """
    return self.text

