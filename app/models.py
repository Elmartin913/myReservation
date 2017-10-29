from django.db import models

# Create your models here.

class Room(models.Model):
    proj_stat = ((1, 'dostepny'),(2, 'brak'))
    name = models.CharField(max_length=64)
    capacity = models.IntegerField(null=True)
    description =  models.TextField(null=True)
    projector =models.IntegerField(choices=proj_stat, null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    date = models.DateField(null=True)
    room = models.ForeignKey(Room, null=True, related_name='room')
    comments = models.TextField(null=True)

    def __str__(self):
        return str(self.date)+' - '+ str(self.room)