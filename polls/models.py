import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    class Meta:
        verbose_name = '質問'
        verbose_name_plural = '質問の複数形'
        ordering = ['-pub_date']
    question_text = models.CharField(max_length=200,default='xxxx')
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    # question = models.ForeignKey('polls.Question',on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

