from django.db import models
from datetime import datetime


class FillUp(models.Model):

    FILL_UPS = (
        (1, "Partial"),
        (2, "Full")
    )

    OCTANE = (
        ('', ''),
        ('87', '87'),
        ('89', '89'),
        ('92', '92'),
        ('diesel', 'Diesel')
    )
    car = models.ForeignKey(
        'car.Car',
        on_delete=models.CASCADE
    )
    odometer = models.IntegerField(blank=True, null=True)
    unit_cost_per = models.FloatField(blank=True, null=True)  # Cost/Gallon
    unit_quantity = models.FloatField(blank=True, null=True)  # Gallons
    total_cost = models.FloatField(blank=True, null=True)
    fuel_economy = models.FloatField(blank=True, null=True)   # Miles / Gallon
    date_time = models.DateTimeField(blank=True, null=True)  # user input
    created_at = models.DateField(auto_now_add=True)  # meta data
    updated_at = models.DateField(auto_now=True)  # meta data
    filled_up = models.IntegerField(
        choices=FILL_UPS,
        default=FILL_UPS[1][0]
    )
    octane = models.CharField(
        choices=OCTANE,
        default=OCTANE[1][0],
        blank=True,
        null=True,
        max_length=20
    )
    fuel_brand = models.ForeignKey(
        'Brand',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    tags = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    services = models.CharField(max_length=255, blank=True, null=True)

    payment = models.ForeignKey(
        'Payment',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    user = models.ForeignKey(
        'accounts.MyProfile',
        on_delete=models.CASCADE,
        to_field='user_id',
    )

    def __str__(self):
        return str(self.date_time)

    def adjust_fuel_amounts_and_cost(self):

        if self.unit_quantity is None or self.unit_cost_per is None:
            self.total_cost = None
            return

        unit_quantity = float(self.unit_quantity)
        unit_cost_per = float(self.unit_cost_per)

        if unit_quantity == 0 or unit_cost_per == 0:
            self.total_cost = None
        elif unit_quantity > 0 and unit_cost_per > 0:
            self.total_cost = str(round(self.unit_quantity * self.unit_cost_per, 2))

    def save(self, *args, **kwargs):
        if 'is_import' not in kwargs:
            self.adjust_fuel_amounts_and_cost()
        else:
            del kwargs['is_import']

        if self.date_time is None:
            self.date_time = datetime.now()

        super(FillUp, self).save(*args, **kwargs)

    def make_floats(self):
        self.unit_quantity = float(self.unit_quantity)
        self.unit_cost_per = float(self.unit_cost_per)

    @property
    def formatted_total_cost(self):
        return self.format_price(self.total_cost)

    @property
    def formatted_unit_cost(self):
        return self.format_price(self.unit_cost_per)

    @staticmethod
    def format_price(value):
        if value is None:
            return "0.00"
        else:
            return "{:.2f}".format(value)

    @staticmethod
    def key_for_fill_up_value(value):
        value = str(value)
        for fill in FillUp.FILL_UPS:
            if value.lower() == fill[1].lower():
                return fill[0]

        return None

    def set_properties_from_form(self, values):
        # validate the keys are legit
        for key, value in values.items():
            setattr(self, key, value)

        return


class Brand(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        'accounts.MyProfile',
        on_delete=models.CASCADE,
        to_field='user_id',
    )

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        'accounts.MyProfile',
        on_delete=models.CASCADE,
        to_field='user_id',
    )

    def __str__(self):
        return self.name


class Payment(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        'accounts.MyProfile',
        on_delete=models.CASCADE,
        to_field='user_id',
    )

    def __str__(self):
        return self.name

# class FuelUnit(models.Model):
#     name = models.CharField(max_length=30)
#
