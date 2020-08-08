from django.db import models
import uuid

# Create your models here.
class Employee(models.Model):
    eid = models.UUIDField( default = uuid.uuid4, editable = False, unique = True)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)

    def __str__(self):
        return self.ename

    class Meta:
        db_table = "employee"