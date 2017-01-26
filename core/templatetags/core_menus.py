from django import template
from car.models import Car

register = template.Library()


@register.inclusion_tag('header_menus.html')
def show_menus(user):
    cars = Car.objects.filter(user_id=user.id)
    return {'cars': cars}
