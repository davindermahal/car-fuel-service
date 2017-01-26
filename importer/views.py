
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from car.models import Car
from .forms import ImporterForm
from accounts.models import MyProfile
from .lib.gascubby import GasCubbyImporter


def upload_file(request, car_id):
    car = get_object_or_404(Car, pk=car_id, user_id=request.user.id)

    if request.user.is_authenticated():
        if request.method == "POST":
            form = ImporterForm(request.POST, request.FILES)
            if form.is_valid():
                my_profile = MyProfile.objects.get(user_id=request.user.id)
                importer = GasCubbyImporter(request.FILES['csv_file'], my_profile, car)
                if importer.import_csv():
                    return HttpResponseRedirect(reverse('importer_add', kwargs={'car_id': car_id, 'error': 'Error importing file.'}))
                else:
                    return HttpResponseRedirect(reverse('importer_add', kwargs={'car_id': car_id}))
        else:
            form = ImporterForm()
            return render(request, 'importer_index.html', {'car': car, 'form': form})
