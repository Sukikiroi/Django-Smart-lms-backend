from django.db import models

class Customer(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()

class Messages(models.Model):
    name = models.CharField("Name", max_length=240)
    message = models.CharField("message", max_length=240)
    class Meta:
        db_table = 'customer_messages'


class Books(models.Model):
    title = models.CharField("title", max_length=240)
    author = models.CharField("author", max_length=240)
    subtitle = models.CharField("subtitle", max_length=240)
    isbn = models.CharField("isbn", max_length=240)
    date_released = models.CharField("date_released", max_length=240)
    pictur_url = models.CharField("pictur_url", max_length=240)
    description = models.CharField("description", max_length=240)

class Agent(models.Model):
    name = models.CharField("name", max_length=240)
    username = models.CharField("username", max_length=240)
    password = models.CharField("password", max_length=240)

    def __str__(self):
        return self.name