import datetime
from django.db import models
from django.utils import timezone
from jsonfield import JSONField


class Pollster(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    organization = models.CharField(max_length=100)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    pollster = models.ForeignKey(Pollster, on_delete=models.CASCADE)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Response(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    choice = models.OneToOneField(Choice, on_delete=models.CASCADE)
    respondent_name = models.CharField(max_length=100)
    response_date = models.DateField()


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)


class Log(models.Model):
    path = models.TextField()
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    query = models.TextField()
    json = JSONField()


class Reminder(models.Model):
    email = models.EmailField()
    text = models.TextField()
    datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
