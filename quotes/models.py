from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=300, unique=True)
    birth_day = models.CharField(max_length=300)
    bio = models.CharField(max_length=5000)

    def __str__(self):
        return self.fullname


class Quotes(models.Model):
    quote = models.CharField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}: {self.quote}"
