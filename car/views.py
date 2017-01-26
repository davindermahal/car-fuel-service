from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotAllowed
from django.urls import reverse
from .models import Car
from .forms import CarForm
from accounts.models import MyProfile


def index(request):
    if request.user.is_authenticated():
        car_list = Car.objects.all().filter(user=request.user.id)
        context = {'car_list': car_list}
        return render(request, 'car_index.html', context)
    else:
        return HttpResponseRedirect('/accounts/signin/')


def detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'car_detail.html', {'car': car})


def add(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            my_profile = MyProfile.objects.get(user_id=request.user.id)
            car.user = my_profile
            car.save()

            return HttpResponseRedirect(reverse('car_detail', args=[car.id]))
    else:
        form = CarForm()

    return render(request, 'car_add.html', {'form': form})


def edit(request, car_id):
    car = get_object_or_404(Car, pk=car_id, user_id=request.user.id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            my_profile = MyProfile.objects.get(user_id=request.user.id)
            car.user = my_profile
            car.save()

            return HttpResponseRedirect(reverse('car_detail', args=[car.id]))
    else:
        form = CarForm(instance=car)

    return render(request, 'car_edit.html', {'form': form, 'car': car})