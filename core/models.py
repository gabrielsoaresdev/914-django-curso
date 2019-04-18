from django.db import models

# Create your models here.



class Person(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    age        = models.IntegerField()

    def __str__ (self):
        return self.first_name + ' ' + self.last_name


class Invite(models.Model):
    person1   = models.ForeignKey(Person, related_name='Person1', on_delete=models.CASCADE)
    person2   = models.ForeignKey(Person, related_name='Person2', on_delete=models.CASCADE)
    date      = models.DateTimeField()
    is_active = models.BooleanField()

    def __str__ (self):
        return self.person1.first_name + ' - ' + self.person2.first_name

class Friend(models.Model):
    friend1   = models.ForeignKey(Person, related_name='Friend1', on_delete=models.CASCADE)
    friend2   = models.ForeignKey(Person, related_name='Friend2', on_delete=models.CASCADE)
    date      = models.DateTimeField()
    is_active = models.BooleanField()

    def __str__ (self):
        return self.friend1.first_name + ' - ' + self.friend2.first_name

class Post(models.Model):
    message   = models.CharField(max_length=240)
    date_time = models.DateTimeField()
    person    = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__ (self):
        return self.message + " - " + self.person.last_name.upper() + ", " + self.person.first_name
