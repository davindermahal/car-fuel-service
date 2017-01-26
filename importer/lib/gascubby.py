import csv
import datetime
import time
import os

from fuel.models import FillUp, Brand, Location, Payment


class GasCubbyImporter:

    def __init__(self, file, profile, car):
        self.car = car
        self.file = file
        self.profile = profile
        self.temp_file = None

    def validate(self):
        if type(self.file) == 'InMemoryUploadedFile' and self.file.content_type == 'text/csv':
            return True
        else:
            return False

    def save_temp_file(self):

        self.temp_file = '/tmp/import_u' + str(self.profile.id) + '_' + str(int(time.time())) + '.txt'

        with open(self.temp_file, 'wb') as destination:
            for chunk in self.file.chunks():
                destination.write(chunk)

    def import_csv(self):

        # if self.validate() is False:
        #     raise Exception
        self.save_temp_file()
        csv_file = open(self.temp_file, 'rt')
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['Type'] == 'Gas':
                fill = FillUp()
                fill.car = self.car
                fill.fuel_economy = row['MPG']
                date_object = datetime.datetime.strptime(row['Date'] + ' ' + row['Time'], '%Y-%m-%d %I:%M %p')
                fill.date_time = date_object

                try:
                    if row['Odometer'] == '':
                        fill.odometer = None
                    else:
                        fill.odometer = float(row['Odometer'].replace(',', ''))
                except Exception as e:
                    print(row['Odometer'], e)

                fill.octane = row['Octane']

                fill.unit_cost_per = float(row['Cost/Gallon'][1:])
                fill.unit_quantity = row['Gallons']
                fill.total_cost = float(row['Total Cost'][1:])

                fill.filled_up = FillUp.key_for_fill_up_value(row['Filled Up'])

                if row['Gas Brand'] != '':
                    brand, created = Brand.objects.get_or_create(
                        name=row['Gas Brand'],
                        user=self.profile,
                    )
                    fill.fuel_brand = brand

                if row['Location'] != '':
                    location, created = Location.objects.get_or_create(
                        name=row['Location'],
                        user=self.profile,
                    )
                    fill.location = location

                if row['Payment Type'] != '':
                    payment, created = Payment.objects.get_or_create(
                        name=row['Payment Type'],
                        user=self.profile,
                    )
                    fill.payment = payment

                fill.notes = row['Notes']
                fill.tags = row['Tags']
                fill.services = row['Services']

                fill.user = self.profile
                fill.save(is_import=True)
        return True

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.temp_file)