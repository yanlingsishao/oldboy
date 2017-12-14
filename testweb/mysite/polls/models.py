from django.db import models
import datetime
from django.utils import timezone
# Create yofrom polls.models import Question, Choiceur models here.

class Question(models.Model):
    # ...
    def __str__(self):  # __unicode__ on Python 2
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # ...
    def __str__(self):  # __unicode__ on Python 2
        return self.choice_text
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)