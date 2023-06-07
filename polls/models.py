import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    # ...
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

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


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'was_published_recently']  # Use 'was_published_recently' method here
    list_filter = ['pub_date']  # Update with valid fields


admin.site.register(Question, QuestionAdmin)
