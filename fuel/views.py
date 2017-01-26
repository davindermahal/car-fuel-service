from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import FillUp
from .forms import FillUpForm, CustomFillUpForm
from accounts.models import MyProfile
from car.models import Car


def view_for_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id, user_id=request.user.id)
    fill_up_list = FillUp.objects.filter(user=request.user.id, car=car_id).order_by('-date_time')
    return render(request, 'fill_up_index.html', {'fill_up_list': fill_up_list, 'car': car})


def edit(request, car_id, fill_up_id):
    car = get_object_or_404(Car, pk=car_id, user_id=request.user.id)

    fill_up = get_object_or_404(FillUp, pk=fill_up_id)
    if request.method == 'POST':
        form = CustomFillUpForm(request.POST, instance=fill_up, car_id=car.id, user_id=request.user.id)

        if form.is_valid():
            form.save()
            url = reverse('fuel_view_for_car', args=[car.id])
            return HttpResponseRedirect(url)
    else:

        form = CustomFillUpForm(instance=fill_up, car_id=car.id, user_id=request.user.id)

    return render(request, 'edit.html', {'form': form, 'fill_up_id': fill_up_id, 'car': car})


def detail(request, car_id, fill_up_id):
    fill_up = get_object_or_404(FillUp, pk=fill_up_id)
    car = get_object_or_404(Car, pk=car_id, user_id=request.user.id)

    return render(request, 'fill_up_detail.html', {'fill_up': fill_up, 'car': car})


# def add_for_car(request, car_id):
#     car = get_object_or_404(Car, pk=car_id, user_id=request.user.id)
#
#     if request.method == 'POST':
#         form = FillUpForm(request.POST, car_id=car.id, user_id=request.user.id)
#
#         if form.is_valid():
#             fill_up = form.save(commit=False)
#             my_profile = MyProfile.objects.get(user_id=request.user.id)
#             fill_up.user = my_profile
#             fill_up.save()
#             return HttpResponseRedirect(reverse('fuel_view_for_car', args=[car.id]))
#     else:
#         form = FillUpForm(car_id=car.id, user_id=request.user.id)
#
#     return render(request, 'add.html', {'form': form, 'car': car})

def add_for_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id, user_id=request.user.id)

    if request.method == 'POST':
        form = CustomFillUpForm(request.POST, car_id=car.id, user_id=request.user.id)

        if form.is_valid():
            my_profile = MyProfile.objects.get(user_id=request.user.id)

            fill_up = FillUp()
            fill_up.set_properties_from_form(form.cleaned_data)
            fill_up.user = my_profile
            fill_up.car = car
            fill_up.save()

            return HttpResponseRedirect(reverse('fuel_view_for_car', args=[car.id]))
    else:
        form = CustomFillUpForm(car_id=car.id, user_id=request.user.id)

    return render(request, 'add.html', {'form': form, 'car': car})
