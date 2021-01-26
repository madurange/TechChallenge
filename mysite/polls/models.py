import datetime

from django.db import models
from django.utils import timezone

# Questions are unique (Note: Case Sensitivity is in effect)
class Question(models.Model):
    question_text = models.CharField(max_length=200, null=False, unique=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Choice Text is unique for each question. (Note: Case Sensitivity is in effect)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, null=False)
    votes = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['question', 'choice_text'], 
                name='unique choice'
            )
        ]

    def __str__(self):
        return self.choice_text
