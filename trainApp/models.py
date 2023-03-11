from django.db import models

# Create your models here.

class UserDetails(models.Model):

    gender_choose = (('M', 'Male'),('F', 'Female'),('O', 'Others'))
    from_choose = (('HYD','Hyderabad'),('MB','Mumbai'),('T','Tirupati'),('ND','New Delhi'),('TN','Tamil Nadu'),('VIZ','Vizag'),('KAR','Karnataka'))
    to_choose = (('HYD','Hyderabad'),('MB','Mumbai'),('T','Tirupati'),('ND','New Delhi'),('TN','Tamil Nadu'),('VIZ','Vizag'),('KAR','Karnataka'))
    #train_seat_types = (('GEN','General'),('LB/ SR','Lower Berth / SR Citizen'),('PD','Person With Disabilty'),('NT','New Tatkal'),('PT','Premium Tatkal'))


    #Name = models.CharField(max_length=1000)
    #Email = models.EmailField(max_length=1000)
    From_location = models.CharField(max_length=7,choices=from_choose)
    To_location = models.CharField(max_length=7,choices=to_choose)
    Mobile = models.CharField(max_length=1000)
    Date = models.DateField()
    Gender = models.CharField(max_length=1,choices=gender_choose)

    #Train_Seat = models.CharField(max_length=6,choices=train_seat_types)



