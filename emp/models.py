from django.db import models
from django.contrib.auth.models import User

class department(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="قطاعات"

class emp(models.Model):
    الاسم=models.CharField(max_length=50)
    
    المرتب=models.FloatField()
    القطاع=models.ForeignKey(department,on_delete=models.CASCADE)
    def __str__(self):
        return self.الاسم
    class Meta:
        verbose_name="موظفين"
        
class suppliers(models.Model):
    الاسم=models.CharField( max_length=50)
    اسم_المورد=models.CharField( max_length=50)
    العنوان=models.CharField( max_length=50)
    رقم_التواصل=models.DecimalField(max_digits=12,decimal_places=0)
    def __str__(self):
        return self.الاسم
    class Meta:
        verbose_name="موردين"
        