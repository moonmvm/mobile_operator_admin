from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    passport = models.CharField(max_length=25, blank=False, unique=True)
    date_of_birth = models.DateField()

    class Meta:
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'Client: {self.first_name} {self.last_name}. Phone: {self.phone}'
