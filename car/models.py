from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    vin = models.CharField(max_length=255,blank=True, null=True)
    license_plate = models.CharField(max_length=20,blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    sell_date = models.DateField(blank=True, null=True)
    year = models.IntegerField()
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    model = models.ForeignKey(
        'Model',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    tire_size = models.IntegerField(blank=True, null=True)
    tire_pressure = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(
        'accounts.MyProfile',
        on_delete=models.CASCADE,
        to_field='user_id',
    )

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
