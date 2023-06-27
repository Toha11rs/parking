from django.db import models


class User(models.Model):
    Name = models.CharField(max_length=20)
    Surname = models.CharField(max_length=20)
    PhoneNumber = models.IntegerField()

    class Meta:
        db_table = 'user'

class Car(models.Model):
    Number = models.CharField(max_length=20)
    User = models.ForeignKey(User, on_delete=models.CASCADE,default="none")

    class Meta:
        db_table = 'car'

    def __str__(self):

        return (f"{self.Number}")

class Transaction(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE,default="none")
    date_arrival = models.DateTimeField()
    date_departure = models.DateTimeField()
    price = models.IntegerField()

    class Meta:
        db_table = 'transaction'

class parking_place(models.Model):
    Place_number = models.IntegerField()
    Availability = models.BooleanField()
    car = models.ForeignKey(Car,on_delete=models.CASCADE,default="none")

    class Meta:
        db_table = 'parking_places'