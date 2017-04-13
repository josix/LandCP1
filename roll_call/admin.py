from django.contrib import admin
from roll_call.models import set_number,set_time,attendence

# Register your models here.

admin.site.register(set_number)
admin.site.register(set_time)
admin.site.register(attendence)