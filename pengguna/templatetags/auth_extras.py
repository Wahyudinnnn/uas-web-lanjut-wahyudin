import datetime

from django import template
from django.contrib.auth.models import Group


register = template.Library()


@register.filter(name='my_group')
def my_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
    except:
        group = Group.objects.create(name=group_name)
    return True if group in user.groups.all() else False