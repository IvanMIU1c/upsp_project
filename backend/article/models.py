
import uuid

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    AccessCheck = models.BooleanField()
    AboutStudent = models.TextField()
    Group = models.ForeignKey('Group', related_name='Group', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Group(models.Model):
    GroupName = models.CharField(max_length=120)
    description = models.TextField()
    def __str__(self):
        return self.GroupName

class AccessData(models.Model):
    Student = models.ForeignKey("Student", related_name="student", on_delete=models.CASCADE)
    DeviceName = models.TextField()

class AccessPending(models.Model):
    DeviceName = models.CharField(max_length=120)
    connected_at = models.DateTimeField(auto_now=False,auto_now_add=True) # data field
    status = models.TextField()
    def __str__(self):
        return self.DeviceName

class AccessQR(models.Model):
    DeviceName = models.TextField()
    qrData = models.UUIDField(primary_key=True, default = uuid.uuid4(), editable = False)  # uuid field
    data = models.DateTimeField(auto_now=False, auto_now_add=False,)  # data field



