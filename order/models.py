from django.db import models


# Create your models here.

class Details(models.Model):
    name = models.CharField(max_length= 20,help_text= 'Customer Name')
    cont_no = models.CharField(max_length = 12, help_text='Contact Phone Number')
    address = models.CharField(max_length= 200,help_text = 'Delivery Address')
    date = models.DateField()
    time = models.TimeField()
    rice = models.FloatField(help_text= 'Amount of Rice in kg')
    daal = models.FloatField(help_text = 'Amount of Daal in kg')
    salt = models.FloatField(help_text = 'Amount of Salt in kg')
    amount = models.FloatField()
    
    def __str__(self):
        return self.name
