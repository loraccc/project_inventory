from django.db import models

# Create your models here.
class appuser(models.Model):
    full_name= models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    class meta:
        db_table="app_users"
class items(models.Model):
    title=models.CharField(max_length=100)
    particulars=models.CharField(max_length=200)
    lf=models.CharField(max_length=100,null=True,blank=True)
    quantity=models.IntegerField()
    price=models.FloatField(max_length=200)
    total=models.FloatField(max_length=200)
    added_at=models.DateTimeField(null=True,blank=True)
    user= models.ForeignKey(appuser,on_delete=models.CASCADE)

    class meta:
        db_table="app_items"





