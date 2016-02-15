from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, default='')
    message = models.TextField(default='')
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=200, default='', unique=True)
    answer = models.TextField(default='')
    submit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        unique_together = ('question', 'answer')

    def __str__(self):
        return self.question


class Event(models.Model):
    name = models.CharField(max_length=200, default='')
    content = models.TextField(default='')
    date = models.DateField()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class Host(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    biography = models.TextField(default='')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=200, default='')
    post = models.TextField(default='')
    posted_by = models.ForeignKey(Host)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name
