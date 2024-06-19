from django.db import models

# Create your models here.
class Foodtype(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Food(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    amount = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    cost_time = models.IntegerField(default=0)
    foodType = models.ForeignKey(
        'Foodtype', to_field="ID", on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
class Staff(models.Model):
    ID = models.AutoField(primary_key=True)         # 員工ID
    # citizenID = models.CharField(max_length=20)     # 身分證字號
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=20, choices=(
        ('male', '男'), ('female', '女')), default='male')
    born_date = models.DateField(null=True)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name
    
class Table(models.Model):
    ID = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=20)
    staff = models.ForeignKey('Staff', on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.ID) + ' ' + self.name