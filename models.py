from django.db import models

# Create your models here.
class Client(models.Model):
    Id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=30)
    CreatedBy=models.CharField(max_length=30)
    class Meta:                                                       
        db_table='client101'

class User(models.Model):
    Id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=30)
    CreatedBy=models.CharField(max_length=30)
    class Meta:
        db_table='User102'

