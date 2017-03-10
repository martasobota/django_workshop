from django.db import models
from django.db.models.fields.related import ManyToManyField, ForeignKey
from random import choices

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=64)
    description = models.TextField()
    
    def __str__(self):
        return 'Name: {}, Surname: {}, Description: {}'.format(self.name,self.surname, self.description)
    
class Address(models.Model):
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=64)
    home_number = models.IntegerField()
    flat_number = models.IntegerField(null=True)
    person = ForeignKey(Person)
    
    def __str__(self):
        return 'street: {}, home number: {}, flat number: {}, city: {}'.format(
            self.street, 
            self.home_number, 
            self.flat_number,
            self.city)

TEL_TYPES = (
    (1, "home"),
    (2, "work"),
    (3, "private")
     )

class Phone(models.Model):
    telephone_number = models.CharField(max_length=32)
    type = models.IntegerField(choices=TEL_TYPES)
    person = ForeignKey(Person)
    
    def __str__(self):
        return 'Telephone number: {}, type: {}'.format(
            self.telephone_number, 
            self.type)
    
MAIL_TYPES = (
    (1, "private"),
    (2, "official"),
     )
    
class Email(models.Model):
    e_mail = models.CharField(max_length=64)
    type = models.IntegerField(choices=MAIL_TYPES)
    person = ForeignKey(Person)
    
    def __str__(self):
        return 'E-mail address: {}, type: {}'.format(
            self.e_mail, 
            self.type)
    