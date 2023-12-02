from django.db import models
from accounts.models import User
from groups.models import Group
from django.db.models.signals import pre_save
from django.dispatch import receiver  # Add this import

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=20 , unique=True)
    admin= models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return "Room : "+ self.name + " | Id : " + self.id


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "Message is :- "+ self.content